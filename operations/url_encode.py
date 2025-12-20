import urllib.parse

NAME = "URL Encode"

def run(data: str) -> str:
    return urllib.parse.quote(data)