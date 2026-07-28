# 🤖 AI Text Summarizer

A beginner Generative AI project built using the OpenAI API.

This application summarizes long articles into different formats based on the user's choice.

## Features

- Short Summary
- Detailed Summary
- Bullet Point Summary
- Input Validation
- Error Handling using try-except

## Tech Stack

- Python
- OpenAI API
- python-dotenv

## How to Run

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate it

Windows

```bash
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file

```
OPENAI_API_KEY=your_api_key
```

5. Run

```bash
python app.py
```

## Project Structure

```
AI_Text_Summarizer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Learning Outcomes

- OpenAI Chat Completions API
- Prompt Engineering Basics
- User Input Validation
- Exception Handling