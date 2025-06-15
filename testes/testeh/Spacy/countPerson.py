#Crie um programa em Python que, dado o texto de um livro como input, calcula o número de ocorrências das personagens desse livro

import sys
import spacy
from collections import Counter

npl = spacy.load('en_core_web_lg')


def extrairPersonagens(book):  
    with open(book, 'r',encoding="utf-8") as f:
        text = f.read()

    personagens=[]

    doc = npl(text)
    for ent in doc.ents:
        if ent.label_== 'PERSON':
            personagens.append(ent.text)
    return personagens
def main():
    book = sys.argv[1]
    persons = extrairPersonagens(book)
    
    top_enti = Counter(persons)

    for nome, freq in sorted(top_enti.items(), key=lambda x: x[1], reverse=True):
        if freq > 2:
            print(f"{nome}: {freq}")

main()
