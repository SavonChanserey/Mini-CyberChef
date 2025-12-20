import re

NAME = "Extract URLs"

def run(data: str) -> str:
    urls = re.findall(r'https?://[^\s]+', data)
    return '\n'.join(urls) if urls else "[No URLs found]"
