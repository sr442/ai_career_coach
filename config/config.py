import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Settings
DEFAULT_MODEL = "llama-3.1-8b-instant"


EMBEDDING_MODEL = "all-MiniLM-L6-v2"



