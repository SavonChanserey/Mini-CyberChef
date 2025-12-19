import html

NAME = "To HTML Entity"
DESCRIPTION = "Encode to HTML entities (< → &lt;)"

def run(data: str) -> str:
    return html.escape(data)