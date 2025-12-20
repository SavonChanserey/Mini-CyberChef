import html

NAME = "From HTML Entity"

def run(data: str) -> str:
    return html.unescape(data)