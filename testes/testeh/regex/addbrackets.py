import re

texto = """O José João Dias Almeida é fixe mas o J. J. Almeida ainda é melhor... já o J. F. Almeida nem tanto"""

regex = r"\bJ(\.|osé)\s+(J(\.|oão)\s+)?(D(\.|ias)\s+)?Almeida\b"


def substituir(s):
    return f"({s.group(0)})"

print(re.sub(regex,substituir,texto))
