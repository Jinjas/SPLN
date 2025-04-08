import re
import random
from unidecode import unidecode

t = [l.split(' :: ') for l in open('nomes.txt').read().split('\n')]
nomes = [e[0] for e in t]
normalized_nomes = [unidecode(nome).lower() for nome in nomes]
emails = [e[1] for e in t]

def adivinha(nomes,email):
    heuristics= [
        rf'^{email}',
        rf'{email}$'
    ]
    for heur in heuristics:
        for n in nomes:
            if re.match(heur, n, re.IGNORECASE):
                print(n)
    matches = []

for email in emails:
    print(email,":->>>",adivinha(nomes,email))