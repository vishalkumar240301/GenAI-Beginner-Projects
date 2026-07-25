# ✍️ AI Grammar Checker

A Generative AI application that corrects grammar, spelling, and punctuation while preserving the original meaning of the sentence.

## Features

- Grammar Correction
- Spelling Correction
- Punctuation Correction
- Input Validation
- Error Handling
- Professional Prompt Design

## Tech Stack

- Python
- OpenAI API
- python-dotenv

## How to Run

1. Create virtual environment

```bash
python -m venv venv
```

2. Activate

```bash
venv\Scripts\activate
```

3. Install packages

```bash
pip install -r requirements.txt
```

4. Create `.env`

```
OPENAI_API_KEY=your_api_key
```

5. Run

```bash
python grammar_checker.py
```

## Project Structure

```
AI_Grammar_Checker/
│
├── grammar_checker.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Learning Outcomes

- System Prompts
- Prompt Engineering
- Input Validation
- OpenAI Chat Completions API
- Exception Handling