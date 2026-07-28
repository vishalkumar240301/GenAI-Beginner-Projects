# 🤖 AI Quiz Generator

An AI-powered Quiz Generator built using Python and OpenAI GPT-4.1 Mini.

This application generates multiple-choice quizzes on any topic with different difficulty levels.

## 🚀 Features

- Generate quizzes on any topic
- Beginner, Intermediate and Advanced difficulty
- Choose number of questions
- Four options for every question
- Correct answer included
- Simple command-line interface
- Input validation
- Uses OpenAI GPT-4.1 Mini

## 🛠️ Technologies Used

- Python
- OpenAI API
- python-dotenv

## 📂 Project Structure

```
AI_Quiz_Generator/
│
├── quiz_generator.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

## ▶️ How to Run

Clone the repository

```
git clone https://github.com/vishalkumar240301/GenAI-Beginner-Projects.git
```

Move into the project

```
cd AI_Quiz_Generator
```

Create virtual environment

```
python -m venv venv
```

Activate it

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create a `.env` file

```
OPENAI_API_KEY=your_api_key
```

Run

```
python quiz_generator.py
```

## 📌 Example

Topic:
```
Python
```

Difficulty:
```
Intermediate
```

Questions:
```
10
```

The application generates multiple-choice questions with four options and the correct answer.

## 👨‍💻 Author

**Vishal Kumar**