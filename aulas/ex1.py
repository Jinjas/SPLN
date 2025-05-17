from gensim.models import Word2Vec

sentences = [['this','is',' the forst ',' sentence',' for ',' word2vec'],
            ['this','is','the second','sentence'],
            ['yet','another','sentence'],
            ['one','more','sentence'],
            ['and','the','final','sentence']]

model = Word2Vec(sentences,vector_size =100, window=5,min_count=1,sg=1,epochs=5,workers=3)

