import os

from dotenv import load_dotenv

# Loading API key from enviroment variable
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

# raising error if not found an api key
if not gemini_api_key:
    raise EnvironmentError("Gemini api key is not found!")
