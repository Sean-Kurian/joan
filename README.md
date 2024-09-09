
# JOAN - Journal Optimized AI Navigator

JOAN (Journal Optimized AI Navigator) is a sample RAG application that uses AI-optimized embeddings to help you find the most relevant medical research documents. The model is trained on medical paper titles and abstracts from [this dataset on Kaggle](https://www.kaggle.com/datasets/wolfmedal/medical-paper-title-and-abstract-dataset?resource=download&select=train.csv). By default, JOAN returns the top 5 most relevant documents based on a given query.

## Features
- Uses FAISS for fast nearest-neighbor search.
- Reranks documents with a cross-encoder model (MS MARCO).
- Easily queryable via a REST API.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/joan.git
cd joan
```

### 2. (Optional) Create a Virtual Environment
If you want to keep dependencies isolated, you can create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
Use `pip` to install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the API
Launch the Flask API by running:

```bash
python app.py
```

By default, the API will be available at `http://127.0.0.1:5000`.

## Usage Instructions

You can query the API using `curl` or Postman. Send a POST request to the `/search` endpoint with a JSON body containing your search query.

### Example Request
```bash
curl -X POST http://127.0.0.1:5000/search \
-H "Content-Type: application/json" \
-d '{"query": "Recent advancements in cancer treatment"}'
```

### Example JSON Request Body
```json
{
  "query": "Recent advancements in cancer treatment"
}
```

### Example Response
```json
[
    {
        "abstract": "The current challenges in cancer treatment using conventional therapies have made the emergence of nanotechnology with more advancements. The exponential growth of nanoscience has drawn to develop nanomaterials (NMs) with therapeutic activities. NMs have enormous potential in cancer treatment by altering the drug toxicity profile. Nanoparticles (NPs) with enhanced surface characteristics can diffuse more easily inside tumor cells, thus delivering an optimal concentration of drugs at tumor site while reducing the toxicity. Cancer cells can be targeted with greater affinity by utilizing NMs with tumor specific constituents. Furthermore, it bypasses the bottlenecks of indiscriminate biodistribution of the antitumor agent and high administration dosage. Here, we focus on the recent advances on the use of various nanomaterials for cancer treatment, including targeting cancer cell surfaces, tumor microenvironment (TME), organelles, and their mechanism of action. The paradigm shift in cancer management is achieved through the implementation of anticancer drug delivery using nano routes.",
        "relevance_score": 5.710176944732666,
        "title": "Nanomaterials in anticancer applications and their mechanism of action - A review",
        "uuid": "4410"
    },
    {
        "abstract": "Cancer is one of the deadliest diseases worldwide in present times, with its incidence on a tremendous rise. It is caused by uncontrolled cell growth. Cancer therapies have advanced substantially, but there is a need for improvement in specificity and fear of systemic toxicity. Early detection is critical in improving patients' prognosis and quality of life, and recent advancements in technology, especially in dealing with biomaterials, have aided in that surge. Nanotechnology possesses the key to solving many of the downsides of traditional pharmaceutical formulations. Indeed, significant progress has been made in using customized nanomaterials for cancer diagnosis and treatment with high specificity, sensitivity, and efficacy. Nanotechnology is the integration of nanoscience into medicine by the use of nanoparticles. The advent of nanoscience in cancer diagnosis and treatment will help clinicians better assess and manage patients and improve the healthcare system and services. This review article gives an account of the clinical applications of nanoscience in the modern management of cancer, the different modalities of nanotechnology used, and the limitations and possible side effects of this new tool.",
        "relevance_score": 4.790607452392578,
        "title": "The Application of Nanotechnology and Nanomaterials in Cancer Diagnosis and Treatment: A Review",
        "uuid": "5331"
    },
    {
        "abstract": "Despite exciting advances in targeted therapies, high drug costs, marginal therapeutic benefits and notable toxicities are concerning aspects of today's cancer treatments. This special issue of Seminars in Cancer Biology proposes a broad-spectrum, integrative therapeutic model to complement targeted therapies. Based on extensive reviews of the cancer hallmarks, this model selects multiple high-priority targets for each hallmark, to be approached with combinations of low-toxicity, low-cost therapeutics, including phytochemicals, adapted to the well-known complexity and heterogeneity of malignancy. A global consortium of researchers has been assembled to advance this concept, which is especially relevant in an era of rapidly expanding capacity for genomic tumor analyses, alongside alarming growth in cancer morbidity and mortality in low- and middle-income nations.",
        "relevance_score": 3.9049060344696045,
        "title": "A broad-spectrum integrative design for cancer prevention and therapy: The challenge ahead",
        "uuid": "681"
    },
    {
        "abstract": "Oncologic therapeutics has evolved enormously as we entered the 21st century. Unfortunately, the treatment of advanced urothelial cancer has remained unchanged over the last two decades despite a better understanding of the genetic alterations in bladder cancer. Pathways such as the PI3K/AKT3/mTOR and FGFR have been implicated in urothelial bladder cancer. However, targeted therapies have not shown proven benefit yet and are still considered investigational. Recently, researchers have been successful in manipulating the systemic immune response to mount antitumor effects in melanoma, lung cancer and lymphoma. Historically, intravesical Bacillus Calmette-Guérin immunotherapy has been highly active in nonmuscle invasive bladder cancer. Early data suggest that immune checkpoint inhibitors will soon prove to be another cornerstone in the treatment armamentarium of advanced bladder cancer.",
        "relevance_score": 3.183420181274414,
        "title": "Anti-PD-1 and PD-L1 therapy for bladder cancer: what is on the horizon?",
        "uuid": "2894"
    },
    {
        "abstract": "Brain metastases (BM) are an increasing challenge in the management of patients with advanced cancer. Treatment options for BM are limited and mainly focus on the application of local therapies. Systemic therapies including targeted therapies are only poorly investigated, as patients with BM were frequently excluded from clinical trials. Several targeted therapies have shown promising activity in patients with BM. In the present review we discuss existing and emerging targeted therapies for the most frequent BM primary tumor types. We focus on challenges in the conduction of clinical trials on targeted therapies in BM patients such as patient selection, combination with radiotherapy, the obstacles of the blood-brain barrier and the definition of study end points.",
        "relevance_score": 0.509122371673584,
        "title": "The future of targeted therapies for brain metastases",
        "uuid": "624"
    }
]
```

## Customization

- **Query**: Change the query in the request body to search for different medical topics.
- **Top Results**: By default, JOAN returns the top 5 most relevant results. You can modify this behavior by adjusting the code in \`app.py\` to retrieve a different number of documents.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
