import textacy
import sys
from collections import Counter
from textacy import preprocessing, extract, text_stats as ts

text = open(sys.argv[1],"r",encoding="utf-8").read()
doc = textacy.make_spacy_doc(text,lang="pt_core_news_lg")

# extrair campos nominais com um counter
#nominais = [x.text for x in extract.noun_chunks(doc)] 
#n = Counter(nominais)
#print(n.most_common())

# extrair keyterms
#keywords = extract.keyterms.sgrank(doc,topn=20)
#print(list(keywords))

# extrair triplos
#triplos = extract.subject_verb_object_triples(doc)
#print(list(triplos))

print(ts.readability.flesch_kincaid_grade_level(doc))
print(ts.diversity.ttr(doc))
print(list(extract.kwic.keyword_in_context(doc,"Angola")))

