from pathlib import Path

PROJECT_PATH = Path(r"E:\Python\performance-tests")
OLLAMA_CHAT_URL = "http://localhost:11434/v1/chat/completions"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"

CHAT_MODEL = "qwen2.5:7b-instruct"
EMBED_MODEL = "nomic-embed-text"

CHUNK_SIZE = 200
CHUNK_OVERLAP = 40
TOP_K = 8
