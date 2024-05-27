from openai import OpenAI


import os
from dotenv import load_dotenv
load_dotenv()

#this is all that we can securely referency our api key 



openai_client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

prompt = "your name is {Ali} you are a sales agent that sells cheese"
formated_system_promt = {"role":"system", "content": prompt}
messages = []
messages.append(formated_system_promt)

response = openai_client.chat.completions.create(
    model="gpt-4o",
    temperature = 0,
    max_tokens = 100,
    messages = messages,
)

print(response.choices[0].message.content)

