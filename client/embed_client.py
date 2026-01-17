import httpx
from config import OLLAMA_EMBED_URL, EMBED_MODEL


class EmbedClient:
    def __init__(self):
        self.client = httpx.Client(timeout=30)

    def embed(self, text: str) -> list[float]:
        r = self.client.post(
            OLLAMA_EMBED_URL,
            json={
                "model": EMBED_MODEL,
                "prompt": text
            }
        )
        r.raise_for_status()
        return r.json()["embedding"]

    def close(self):
        self.client.close()
