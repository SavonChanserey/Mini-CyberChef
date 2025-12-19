import html

NAME = "From HTML Entity"
DESCRIPTION = "Decode HTML entities (&lt; → <)"

def run(data: str) -> str:
    return html.unescape(data)