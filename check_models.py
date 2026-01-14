import os
from google import genai
try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    print("API key accepted. Available models:\n")
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print("Connection failed:", e)