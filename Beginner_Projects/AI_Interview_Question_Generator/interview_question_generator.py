from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("\n 🤖 AI INTERVIEW QUESTION GENERATOR \n")
print("=" * 45)

while True:
    job_role = input("\n Enter Job Role: \n")
    if job_role.strip():
        break
    print("\n ❌ Job Role can't be empty \n")
    print("\n Please Enter Job Role \n")

while True:
    experience = input("\n Enter Experience (Years): \n")
    if experience.strip().isdigit():
        break
    print("\n ❌ Enter a valid experience \n")
    print("\n Please enter experience \n")

print("\n Choose Difficulty \n")
print("1. Beginner")
print("2. Intermediate")
print("3. Advanced")

while True:
    difficulty = input("\nEnter Difficulty (1-3): ")
    if difficulty in ["1", "2", "3"]:
        break
    print("\n ❌ Invalid selection \n")
    print("\n Please select from 1,2 or 3 \n")

print("\n Choose Number of Questions \n")
print("1. 5")
print("2. 10")
print("3. 15")

while True:
    number = input("\n Enter number of questions: ")
    if number in ["1", "2", "3"]:
        break
    print("\n ❌ Inavlid selection \n")
    print("\n Please select from 1,2 or 3 \n")


difficulties  = {
    "1" : "Beginner",
    "2" : "Intermediate",
    "3" : "Advanced"
}

numbers = {
    "1" : "5",
    "2" : "10",
    "3" : "15"
}

difficulty = difficulties[difficulty]
number = numbers[number]

print("=" * 45)
print("QUESTION DETAILS")
print("=" * 45)

print(f"Job Role        : {job_role}")
print(f"Experience      : {experience}")
print(f"Difficulty      : {difficulty}")
print(f"No. Questions   : {number}")

print("\n Generating Interview Questions...\n")

SYSTEM_PROMPT = """
You are an expert technical interviewer.

Generate interview questions based on:

- Job Role
- Years of Experience
- Difficulty Level
- Number of Questions

Return only the interview questions.

Do not include answers, explanations, or headings.

Number each question.
"""

messages = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : f"""
            Job Role : {job_role}
            Experience : {experience}
            Difficulty : {difficulty}
            Number of Questions : {number}
        """
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("GENERATED INTERVIEW QUESTIONS")
    print("=" * 45)

    generated_questions = response.choices[0].message.content
    print(generated_questions)

except Exception as e:
    print("\n ❌ Something went wrong \n")
    print(f"Error: {e}")