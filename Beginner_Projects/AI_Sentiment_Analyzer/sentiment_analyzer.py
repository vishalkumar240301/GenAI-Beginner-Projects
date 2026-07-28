from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("=" * 45)
print("\n 🤖 AI SENTIMENT ANALYZER \n")
print("=" * 45)

while True:
    text = input("\n Please enter you review \n")
    if text.strip():
        break
    print("\n ❌Text can't be empty \n")
    print("\n Please enter you review \n")

print("\n🤖 Analyzing Sentiment...\n")

SYSTEM_PROMPT = """
You are an expert AI Sentiment Analyzer.

Analyze the user's text.

Classify it as exactly one of:
- Positive 😊
- Negative 😞
- Neutral 😐

Then provide a one-sentence explanation.

Return only the sentiment and explanation.
"""

messages = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    },
    {
        "role" : "user",
        "content" : text
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("\n SENTIMENT ANALYSIS \n")
    print("=" * 45)

    sentiment_analysis = response.choices[0].message.content
    print(sentiment_analysis)

except Exception as e:
    print("\n ❌Something went wrong \n")
    print(f"Error : {e}")