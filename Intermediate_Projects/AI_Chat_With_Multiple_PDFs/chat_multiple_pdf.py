from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os

load_dotenv()

client = OpenAI()

print("=" * 45)
print("🤖 AI CHAT WITH MULTIPLE PDFs")
print("=" * 45)

# -----------------------------
# Locate PDF Folder
# -----------------------------
pdf_folder = "PDFs"

# -----------------------------
# Find all PDF files
# -----------------------------
pdf_files = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        pdf_files.append(file)

print(f"\n📄 Found {len(pdf_files)} PDF(s)\n")

# -----------------------------
# Read all PDFs
# -----------------------------
all_pdf_text = ""

print("Loading PDFs...\n")

for pdf in pdf_files:

    pdf_path = os.path.join(pdf_folder, pdf)

    reader = PdfReader(pdf_path)

    pdf_text = ""

    for page in reader.pages:
        pdf_text += page.extract_text() or ""

    all_pdf_text += pdf_text + "\n"

    print(f"✅ {pdf} loaded")

print("\n" + "-" * 45)

print(f"\nTotal Characters Extracted: {len(all_pdf_text)}")

# -----------------------------
# System Prompt
# -----------------------------
system_prompt = """
You are an AI assistant.

Answer the user's question ONLY using the information provided in the PDFs.

If the answer is not available in the PDFs, politely say:

'I couldn't find that information in the provided PDFs.'

Do not make up information.
"""

system_message = {
    "role": "system",
    "content": system_prompt
}

print("\n" + "=" * 45)
print("📖 CHAT WITH MULTIPLE PDFs")
print("Type 'exit' to quit.")
print("=" * 45)

# -----------------------------
# Chat Loop
# -----------------------------
while True:

    user_question = input("\n❓ Ask your question: ").strip()

    if user_question.lower() == "exit":
        print("\n👋 Thank you for using AI Chat With Multiple PDFs!")
        break

    if not user_question:
        print("\n❌ Question can't be empty.")
        continue

    user_message = {
        "role": "user",
        "content": f"""
PDF Content:

{all_pdf_text}

Question:

{user_question}
"""
    }

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