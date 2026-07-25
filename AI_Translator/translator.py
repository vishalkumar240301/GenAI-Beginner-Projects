from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create OpenAI client
client = OpenAI()

# Display application title
print("=" * 45)
print("        AI TRANSLATOR")
print("=" * 45)

# Display available source languages
print("\nSelect your Source Language\n")
print("1. English")
print("2. Hindi")
print("3. French")
print("4. Spanish")
print("5. Tamil")

# Keep asking until the user selects a valid source language
while True:
    source_choice = input("\nSelect your Source Language (1-5): ")

    if source_choice in ["1", "2", "3", "4", "5"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, 3, 4, or 5.")

# Display available target languages
print("\nSelect your Target Language\n")
print("1. English")
print("2. Hindi")
print("3. French")
print("4. Spanish")
print("5. Tamil")

# Keep asking until the user selects a valid target language
while True:
    target_choice = input("\nSelect your Target Language (1-5): ")

    if target_choice in ["1", "2", "3", "4", "5"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, 3, 4, or 5.")

# Prevent translation when both languages are the same
if source_choice == target_choice:
    print("\n❌ Source and Target languages cannot be the same.")
    exit()

# Keep asking until the user enters some text
while True:
    text = input("\nEnter text to translate:\n")

    if text.strip():
        break

    print("\n❌ Text can't be empty.")

# Store language names for each menu option
languages = {
    "1": "English",
    "2": "Hindi",
    "3": "French",
    "4": "Spanish",
    "5": "Tamil"
}

# Convert numeric choices into language names
source_language = languages[source_choice]
target_language = languages[target_choice]

# Display user's selections before translation
print("\nSource Language:", source_language)
print("Target Language:", target_language)

print("\nText to Translate:")
print(text)

print("\nGenerating Translation...\n")

try:
    # Send translation request to OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert language translator."
            },
            {
                "role": "user",
                "content": f"""
Translate the following text from {source_language} to {target_language}.

Text:
{text}
"""
            }
        ]
    )

    # Display translated text
    print("=" * 45)
    print("TRANSLATED TEXT")
    print("=" * 45)

    translation = response.choices[0].message.content
    print(translation)

# Handle unexpected errors
except Exception as e:
    print("\n❌ Something went wrong!")
    print(f"Error: {e}")