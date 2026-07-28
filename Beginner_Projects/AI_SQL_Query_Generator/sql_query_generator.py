from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("\n 🤖 AI SQL QUERY GENERATOR \n")
print("=" * 45)

print("\n 📈Enter Database Type: \n")
print("1 . MySQL")
print("2. PostgreSQL")
print("3. SQLite")
print("4. SQL Server")

while True:
    database_type = input("\n Select Database from (1-4) :")
    if database_type in ["1", "2", "3", "4"]:
        break
    print("\n❌ Invalid Database")
    print("\nSelect Database (1-4): ")

while True:
    table_name = input("\n Enter Table Name: \n")
    if table_name.strip():
        break
    print("\n ❌ Table Name can't be empty \n")
    print("\nEnter Table Name:")

while True:
    description = input("\n Describe what you want \n")
    if description.strip():
        break
    print("\n ❌ Description can't be empty \n")
    print("\n Please enter description \n")

print("\n Choose SQL Type \n")
print("1 . SELECT")
print("2. INSERT")
print("3 . UPDATE")
print("4. DELETE")
print("5. CREATE TABLE")
print("6. Custom")

while True:
    sql_type = input("\n Please select SQL Type: \n")
    if sql_type in ["1", "2", "3", "4", "5", "6"]:
        break
    print("\n ❌ Invalid Selection \n")
    print("\nPlease select from (1-6)")

database = {
    "1" : "MySQL",
    "2" : "PostgreSQL",
    "3" : "SQLite",
    "4" : "SQL Server"
}

sql_types = {
    "1" : "SELECT",
    "2" : "INSERT",
    "3" : "UPDATE",
    "4" : "DELETE",
    "5" : "CREATE TABLE",
    "6" : "Custom"
}

database_type = database[database_type]
sql_type = sql_types[sql_type]

if sql_type == "Custom":
    print("\nExamples:")
    print("- ALTER TABLE")
    print("- DROP TABLE")
    print("- TRUNCATE")
    print("- CREATE INDEX")

    while True:
        sql_type = input("\nEnter your custom SQL Type: ")

        if sql_type.strip():
            break

        print("\n❌ SQL Type can't be empty.")
        print("Please enter your SQL Type.")

print("=" * 45)
print("SQL COMMAND DETAILS")
print("=" * 45)

print(f"Database     : {database_type}")
print(f"Table Name   : {table_name}")
print(f"SQL Type     : {sql_type}")
print(f"Description  : {description}")

print("\n🤖 Generating SQL Query...\n")

SYSTEM_PROMPT = """
You are an expert SQL Query Generator.

Generate SQL queries based on the user's request.

Supported databases:
- MySQL
- PostgreSQL
- SQLite
- SQL Server

Supported SQL operations include:

- SELECT
- INSERT
- UPDATE
- DELETE
- CREATE TABLE

If the user provides a custom SQL operation (such as ALTER TABLE, DROP TABLE, TRUNCATE, CREATE INDEX, etc.), generate the appropriate SQL query.

Return only the SQL query.

Do not include explanations.

Do not include markdown.

Do not include ```sql.
"""

messages = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : f"""
            Database: {database_type}
            Table Name: {table_name}
            Description: {description}
            SQL Type: {sql_type}
        """
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("GENERATED SQL QUERY")
    print("=" * 45)

    sql_query = response.choices[0].message.content
    print(sql_query)

except Exception as e:
    print("\n ❌ Something went wrong \n")
    print(f"Error : {e}")
