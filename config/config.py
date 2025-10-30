import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Settings
DEFAULT_MODEL = "llama3-8b-8192"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


