# Project Structure

├── └──L2_GENAI_ASSISMENT/
├── └──project\
├── └──src\
├──     └──services.py
├──     └──utils.py
├──  |──main.py
├──  |──requirements.txt
├──  |──.env
├──  |──.gitignore
└──  |──README.md

# .env variable
MODEL = Vector database Pinecone Embedding Model
PINECONE_API_KEY = Vector database Pinecone Api Key 
INDEX_NAME = Vector database Pinecone Index Name
ENVIRNOMENT = Vector database Pinecone Cloud Envirnoment
PINECONE_DIMENSION Vector database Pinecone Dimensions
AZURE_ENDPOINT = Azure Endpoint
AZURE_API_VERSION = Azure Api version
AZURE_API_KEY = Azure Api key
AZURE_MODEL = Azure Model
AZURE_DEVELOPMENT = Azure Development Model

# Activate virtual environment
cd project
For windows .venv\Scripts\activate
For Linux source .venv/bin/activate


# Features
* Query a YouTube video using natural language
└── Paste a YouTube video URl/ID
└── Chatbot fetches the transcript
└── Embeds & stores it in a vector databases i.e Pinecone
└── Ask unlimited queries without regenerating embeddings

* Smart Input Validation
└── Video Url cannot be blank
└── User query cannot be blank
└── Video Url filed locks after ingestion to prevent duplicate processing
└── Type "stop/exit/quit" reset the chatbot

* Chunking + Embedding + Semantic Search
└── Transcript is chunked
└── Chunks stored in Pinecone
└── LLM answer based only on retrieved chunks

* Clean UI
└── Built with Gradio
└── History panel
└── Auto-clean input fields
└── Clear button resets everything
