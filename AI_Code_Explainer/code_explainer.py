from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("🤖 AI CODE EXPLAINER")
print("=" * 45)

print("\n🧑‍💻 Paste your code below.")
print("\n Type END on a new line when you're finished.\n")

code_lines = []

while True:
    line = input()

    if line == "END":
        break

    code_lines.append(line)

code = "\n".join(code_lines)

if not code.strip():
    print("\n❌ Code can't be empty.")
    exit()

print("\n🤖 Analyzing Code...\n")

SYSTEM_PROMPT = """
You are an expert programming tutor.

Explain the provided code in beginner-friendly language.

Your response should include:

1. What the code does.
2. Line-by-line explanation.
3. Important programming concepts used.
4. Suggested improvements (if any).

Return only the explanation.

Do not repeat the entire code unless necessary.
"""

messages = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : code
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("CODE EXPLANATION")
    print("=" * 45)

    code_explanation = response.choices[0].message.content
    print(code_explanation)

except Exception as e:
    print("\n ❌ Something went wrong \n")
    print(f"Error: {e}")