import re,sys
import spacy
from collections import Counter

stopthings = {}

npl = spacy.load('pt_core_news_lg')

def process_file(padrao,file) :
    with open(file, 'r',encoding="utf-8") as f:
        text = f.read()
    frases_validas = []
    doc = npl(text)
    for sent in doc.sents:
        if re.search(padrao,sent.text,re.IGNORECASE):
            frases_validas.append(sent.text)
    return frases_validas

def extrair(frases):
    verbos = []
    entidades = []
    for f in frases:
        doc = npl(f)
        for token in doc:
            #print(f"text: {token.text}; lemma_: {token.lemma_}; pos_: {token.pos_}; ")
            if token.pos_== 'VERB':
                lemma = token.lemma_
                if lemma not in stopthings:
                    verbos.append(lemma)
        for ent in doc.ents:
            print(f"text: {ent.text} ; label_: {ent.label_}")
            entidades.append(ent.text)
    return verbos, entidades

def main():
    padrao = sys.argv[1]
    files = sys.argv[2:]
    frases = []
    for f in files:
        encontradas = process_file(padrao, f)
        frases.extend(encontradas)
    verbos,entidades = extrair(frases)
    top_verbos = Counter(verbos).most_common(20)
    top_enti = Counter(entidades).most_common(20)

    print("top entidades: ",top_enti,"\ntop verbos: ",top_verbos)

main()