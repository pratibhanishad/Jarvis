from g4f.client import Client

def llm2(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        web_search=False
    )
    x = response.choices[0].message.content
    return x

# while True:
#     x=llm2(text=input())
#     print(x)