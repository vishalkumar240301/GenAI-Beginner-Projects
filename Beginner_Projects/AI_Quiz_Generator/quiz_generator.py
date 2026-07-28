from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("🤖 AI Quiz Generator")
print("=" * 45)

while True:
    topic = input("\n Topic: \n")
    if topic.strip():
        break
    print("\n ❌ Topic can't be empty \n")
    print("\n Please enter Topic \n")

print("\n Difficulty: \n")
print("1. Beginner")
print("2. Intermediate")
print("3. Advanced")

while True:
    difficulty = input("\n Please enter quiz difficult level : ")
    if difficulty in ["1", "2", "3"]:
        break
    print("\n ❌ Inavlid choice \n")
    print("\n Enter from 1, 2 or 3 \n")

print("\n Number of Questions \n")
print("1. 5")
print("2. 10")
print("3. 15")

while True:
    number_of_questions = input("\n Enter Number of Questions : \n")
    if number_of_questions in ["1", "2", "3"]:
        break
    print("\n ❌ Inavlid selection \n")
    print("\n Please select from 1, 2 or 3 \n")

difficulties = {
    "1" : "Beginner",
    "2" : "Intermediate",
    "3" : "Advanced"
}

questions = {
    "1" : "5",
    "2" : "10",
    "3" : "15"
}

difficulty = difficulties[difficulty]
number_of_questions = questions[number_of_questions]

print("=" * 45)
print("QUIZ DETAILS")
print("=" * 45)

print(f"Topic : {topic}")
print(f"Difficulty : {difficulty}")
print(f"Number of Questions : {number_of_questions}")

print("\n🤖 Generating Quiz...\n")


SYSTEM_PROMPT = """
You are an expert Quiz Generator.

Generate multiple-choice quiz questions based on:

- Topic
- Difficulty Level
- Number of Questions

Rules:

- Each question should have exactly four options (A, B, C, D).
- Mention the correct answer after each question.
- Number every question.
- Do not provide explanations.
"""

messages = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : f"""
            Topic : {topic}
            Difficulty : {difficulty}
            Number of question : {number_of_questions}
            """
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("GENERATED QUIZ")
    print("=" * 45)

    generated_quiz = response.choices[0].message.content
    print(generated_quiz)

except Exception as e:
    print("\n ❌ Something went wrong \n")
    print(f"Error : {e}")


