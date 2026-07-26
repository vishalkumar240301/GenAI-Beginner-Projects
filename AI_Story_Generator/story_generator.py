from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI()

# Display application title
print("=" * 45)
print("🤖 AI STORY GENERATOR")
print("=" * 45)

# Display story genre options
print("\nChoose Story Genre\n")
print("1. Fantasy")
print("2. Horror")
print("3. Sci-Fi")
print("4. Mystery")
print("5. Adventure")
print("6. Custom")

# Validate story genre
while True:
    story_genre = input("\nChoose Story Genre (1-6): ")

    if story_genre in ["1", "2", "3", "4", "5", "6"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2, 3, 4, 5 or 6.")

# Story genre dictionary
genres = {
    "1": "Fantasy",
    "2": "Horror",
    "3": "Sci-Fi",
    "4": "Mystery",
    "5": "Adventure",
    "6": "Custom"
}

story_genre = genres[story_genre]

# Ask for custom genre if selected
if story_genre == "Custom":
    while True:
        custom_genre = input("\nEnter your custom story genre: ")

        if custom_genre.strip():
            story_genre = custom_genre
            break

        print("\n❌ Genre can't be empty.")
        print("Please enter your custom genre.")

# Character Name
while True:
    character_name = input("\nEnter Main Character Name: ")

    if character_name.strip():
        break

    print("\n❌ Character name can't be empty.")
    print("Please enter character name.")

# Story Setting
while True:
    story_setting = input("\nEnter Story Setting: ")

    if story_setting.strip():
        break

    print("\n❌ Story Setting can't be empty.")
    print("Please enter story setting.")

# Story Length
print("\nChoose Story Length\n")
print("1. Short")
print("2. Medium")
print("3. Long")

while True:
    story_length = input("\nPlease select story length (1-3): ")

    if story_length in ["1", "2", "3"]:
        break

    print("\n❌ Invalid choice!")
    print("Please select 1, 2 or 3.")

story_lengths = {
    "1": "Short",
    "2": "Medium",
    "3": "Long"
}

story_length = story_lengths[story_length]

# Display user selections
print("\n" + "=" * 45)
print("STORY DETAILS")
print("=" * 45)

print(f"Story Genre     : {story_genre}")
print(f"Character Name  : {character_name}")
print(f"Story Setting   : {story_setting}")
print(f"Story Length    : {story_length}")

print("\nGenerating Story...\n")

SYSTEM_PROMPT = """
You are an expert AI Story Generator.

Generate an engaging and creative story based on the user's inputs.

The story should match:
- Story Genre
- Main Character
- Story Setting
- Story Length

If the user selects:
- Short → Generate a short story.
- Medium → Generate a medium-length story.
- Long → Generate a detailed story.

Return only the story.

Do not include explanations or headings.
"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": f"""
Story Genre: {story_genre}

Main Character: {character_name}

Story Setting: {story_setting}

Story Length: {story_length}
"""
    }
]

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    print("=" * 45)
    print("GENERATED STORY")
    print("=" * 45)

    generated_story = response.choices[0].message.content
    print(generated_story)

except Exception as e:
    print("\n❌ Something went wrong.")
    print(f"Error: {e}")