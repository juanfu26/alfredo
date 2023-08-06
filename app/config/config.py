import os

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Folder with personal data to query about
DATA_FOLDER = os.getenv("DATA_FOLDER", "./data")

# Enable to save to disk & reuse the model (for repeated queries on the same data)
VECTORSTORE_PERSIST = os.getenv("VECTORSTORE_PERSIST", True)
VECTORSTORE_FOLDER = os.getenv("VECTORSTORE_FOLDER", "./persist") 

LOGGING_CONFIG_FILE = os.getenv("LOGGING_CONFIG_FILE", "./app/logging.yml") 
