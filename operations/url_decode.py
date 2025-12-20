import urllib.parse

NAME = "URL Decode"

def run(data: str) -> str:
    try:
        return urllib.parse.unquote(data)
    except Exception as e:
        return f"[URL Decode Error] {e}"