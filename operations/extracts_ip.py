import re

NAME = "Extract IPs"

def run(data: str) -> str:
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    return '\n'.join(ips) if ips else "[No IPs found]"


# Example: Server log example:
# User from 192.168.1.100 accessed /admin
# Suspicious connection from 8.8.8.8 and 256.256.256.256
# Another user: 10.0.0.55 and 172.16.254.1
# Invalid ones like 999.999.999.999 or 1.2.3.999 should be skipped
# Also 0.0.0.0 is valid