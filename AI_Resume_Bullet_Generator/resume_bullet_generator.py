from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("\n 🤖 AI Resume Bullet Generator \n")
print("=" * 45)

while True:
    job_role = input("\n Please enter Job Role \n")
    if job_role.strip():
        break
    print("\n ❌ Job Role can't be empty \n")
    print("\n Please enter Job Role \n")

while True:
    years_of_experience = input("\n Please enter your overall expereince \n")
    if years_of_experience.strip().isdigit():
        break
    print("\n ❌ Please enter a valid number for years of experience. \n")
    print("\n Please enter your overall experience \n")

while True:
    work_description = input("\n Please enter you work description \n")
    if work_description.strip():
        break
    print("\n ❌ Work Description can't be empty \n")
    print("\n Please enter work description \n")

print(f"Job Role            : {job_role}")
print(f"Experience          : {years_of_experience}")
print(f"Work Description    : {work_description}")

print("\n Generating Resume Bullet Points... \n")

SYSTEM_PROMPT = """
Generate 4 to 6 ATS-friendly resume bullet points.

Use strong action verbs.

Quantify achievements whenever possible.

Keep each bullet under 25 words.

Return only the bullet points.
"""

messages = [
    {
        "role" : "system", 
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : f"""
            Job Role: {job_role}
            Experience: {years_of_experience} Years
            Work Description: {work_description}
        """
    }   
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("AI RESUME BULLET GENERATOR")
    print("=" * 45)

    resume_bullet_generator = response.choices[0].message.content
    print(resume_bullet_generator)

except Exception as e:
    print("\n ❌ Something went wrong \n")
    print(f"Error : {e}")