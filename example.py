from client.llm_client import LLMClient

with open("prompts/system.txt", encoding="utf-8") as f:
    system_prompt = f.read()

question = """
Объясни разницу между unit, integration и e2e тестами.
Приведи примеры для Python.
"""

llm = LLMClient()
answer = llm.ask(system_prompt, question)
llm.close()

print(answer)
