import spacy

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")

documento = "O João Manuel da Silva nasceu em Tebosa em Fevereiro de 1901. Imigrou para a cidade de S.Paulo no Brasil"

ad = nlp(documento)

for frase in ad.sents:
    print(frase)
    for ent in frase.ents:
        print(ent,ent.label_)

    for token in frase:
        print("Token:", token.text,token.lemma_,token.pos_,token.ent_type_)