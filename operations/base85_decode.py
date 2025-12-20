import base64

NAME = "From Base85"

def run(data: str) -> str:
    data = data.strip().removeprefix("<~").removesuffix("~>")
    return base64.a85decode(data).decode("utf-8", errors="replace")
