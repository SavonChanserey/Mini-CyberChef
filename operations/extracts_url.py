import re

NAME = "Extract URLs"

def run(data: str) -> str:
    urls = re.findall(r'https?://[^\s]+', data)
    return '\n'.join(urls) if urls else "[No URLs found]"

# Example input:
# Check out https://example.com and http://google.com/search?q=python
# Also www.github.com and https://x.ai/grok
# No url here, but ftp://old.site is not http(s)
# And example.com without protocol is not extracted