import spacy
import jjcli
import re
from collections import Counter

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")

cli = jjcli.clfilter()
ocorrencias = Counter()


def entities(txt):
    ad = nlp(txt)
    for frase in ad.sents:
        for ent in frase.ents:
            ocorrencias[(ent.text,ent.label_)]+=1


for txt in cli.text():
    result = re.findall(r'<ScopeContent>(.*?)<\ScopeContent>',txt,re.DOTALL)
    for text in result:
        entities(text)


    print("Ocorrencias de key:",ocorrencias)