from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI()

print("=" * 45)
print("🤖 AI CHAT WITH PDF")
print("=" * 45)

# -----------------------------
# Load PDF
# -----------------------------
while True:
    pdf_file = input("\n📄 Enter PDF file name (example: sample.pdf): ").strip()

    if not pdf_file:
        print("\n❌ File name cannot be empty.")
        continue

    if os.path.exists(pdf_file):
        break

    print("\n❌ PDF file not found. Please try again.")

reader = PdfReader(pdf_file)

pdf_text = ""

for page in reader.pages:
    pdf_text += page.extract_text() or ""

print("\n✅ PDF Loaded Successfully!")
print("\nFirst 1000 characters of the PDF:\n")
print("-" * 45)
print(pdf_text[:1000])
print("-" * 45)

# -----------------------------
# System Prompt
# -----------------------------
system_prompt = """
You are an AI assistant.

Answer the user's question ONLY using the information provided in the PDF.

If the answer is not available in the PDF, politely say:

'I couldn't find that information in the provided PDF.'

Do not make up information.
"""

# This never changes
system_message = {
    "role": "system",
    "content": system_prompt
}

print("\n" + "=" * 45)
print("📖 CHAT WITH THE PDF")
print("Type 'exit' to quit.")
print("=" * 45)

# -----------------------------
# Ask Questions
# -----------------------------
while True:

    user_question = input("\n❓ Ask your question: ").strip()

    if user_question.lower() == "exit":
        print("\n👋 Thank you for using AI Chat With PDF!")
        break

    if not user_question:
        print("\n❌ Question can't be empty.")
        continue

    # Create user message for current question
    user_message = {
        "role": "user",
        "content": f"""
PDF Content:

{pdf_text}

Question:

{user_question}
"""
    }

    # Final messages sent to OpenAI
    messages = [system_message, user_message]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )

        print("\n" + "=" * 45)
        print("ANSWER")
        print("=" * 45)

        answer = response.choices[0].message.content
        print(answer)

        print("\n" + "-" * 45)

    except Exception as e:
        print("\n❌ Something went wrong.")
        print(f"Error: {e}")