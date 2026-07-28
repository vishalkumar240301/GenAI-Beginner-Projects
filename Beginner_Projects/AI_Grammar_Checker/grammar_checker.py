from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI()

SYSTEM_PROMPT = """
You are an expert English Grammar Checker.

Correct grammar, spelling, and punctuation mistakes.

Do not change the meaning of the sentence.

Return only the corrected sentence.
"""

# Display title
print("=" * 45)
print("\n 🤖 AI Grammmar Checker \n")
print("=" * 45)

# Ask user to enter text

while True:
    text = input("\n Enter your Sentence : \n")

    # Validate text
    if text.strip():
        break
    print("\n❌ Text can't be empty \n")
    print("\n Please enter a sentence.")

# Display "Checking Grammar..."
print("\n 🤖 Checking Grammar.... \n")

messages = [
    {"role" : "system", "content" : SYSTEM_PROMPT},
    {"role" : "user", "content" : text}
]

try:
    response = client.chat.completions.create(
        model= "gpt-4.1-mini",
        messages = messages
    )

    print("=" * 45)
    print("CORRECTED SENTENCE")
    print("=" * 45)

    grammar_check = response.choices[0].message.content
    print(grammar_check)

except Exception as e:
    print("\n❌ Something went wrong\n")
    print(f"Error :{e}")
