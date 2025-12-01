NAME = "From Binary"
def run(data: str) -> str:
    try:
        return "".join(chr(int(b, 2)) for b in data.replace("\n"," ").split() if b)
    except:
        return "[Invalid Binary]"