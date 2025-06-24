import openai

openai.api_key = "your-api-key-here"

response = openai.ChatCompletion.create(
    model="gpt-4.0",
    messages=[{"role": "user", "content": "Hello, what can you do?"}]
)

print(response.choices[0].message['content'])