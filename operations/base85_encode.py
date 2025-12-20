import base64

NAME = "To Base85"

def run(data: str) -> str:
    data = data.strip().removeprefix("<~").removesuffix("~>")
    return base64.a85encode(data.encode()).decode()
    