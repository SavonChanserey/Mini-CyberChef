import re

NAME = "Extract IPs"

def run(data: str) -> str:
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    return '\n'.join(ips) if ips else "[No IPs found]"