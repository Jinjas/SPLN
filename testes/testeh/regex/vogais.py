import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def vogais_ordenadas(palavras):
    vogais = 'aeiou'

    resultado ={
        palavra: ''.join([remover_acentos(letra) for letra in palavra.lower() if remover_acentos(letra) in vogais]) for palavra in palavras
    }

    for palavra in sorted(resultado,key=lambda x:resultado[x]):
        print(f"{palavra}: {resultado[palavra]}")

words = ['atribuição', 'unidirecional', 'Alunos', 'Área', 'café', 'esdrúxula']
vogais_ordenadas(words)