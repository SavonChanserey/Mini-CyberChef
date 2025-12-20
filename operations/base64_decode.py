import base64

NAME = "From Base64"

def run(data: str) -> str:
    cleaned = data.replace(" ", "").replace("\n", "")
    return base64.b64decode(cleaned).decode("utf-8", errors="replace")