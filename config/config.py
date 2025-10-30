import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Settings
DEFAULT_MODEL = "mixtral-8x7b"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
