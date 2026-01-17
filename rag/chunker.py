

def chunk_text(text: str, max_lines: int, overlap: int) -> list[str]:
    lines = text.splitlines()
    chunks = []

    i = 0
    while i < len(lines):
        chunk = lines[i:i + max_lines]
        chunks.append("\n".join(chunk))
        i += max_lines - overlap

    return chunks
