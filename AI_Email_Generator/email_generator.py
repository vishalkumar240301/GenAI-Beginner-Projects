from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI()

# Display application title
print("=" * 45)
print("        AI EMAIL GENERATOR")
print("=" * 45)

# Display email type options
print("\n✉️ Please Choose Email Type\n")
print("1. Leave Request")
print("2. Job Application")
print("3. Meeting Request")
print("4. Thank You")
print("5. Complaint")
print("6. Custom")

# Validate email type
while True:
    email_type = input("\nPlease enter your choice (1-6): ")

    if email_type in ["1", "2", "3", "4", "5", "6"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, 3, 4, 5 or 6.")

# Display tone options
print("\nPlease Select Email Tone\n")
print("1. Professional")
print("2. Friendly")
print("3. Formal")
print("4. Casual")

# Validate tone
while True:
    email_tone = input("\nPlease enter your choice (1-4): ")

    if email_tone in ["1", "2", "3", "4"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, 3 or 4.")

# Validate recipient
while True:
    email_recipient = input("\n Enter Recipient Name/Role: ")

    if email_recipient.strip():
        break

    print("\n❌ Email Recipient can't be empty.")
    print("Please enter email recipient.")

# Ask user for the reason/purpose
while True:
    reason = input("\nPlease enter the Reason/Purpose of the email:\n")

    if reason.strip():
        break

    print("\n❌ Reason can't be empty.")
    print("Please enter the reason again.")

# Dictionaries to convert menu choices into text
email_types = {
    "1": "Leave Request",
    "2": "Job Application",
    "3": "Meeting Request",
    "4": "Thank You",
    "5": "Complaint",
    "6": "Custom"
}

tones = {
    "1": "Professional",
    "2": "Friendly",
    "3": "Formal",
    "4": "Casual"
}

# Convert numeric choices into text
email_type = email_types[email_type]
email_tone = tones[email_tone]

# Display user selections
print("\n" + "=" * 45)
print("EMAIL DETAILS")
print("=" * 45)

print(f"Email Type      : {email_type}")
print(f"Email Tone      : {email_tone}")
print(f"Recipient       : {email_recipient}")
print(f"Reason          : {reason}")

print("\nGenerating Email...\n")

SYSTEM_PROMPT = """
You are an expert AI Email Generator.

Generate a professional and well-structured email.

Use the email type, tone, recipient, and reason provided by the user.

Return only the generated email.

Do not include explanations, notes, or markdown formatting.
"""

messages = [
    {"role" : "system", "content" : SYSTEM_PROMPT},
    {"role" : "user", "content" : 
     f""" Email Type: {email_type}

        Tone: {email_tone}

        Recipient: {email_recipient}

        Reason: {reason} """}
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    print("=" * 45)
    print("GENERATED EMAIL")
    print("=" * 45)

    generated_email = response.choices[0].message.content
    print(generated_email)

except Exception as e :
    print("\n ❌ Something went wrong")
    print(f"Error: {e}")