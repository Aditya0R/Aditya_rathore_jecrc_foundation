### Week 7 - RAG Document Question Answering System

## Project Title
Document Question Answering System using Retrieval-Augmented Generatio

A beginner-friendly **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions based on their content. The system retrieves the most relevant information from the uploaded document and generates answers using semantic search.

---

# 📌 Project Overview

Large Language Models (LLMs) have vast knowledge but cannot automatically access the contents of newly uploaded or private documents. This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on the language model's knowledge, the application first retrieves the most relevant sections from the uploaded PDF and then generates an answer based on that retrieved context.

This approach improves accuracy, reduces hallucinations, and enables question answering over custom documents.

---

# 🎯 Objectives

- Understand the concept of Retrieval-Augmented Generation (RAG)
- Build an end-to-end document question-answering system
- Learn document loading and preprocessing
- Generate semantic embeddings
- Store embeddings in a vector database
- Retrieve relevant document chunks
- Build an interactive Streamlit application

---

# ✨ Features

- 📄 Upload PDF documents
- 📖 Automatic text extraction
- ✂️ Intelligent text chunking
- 🔍 Semantic similarity search
- 🧠 Embedding generation using Sentence Transformers
- 🗂️ Vector storage using ChromaDB
- ❓ Ask questions from uploaded documents
- 📑 Display retrieved context chunks
- 💻 Simple and interactive Streamlit interface
- 🚀 Fully local embedding generation (No paid embedding API required)

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| PyPDFLoader | PDF Loading |
| RecursiveCharacterTextSplitter | Text Chunking |
| HuggingFace Sentence Transformers | Embedding Generation |
| ChromaDB | Vector Database |
| pypdf | PDF Processing |

---

# 📂 Project Structure

```
RAG_Document_Question_Answering
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── data
│
├── vector_db
│
└── screenshots
```

---

# ⚙️ System Architecture

```
                User
                  │
                  ▼
          Upload PDF Document
                  │
                  ▼
         PDF Text Extraction
                  │
                  ▼
           Text Chunking
                  │
                  ▼
      Embedding Generation
                  │
                  ▼
     Store Embeddings in ChromaDB
                  │
                  ▼
          User Question
                  │
                  ▼
      Convert Question to Vector
                  │
                  ▼
      Retrieve Similar Chunks
                  │
                  ▼
       Generate Final Answer
                  │
                  ▼
        Display Result
```

---

# 🔄 Workflow

### Step 1

User uploads a PDF document.

↓

### Step 2

The application extracts text from every page.

↓

### Step 3

The extracted text is divided into smaller chunks.

↓

### Step 4

Each chunk is converted into semantic embeddings.

↓

### Step 5

Embeddings are stored inside ChromaDB.

↓

### Step 6

The user's question is converted into an embedding.

↓

### Step 7

Similarity search retrieves the most relevant chunks.

↓

### Step 8

The retrieved context is shown as the answer.

---

# 📊 RAG Pipeline

```
PDF
   │
   ▼
Text Extraction
   │
   ▼
Chunking
   │
   ▼
Embeddings
   │
   ▼
Vector Database
   │
   ▼
Question
   │
   ▼
Similarity Search
   │
   ▼
Retrieved Context
   │
   ▼
Final Answer
```

---

# 📥 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/RAG_Document_Question_Answering.git
```

Move inside the project

```bash
cd RAG_Document_Question_Answering
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📚 Dataset

This project works with any PDF document, including:

- Notes
- Books
- Research Papers
- Resume
- Articles
- Documentation
- Reports

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- PDF Upload
- Generated Answer
- Retrieved Context

---

# 💡 Advantages

- Better factual accuracy
- Works on custom/private documents
- Reduces hallucinations
- Fast semantic search
- Easy to extend
- Beginner-friendly implementation

---

# 🚀 Future Improvements

- Multi-PDF support
- Chat history
- Voice-based question answering
- OCR support for scanned PDFs
- Hybrid search
- FAISS/Pinecone integration
- Multi-language support
- Better retrieval ranking

---

# 📖 Learning Outcomes

After completing this project, you will understand:

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Document Chunking
- Vector Databases
- Streamlit Application Development
- End-to-End AI Pipeline

# 👨‍💻 Author

**Aditya Rathore**
