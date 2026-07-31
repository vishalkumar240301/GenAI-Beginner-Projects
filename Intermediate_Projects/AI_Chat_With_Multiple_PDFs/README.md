# 🤖 AI Chat With Multiple PDFs

A GenAI project that allows users to chat with multiple PDF documents using OpenAI's GPT model.

This project reads all PDF files from a folder, extracts their text, and allows the user to ask questions based on the combined content.

> ⚠️ This is Version 1 (Pre-RAG).
> It sends the complete PDF contents to the LLM, so it works only for small documents.

---

## 🚀 Features

- Read multiple PDFs automatically
- Extract text from every PDF
- Combine all document content
- Ask questions about the PDFs
- Continuous chat until the user exits

---

## 📁 Project Structure

```
AI_Chat_With_Multiple_PDFs/
│
├── PDFs/
│   ├── html_tutorial.pdf
│   ├── javabook.pdf
│   └── Node.pdf
│
├── chat_multiple_pdf.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🛠️ Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate it

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python chat_multiple_pdf.py
```

---

## 📚 Technologies Used

- Python
- OpenAI API
- pypdf
- python-dotenv

---

## ⚠️ Limitation

This version sends the complete contents of every PDF to the LLM.

Large PDFs may exceed the model's context window or token limit.

The next version will implement **Text Chunking** and later **Retrieval-Augmented Generation (RAG)**.

---

## 👨‍💻 Author

Vishal Kumar