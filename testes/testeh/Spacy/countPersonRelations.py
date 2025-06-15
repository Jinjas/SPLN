import sys
import spacy
from collections import Counter
import json

npl = spacy.load('en_core_web_lg')


def extrairRelacoes(book):  
    with open(book, 'r',encoding="utf-8") as f:
        text = f.read()


    doc = npl(text)
    relacoes = {}


    for sents in doc.sents:
        personagens=[]
        for ent in sents.ents:
            if ent.label_== 'PERSON':
                personagens.append(ent.text)
        
        personagensSorted = sorted(personagens)
        n = len(personagensSorted)
        if  n >=2:
            for i in range(n):
                for j in range(i + 1, n):
                    par = (personagensSorted[i], personagensSorted[j])
                    if par in relacoes:
                        relacoes[par] += 1
                    else:
                        relacoes[par] = 1

    return relacoes

def guardar_em_json(relacoes):
    lista_relacoes = []

    sorted_relacoes = sorted(relacoes.items(), key=lambda x: x[1], reverse=True)
    for par, peso in sorted_relacoes:
        p1, p2 = par
        item = {
            "source": p1,
            "target": p2,
            "weight": peso
        }
        lista_relacoes.append(item)

    with open("./output.json", "w", encoding="utf-8") as f:
        json.dump(lista_relacoes, f, indent=2, ensure_ascii=False)

def main():
    book = sys.argv[1]
    relations = extrairRelacoes(book)
    guardar_em_json(relations)

main()
