from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
from tqdm import tqdm  
data = pd.read_csv('train.csv')

#This file creates the embeddings from the train.csv file. The embeddings are saved in a new file called document_embeddings.csv. 
# No need to run this file if document_embeddings.csv is already present in the directory.

data['text'] = data['title'] + " " + data['abstract'] + " " + data['Keywords']

model_name = "allenai/scibert_scivocab_uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_embeddings(text, model, tokenizer, max_length=512):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=max_length)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    return outputs.last_hidden_state.mean(dim=1).squeeze()

tqdm.pandas()

data['embedding'] = data['text'].progress_apply(lambda x: get_embeddings(x, model, tokenizer))

data['embedding'] = data['embedding'].apply(lambda x: x.tolist())

data[['uuid', 'title', 'abstract', 'author', 'embedding', ]].to_csv('document_embeddings.csv', index=False)
