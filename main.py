import openai


client = openai.OpenAI(
    api_key="Your_Api",
    base_url="https://openrouter.ai/api/v1"
)

def chat_with_openrouter(prompt):

    try:
        # Generate response using GPT-3.5 Turbo model (you can change the model as needed)
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        # Return clean text output
        return response.choices[0].message.content.strip()

    except Exception as e:
        # Handle any errors gracefully
        return f" Error: {e}"

if __name__ == "__main__":
    print("OpenRouter Chatbot started! Type 'exit' or 'quit' to end.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! ")
            break

        # Get response
        response = chat_with_openrouter(user_input)

        print("Chatbot:", response)


