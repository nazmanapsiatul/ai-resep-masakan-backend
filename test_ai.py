from ollama import chat

response = chat(
    model='gemma3:1b',
    messages=[
        {
            'role': 'user',
            'content': 'Saya punya ayam dan cabe. Sebutkan bahan yang saya miliki.'
        }
    ]
)

print(response['message']['content'])