# Youtube-Video-QA-Rag

This project is a Retrieval-Augmented Generation (RAG) based application that allows users to ask natural language questions about the content of YouTube videos.

The system extracts video transcripts, processes them into semantic embeddings, stores them in a vector database, and retrieves the most relevant video segments to answer user queries accurately.

---

## 🚀 Features

- Extract transcripts from YouTube videos
- Intelligent text chunking for long video content
- Semantic search using vector embeddings
- Fast similarity search using FAISS
- Question answering based on retrieved video context
- Modular and extensible RAG-based architecture
- Windows-compatible and API-free setup

---

## 🧠 Architecture Overview

1. **Transcript Extraction**
   - Fetches video transcripts using the YouTube Transcript API

2. **Text Chunking**
   - Splits transcripts into overlapping chunks to preserve context

3. **Embeddings Generation**
   - Converts transcript chunks into vector embeddings using Sentence Transformers

4. **Vector Database (FAISS)**
   - Stores embeddings and performs semantic similarity search

5. **Retrieval-Based Question Answering**
   - Retrieves the most relevant transcript segments for a given user query

---

## 🛠 Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- YouTube Transcript API
- Streamlit

---

## 📂 Project Structure

youtube-video-qa-rag/
│
├── app.py               # Streamlit application
├── transcript_loader.py # YouTube transcript extraction
├── vector_store.py      # FAISS vector store creation
├── qa_chain.py          # Retrieval-based QA logic
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md

---

## ▶️ How to Run the Project

1. Clone the repository
   git clone https://github.com/SciddhantoSinha/youtube-video-qa-rag.git

2. Navigate to the project directory
   cd youtube-video-qa-rag

3. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Run the application
   python -m streamlit run app.py

---

## ⚠️ Important Notes

- This project focuses on retrieval accuracy using RAG principles
- The generation layer is intentionally kept retrieval-based for stability on Windows
- The architecture supports future integration with OpenAI or local LLMs in Linux/WSL environments

---

## 📌 Future Enhancements

- Support for multi-video querying
- Timestamp-based answer referencing
- Conversational memory
- LLM-based summarization
- UI and UX improvements

---

## 👤 Author

Sciddhanto Sinha
