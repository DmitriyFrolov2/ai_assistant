import httpx

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "qwen2.5:7b-instruct"


class LLMClient:
    def __init__(self, timeout: float = 60.0):
        self.client = httpx.Client(timeout=timeout)

    def ask(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False,
                "temperature": 0.2,
                "top_p": 0.9
            }
        )
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    def close(self):
        self.client.close()
