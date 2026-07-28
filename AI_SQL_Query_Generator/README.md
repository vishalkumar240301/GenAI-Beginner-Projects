# 🤖 AI SQL Query Generator

A beginner-friendly GenAI project that generates SQL queries using OpenAI GPT-4.1 Mini.

Users can choose the database, SQL operation, table name, and describe what they want. The AI generates the appropriate SQL query instantly.

---

## 🚀 Features

- Supports multiple databases
  - MySQL
  - PostgreSQL
  - SQLite
  - SQL Server
- Supports SQL operations
  - SELECT
  - INSERT
  - UPDATE
  - DELETE
  - CREATE TABLE
  - Custom SQL Operations
- User-friendly menu-driven interface
- Input validation
- OpenAI GPT-4.1 Mini integration
- Error handling

---

## 🛠️ Technologies Used

- Python
- OpenAI API
- python-dotenv

---

## ▶️ How to Run

1. Clone the repository

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate it

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file

```text
OPENAI_API_KEY=your_api_key_here
```

6. Run the project

```bash
python sql_query_generator.py
```

---

## 📸 Example

Database:
MySQL

Table:
Student

SQL Type:
SELECT

Description:
Show all students ordered by name

Output:

```sql
SELECT *
FROM Student
ORDER BY student_name ASC;
```

---

## 👨‍💻 Author

**Vishal Kumar**