from g4f.client import Client

def llm2(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, an AI bot who always responds respectfully and says 'sir' while replying."},
            {"role": "user", "content": text}
        ],
    )
    x = response.choices[0].message.content
    return x
