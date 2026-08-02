from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
import os
import hashlib


# --------------------------------
# 1. Setup
# --------------------------------

load_dotenv()

client = OpenAI()

print("=" * 55)
print("🤖 AI CHAT WITH PDF - RAG")
print("=" * 55)


# --------------------------------
# 2. Find PDFs
# --------------------------------

pdf_folder = "PDFs"

if not os.path.exists(pdf_folder):
    print("\n❌ PDFs folder not found.")
    exit()

pdf_files = [
    file
    for file in os.listdir(pdf_folder)
    if file.lower().endswith(".pdf")
]

if not pdf_files:
    print("\n❌ No PDF files found inside the PDFs folder.")
    exit()

print(f"\n📄 Found {len(pdf_files)} PDF(s)")


# --------------------------------
# 3. Create ChromaDB
# --------------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="pdf_documents"
)


# --------------------------------
# 4. Process PDFs
# --------------------------------

chunk_size = 1000
chunk_overlap = 200


for pdf_file in pdf_files:

    pdf_path = os.path.join(
        pdf_folder,
        pdf_file
    )

    print(f"\n📖 Processing: {pdf_file}")


    # --------------------------------
    # Create PDF fingerprint
    # --------------------------------

    with open(pdf_path, "rb") as file:

        pdf_hash = hashlib.md5(
            file.read()
        ).hexdigest()


    # --------------------------------
    # Check if this exact PDF
    # is already indexed
    # --------------------------------

    existing = collection.get(
        where={
            "$and": [
                {"source": pdf_file},
                {"file_hash": pdf_hash}
            ]
        }
    )


    if existing["ids"]:

        print("   ✅ PDF already indexed.")
        print("   ⏭️ Skipping embedding creation.")

        continue


    # --------------------------------
    # Read PDF
    # --------------------------------

    reader = PdfReader(pdf_path)

    print(
        f"   📄 Pages: {len(reader.pages)}"
    )


    # --------------------------------
    # Split PDF into chunks
    # --------------------------------

    pdf_chunks = []


    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        page_text = page.extract_text() or ""

        start = 0


        while start < len(page_text):

            end = start + chunk_size

            chunk = page_text[start:end]


            if chunk.strip():

                pdf_chunks.append(
                    {
                        "text": chunk,
                        "page": page_number
                    }
                )


            start += (
                chunk_size
                - chunk_overlap
            )


    print(
        f"   ✂️ Created {len(pdf_chunks)} chunks"
    )


    # --------------------------------
    # Create embeddings
    # --------------------------------

    print(
        "   🧠 Creating embeddings..."
    )


    for index, chunk_data in enumerate(
        pdf_chunks
    ):

        chunk_text = chunk_data["text"]


        embedding_response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk_text
        )


        embedding = (
            embedding_response
            .data[0]
            .embedding
        )


        # --------------------------------
        # Metadata
        # --------------------------------

        metadata = {

            "source": pdf_file,

            "page": chunk_data["page"],

            "chunk": index,

            "file_hash": pdf_hash
        }


        # --------------------------------
        # Store in ChromaDB
        # --------------------------------

        collection.upsert(

            ids=[
                f"{pdf_hash}_{index}"
            ],

            documents=[
                chunk_text
            ],

            embeddings=[
                embedding
            ],

            metadatas=[
                metadata
            ]
        )


    print(
        "   ✅ Embeddings stored successfully."
    )


print("\n" + "-" * 55)

print(
    f"📊 Total chunks in ChromaDB: "
    f"{collection.count()}"
)

print("-" * 55)


# --------------------------------
# 5. System Prompt
# --------------------------------

system_prompt = """
You are an AI assistant answering questions
using information retrieved from PDF documents.

Answer the user's question ONLY using the
provided context.

If the answer cannot be found in the context,
say:

"I couldn't find that information in the
provided PDFs."

Do not make up information.

Keep the answer clear and concise.
"""


# --------------------------------
# 6. Start Chat
# --------------------------------

print("\n" + "=" * 55)
print("📖 CHAT WITH YOUR PDFs")
print("Type 'exit' to quit.")
print("=" * 55)


while True:

    user_question = input(
        "\n❓ Ask your question: "
    ).strip()


    # --------------------------------
    # Exit
    # --------------------------------

    if user_question.lower() == "exit":

        print(
            "\n👋 Thank you for using "
            "AI Chat With PDF RAG!"
        )

        break


    # --------------------------------
    # Validate question
    # --------------------------------

    if not user_question:

        print(
            "\n❌ Question can't be empty."
        )

        continue


    try:

        # --------------------------------
        # 7. Embed user question
        # --------------------------------

        question_response = client.embeddings.create(

            model="text-embedding-3-small",

            input=user_question
        )


        question_embedding = (
            question_response
            .data[0]
            .embedding
        )


        # --------------------------------
        # 8. Retrieve relevant chunks
        # --------------------------------

        results = collection.query(

            query_embeddings=[
                question_embedding
            ],

            n_results=5
        )


        relevant_chunks = (
            results["documents"][0]
        )

        metadatas = (
            results["metadatas"][0]
        )


        # --------------------------------
        # 9. Build context
        # --------------------------------

        context_parts = []


        for chunk, metadata in zip(
            relevant_chunks,
            metadatas
        ):

            if metadata is None:
                continue


            context_parts.append(
                f"""
Source: {metadata.get("source", "Unknown")}
Page: {metadata.get("page", "Unknown")}

Content:

{chunk}
"""
            )


        if not context_parts:

            print(
                "\n❌ No relevant information "
                "was found in the PDFs."
            )

            continue


        context = "\n\n".join(
            context_parts
        )


        # --------------------------------
        # 10. User Prompt
        # --------------------------------

        user_prompt = f"""
Context from PDF documents:

{context}

Question:

{user_question}
"""


        # --------------------------------
        # 11. Ask GPT
        # --------------------------------

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ]
        )


        # --------------------------------
        # 12. Display Answer
        # --------------------------------

        answer = (
            response
            .choices[0]
            .message
            .content
        )


        print("\n" + "=" * 55)

        print("ANSWER")

        print("=" * 55)

        print(answer)


        # --------------------------------
        # 13. Display Sources
        # --------------------------------

        print("\n📚 SOURCES")


        shown_sources = set()


        for metadata in metadatas:

            if metadata is None:
                continue


            source = (

                metadata.get(
                    "source",
                    "Unknown"
                ),

                metadata.get(
                    "page",
                    "Unknown"
                )
            )


            if source not in shown_sources:

                print(
                    f"📄 {source[0]} "
                    f"(Page {source[1]})"
                )

                shown_sources.add(source)


        print(
            "\n" + "-" * 55
        )


    except Exception as e:

        print(
            "\n❌ Something went wrong."
        )

        print(
            f"Error: {e}"
        )