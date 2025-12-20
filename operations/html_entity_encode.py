import html

NAME = "To HTML Entity"

def run(data: str) -> str:
    return html.escape(data)