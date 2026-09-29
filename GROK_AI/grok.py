import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Create the xAI client 
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

# Send request to the model
response = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {"role": "user", "content": "EXPLAIN AI IN SIMPLE TERMS."}
    ]
)

# Display the response
print(response.choices[0].message.content)