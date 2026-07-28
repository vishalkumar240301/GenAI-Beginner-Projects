# 🤖 AI Resume Bullet Generator

A beginner-friendly Generative AI project built using **Python** and the **OpenAI API**.

This application generates professional, ATS-friendly resume bullet points based on the user's job role, years of experience, and work description.

---

## 🚀 Features

- Generate professional resume bullet points
- ATS-friendly bullet points
- Strong action verbs
- Input validation
- Uses OpenAI GPT-4.1 Mini
- Clean command-line interface (CLI)

---

## 📋 User Inputs

- Job Role
- Years of Experience
- Work Description

---

## 🛠️ Technologies Used

- Python
- OpenAI API
- python-dotenv

---

## 📁 Project Structure

```
AI_Resume_Bullet_Generator/
│
├── resume_bullet_generator.py
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
cd AI_Resume_Bullet_Generator
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

Run the application

```bash
python resume_bullet_generator.py
```

---

## 📸 Example

### Input

```
Job Role            : React Developer
Experience          : 3 Years
Work Description    : Developed frontend applications using React.js and collaborated with backend developers.
```

### Output

```
• Developed responsive web applications using React.js.

• Collaborated with cross-functional teams to deliver scalable frontend solutions.

• Integrated REST APIs to improve application functionality.

• Optimized UI performance and enhanced user experience.

• Followed best coding practices and maintained high-quality code.
```

---

## 📚 What I Learned

- Prompt Engineering
- Python Input Validation
- OpenAI Chat Completions API
- Building CLI Applications
- Error Handling with try-except
- Generating ATS-friendly Resume Content

---

## 👨‍💻 Author

**Vishal Kumar**

Learning Generative AI by building beginner-friendly projects.