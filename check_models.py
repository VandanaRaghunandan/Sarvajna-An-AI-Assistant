import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # load your .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
models = genai.list_models()
for m in models:
    print(m.name)  # just print the model name
