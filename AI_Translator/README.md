# 🌍 AI Translator

A beginner Generative AI project that translates text between multiple languages using the OpenAI API.

## Supported Languages

- English
- Hindi
- French
- Spanish
- Tamil

## Features

- Source Language Selection
- Target Language Selection
- Input Validation
- Prevent Same Source & Target Language
- Error Handling
- Clean Console Interface

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
python app.py
```

## Project Structure

```
AI_Translator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Learning Outcomes

- Prompt Engineering
- Dynamic Prompt Construction
- Dictionary Mapping
- Input Validation
- Error Handling