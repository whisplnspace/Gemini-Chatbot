import os
import json
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Set up the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the config file
config_file_path = os.path.join(working_directory, "config.json")

# Load the API key from the config file with error handling
try:
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)
        GOOGLE_API_KEY = config_data.get("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is missing in the config file.")
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading config file: {e}")
    raise
except ValueError as ve:
    print(ve)
    raise

# Print the API key (for debugging purposes, you might want to remove this in production)
print(GOOGLE_API_KEY)

# Configure google.generativeai with the API key
genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_pro_model():
    try:
        gemini_pro_model = genai.GenerativeModel("gemini.pro")
        return gemini_pro_model
    except Exception as e:
        print(f"Error loading Gemini Pro model: {e}")
        raise
