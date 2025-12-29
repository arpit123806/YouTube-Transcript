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
