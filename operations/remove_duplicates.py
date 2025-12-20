NAME = "Remove Duplicate Lines"

def run(data: str) -> str:
    lines = data.splitlines()
    return "\n".join(sorted(set(lines), key=lines.index))  # preserves order