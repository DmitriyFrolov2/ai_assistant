from client.llm_client import LLMClient
from client.embed_client import EmbedClient
from rag.scanner import scan_python_files
from rag.chunker import chunk_text
from rag.index import VectorIndex
from rag.retriever import retrieve
from config import *

# Защита от слишком длинных чанков
MAX_CHARS = 3000  # безопасный предел для embeddings

# 1. Сканируем проект
files = scan_python_files(PROJECT_PATH)

# 2. Индексируем
embedder = EmbedClient()
index = VectorIndex()

for path, content in files.items():
    chunks = chunk_text(content, CHUNK_SIZE, CHUNK_OVERLAP)
    for chunk in chunks:
        if len(chunk) > MAX_CHARS:
            continue  # пропускаем слишком большие чанки
        vec = embedder.embed(chunk)
        index.add(vec, f"FILE: {path}\n{chunk}")

# 3. Формируем запрос
query = "Проанализируй архитектуру и качество Python проекта"
query_vec = embedder.embed(query)
context = retrieve(query_vec, index, TOP_K)

embedder.close()

# 4. Запрос в LLM
with open("prompts/system.txt", encoding="utf-8") as f:
    system = f.read()

with open("prompts/report.txt", encoding="utf-8") as f:
    task = f.read()

llm = LLMClient()
answer = llm.ask(
    system,
    task + "\n\nКОНТЕКСТ ПРОЕКТА:\n" + "\n\n".join(context)
)
llm.close()

# 5. Сохраняем отчёт
with open("reports/report.md", "w", encoding="utf-8") as f:
    f.write(answer)

print("Отчёт сгенерирован: reports/report.md")