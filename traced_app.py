
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Three different prompts
prompts = [
    "Explain Artificial Intelligence in simple words with an example.",

    "Write a short motivational message for students learning Python programming.",

    "Explain how LangChain and LangSmith work together in an AI application."
]

# Execute all three prompts
for index, prompt in enumerate(prompts, start=1):

    print("\n" + "=" * 60)
    print(f"RUN {index}")
    print("=" * 60)

    print("\nPROMPT:")
    print(prompt)

    # Send prompt to OpenAI through LangChain
    response = llm.invoke(prompt)

    print("\nRESPONSE:")
    print(response.content)

    print("\n" + "=" * 60)

print("\nAll three prompts completed successfully!")