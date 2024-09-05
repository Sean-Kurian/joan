from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import faiss
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import CrossEncoder
import torch

# This file has two parts - the code for the Flask API (to take your query and return an answer via an API endpoint) and the code for the FAISS index and the CrossEncoder model.

NUM_FAISS_DOCUMENTS = 10
NUM_LLM_RERANKED_DOCUMENTS = 5
app = Flask(__name__)

df = pd.read_csv('document_embeddings.csv')  # Renamed 'data' to 'df'

df['embedding'] = df['embedding'].apply(lambda x: np.array(eval(x)))

dimension = len(df['embedding'][0])

# Create a FAISS index
index = faiss.IndexFlatL2(dimension)  # L2 distance is Euclidean distance
embeddings = np.vstack(df['embedding'].values)
index.add(embeddings)

model_name = "allenai/scibert_scivocab_uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Load the CrossEncoder model for reranking
relevance_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')

def get_query_embedding(query, model, tokenizer, max_length=512):
    inputs = tokenizer(query, return_tensors='pt', padding=True, truncation=True, max_length=max_length)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def rerank_with_local_model(query, documents, relevance_model):
    reranked_results = []
    pairs = []
    
    for idx, row in documents.iterrows():
        text_pair = (query, row['title'] + " " + row['abstract'])
        pairs.append(text_pair)
    
    scores = relevance_model.predict(pairs)

    for idx, score in enumerate(scores):
        row = documents.iloc[idx]
        reranked_results.append((row['uuid'], row['title'], row['abstract'], score))

    reranked_results.sort(key=lambda x: x[3], reverse=True)
    
    return reranked_results[:NUM_LLM_RERANKED_DOCUMENTS]

@app.route('/search', methods=['POST'])
def search():
    request_data = request.json 
    query = request_data.get('query')
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    query_embedding = get_query_embedding(query, model, tokenizer)

    # Search the FAISS index
    D, I = index.search(np.array([query_embedding]), k=NUM_FAISS_DOCUMENTS)

    # Retrieve the relevant documents
    relevant_documents = df.iloc[I[0]].copy()
    relevant_documents.loc[:, 'score'] = D[0]

    # Rerank the documents using the CrossEncoder
    reranked_results = rerank_with_local_model(query, relevant_documents, relevance_model)

    response = [
        {
            "uuid": str(r[0]),
            "title": r[1],
            "abstract": r[2],
            "relevance_score": float(r[3]),
        }
        for r in reranked_results
    ]

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
