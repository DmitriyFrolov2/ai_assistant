from pathlib import Path


def scan_python_files(root: Path) -> dict[str, str]:
    files = {}

    for path in root.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        try:
            files[str(path)] = path.read_text(encoding="utf-8")
        except Exception:
            continue

    return files
