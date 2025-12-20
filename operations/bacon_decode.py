REV_BACON = {v:k for k,v in {'A':'AAAAA','B':'AAAAB','C':'AAABA','D':'AAABB','E':'AABAA','F':'AABAB','G':'AABBA','H':'AABBB',
                            'I':'ABAAA','J':'ABAAB','K':'ABABA','L':'ABABB','M':'ABBAA','N':'ABBAB','O':'ABBBA','P':'ABBBB',
                            'Q':'BAAAA','R':'BAAAB','S':'BAABA','T':'BAABB','U':'BABAA','V':'BABAB','W':'BABBA','X':'BABBB',
                            'Y':'BBAAA','Z':'BBAAB'}.items()}

NAME = "From Bacon"

def run(data: str) -> str:
    data = "".join(c for c in data.upper() if c in "AB")
    return "".join(REV_BACON.get(data[i:i+5], "?") for i in range(0, len(data), 5))