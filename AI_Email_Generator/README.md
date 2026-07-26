# 🤖 AI Email Generator

A beginner-friendly Generative AI project built using **Python** and the **OpenAI API**.

This application generates professional emails based on the user's selected email type, tone, recipient, and reason.

---

## 🚀 Features

- Generate different types of emails
- Multiple email categories
- Multiple writing tones
- Custom recipient support
- Input validation
- Uses OpenAI GPT-4.1 Mini
- Clean command-line interface (CLI)

---

## 📂 Email Types

- Leave Request
- Job Application
- Meeting Request
- Thank You
- Complaint
- Custom

---

## 🎭 Email Tones

- Professional
- Friendly
- Formal
- Casual

---

## 🛠️ Technologies Used

- Python
- OpenAI API
- python-dotenv

---

## 📁 Project Structure

```
AI_Email_Generator/
│
├── email_generator.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/vishalkumar240301/GenAI-Beginner-Projects.git
```

Go to the project folder

```bash
cd AI_Email_Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENAI_API_KEY=your_api_key_here
```

Run the project

```bash
python email_generator.py
```

---

## 📸 Example

```
Email Type      : Leave Request
Email Tone      : Professional
Recipient       : HR Manager
Reason          : Sick Leave
```

Generated Output

```
Subject: Sick Leave Request

Dear HR Manager,

...

Best Regards,
[Your Name]
```

---

## 📚 What I Learned

- Python input validation
- Prompt Engineering
- Using the OpenAI Chat Completions API
- Environment variables with python-dotenv
- Building interactive CLI applications
- Error handling using try-except

---

## 👨‍💻 Author

**Vishal Kumar**

Learning Generative AI by building beginner-friendly projects.