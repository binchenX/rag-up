import os


# base model config
MODEL_NAME = os.getenv("BASE_MODEL", "gemma:2b")
MODE_URL = os.getenv("MODEL_URL", "http://localhost:11434")

# define init index
INIT_INDEX = os.getenv('INIT_INDEX', 'false').lower() == 'true'

# vectordb index persist directory
INDEX_PERSIST_DIRECTORY = os.getenv('INDEX_PERSIST_DIRECTORY', "./data/chromadb")

# Embedding Model
EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL","all-MiniLM-L6-v2")

# External data source: target url to scrape
EXTERNAL_DATA_URL =  os.getenv('EXTERNAL_DATA_URL', "https://open5gs.org/open5gs/docs/")

# Chat http api port
HTTP_PORT = os.getenv('HTTP_PORT', 7654)

# mongodb config host, username, password
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USER = os.getenv('MONGO_USER', 'testuser')
MONGO_PASS = os.getenv('MONGO_PASS', 'testpass')
