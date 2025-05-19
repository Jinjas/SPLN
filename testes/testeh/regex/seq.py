import re

expr = r"\b[\wç]+(?:,\s+(?:[\wç]+))+\s+e\s+[\wç]+\b"

text="""Portugal, Espanha e França resolveram proibir a pesca durante os meses de Janeiro, Fevereiro, Março e Abril.
Durante esses meses, a Itália e Grécia permitem pesca, arrasto, captura.
"""

grs = re.findall(expr,text)

for gr in grs:
    partes = re.sub(r",\s+|\s+e\s+",'|',gr)
    print(partes)


#re.sub(regEx_To_Match,thing_To_Insert,input)
#re.split(regEx_To_Match,input)
#re.findall(regEx_To_Match,input) todos 