import os
from dotenv import load_dotenv
from google import genai
# Load variables from .env
load_dotenv()

# Create genai client
client =  genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Send request to the model
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="EXPLAIN AI IN SIMPLE TERMS."
)

# Display the response
print(response.text)





