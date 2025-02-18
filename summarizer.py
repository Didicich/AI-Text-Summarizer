import openai

openai.api_key = "your-api-key-here"

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    return response["choices"][0]["message"]["content"]

user_input = input("Enter text to summarize: ")
print("Summary:", summarize_text(user_input))
