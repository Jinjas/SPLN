import spacy

# Carrega o modelo grande de português
nlp = spacy.load('pt_core_news_lg')

# Lê os termos
with open("termos.txt", "r", encoding="utf-8") as f:
    termos = [line.strip() for line in f.readlines()]

# Lê as categorias
with open("categorias.txt", "r", encoding="utf-8") as f:
    categorias = [line.strip() for line in f.readlines()]


with open("termos_cat.txt", "w", encoding="utf-8") as f:
    for termo in termos:
        termo_doc = nlp(termo)
        similaridades = []

        for cat in categorias:
            cat_doc = nlp(cat)
            if termo_doc.has_vector:
                #print("vector ", termo_doc.vector)
                if cat_doc.has_vector:
                    sim = termo_doc.similarity(cat_doc)
            else:
                sim = -1
            similaridades.append((cat, sim))

        similaridades_ordenadas = sorted(similaridades, key=lambda x: x[1], reverse=True)

        categorias_proximas = similaridades_ordenadas[:4]


        f.write(f"{termo}@{categorias_proximas[0][0]}#{categorias_proximas[1][0]}\n")
        
        print(f"\nTermo: {termo}")
        print(f"Categorias mais próximas: {categorias_proximas}")