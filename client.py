from google import genai

from cred import gemini_api_key

# Creating client for the model usage using api key
client = genai.Client(api_key = gemini_api_key)