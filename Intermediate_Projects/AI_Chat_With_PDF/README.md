# 🤖 AI Chat With PDF

A GenAI project that allows users to upload a PDF and ask questions based only on the contents of that PDF.

The application reads the PDF, extracts the text, sends the PDF content along with the user's question to GPT, and returns an answer grounded in the document.

---

## 🚀 Features

- Load any PDF file
- Validate file existence
- Extract text using pypdf
- Ask unlimited questions
- Continuous chat loop
- Exit anytime using `exit`
- Answer only from the PDF content
- Prevent hallucinations using prompt engineering

---

## 📁 Project Structure

```
AI_Chat_With_PDF/
│
├── sample.pdf
├── chat_with_pdf.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🛠️ Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python chat_with_pdf.py
```

---

## 📚 Technologies Used

- Python
- OpenAI API
- pypdf
- python-dotenv

---

## 📖 Example

Question:

```
What is HTML?
```

Answer:

```
HTML stands for Hyper Text Markup Language.
```

---

## ⚠️ Limitation

This version sends the entire PDF content to the LLM.

Large PDFs may exceed token limits.

Future versions will implement:

- Chunking
- Embeddings
- Retrieval
- Vector Databases
- Full RAG Pipeline

---

## 👨‍💻 Author

Vishal Kumar