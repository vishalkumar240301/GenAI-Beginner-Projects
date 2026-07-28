from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI()

print("=" * 45)
print("        AI TEXT SUMMARIZER")
print("=" * 45)

print("\nChoose Summary Type:\n")
print("1. Short Summary")
print("2. Detailed Summary")
print("3. Bullet Points")

# Validate choice
while True:
    choice = input("\nEnter your choice (1-3): ")

    if choice in ["1", "2", "3"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, or 3.")

# Get article
while True:
    article = input("\nPaste your article:\n\n")

    if article.strip():
        break

    print("\n❌ Article cannot be empty.")

print("\nGenerating Summary...\n")

# System prompt based on user choice
if choice == "1":
    instruction = "Generate a short summary in 2-3 sentences."
elif choice == "2":
    instruction = "Generate a detailed summary."
else:
    instruction = "Generate the summary in bullet points."

# Call OpenAI API
try:
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert text summarizer."
            },
            {
                "role": "user",
                "content": f"""
                {instruction}

                Article:
                {article}
                """
            }
        ]
    )

    # Display summary
    print("=" * 45)
    print("SUMMARY")
    print("=" * 45)

    summary = response.choices[0].message.content

    print(summary)

except Exception as e:
    print("\n❌ Something went wrong!")
    print(f"Error: {e}")