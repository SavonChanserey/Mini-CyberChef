import urllib.parse

NAME = "URL Decode"

def run(data: str) -> str:
    
    try:
        # Handles %20, %3A, etc. → normal characters
        return urllib.parse.unquote(data)
    except Exception as e:
        return f"[URL Decode Error] {e}"