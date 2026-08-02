# 🤖 AI Chat With PDF - RAG

A beginner-friendly Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF documents.

The application uses OpenAI embeddings, ChromaDB, and GPT to retrieve relevant information from PDF files before generating an answer.

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split PDF text into smaller chunks
- 🧠 Generate embeddings using OpenAI
- 🗄️ Store embeddings in ChromaDB
- 🔎 Retrieve relevant chunks based on the user's question
- 🤖 Generate answers using GPT
- 📚 Display source PDF files and page numbers
- 💾 Persist embeddings locally using ChromaDB
- ⚡ Skip embedding creation for already indexed PDFs
- 🛡️ Handle invalid questions and API errors

---

## 🧠 RAG Workflow

```text
PDF
 ↓
Extract Text
 ↓
Split Text into Chunks
 ↓
Create Embeddings
 ↓
Store in ChromaDB
 ↓
User Question
 ↓
Create Question Embedding
 ↓
Similarity Search
 ↓
Retrieve Relevant Chunks
 ↓
Build Context
 ↓
Send Context + Question to GPT
 ↓
Generate Answer
 ↓
Display Sources