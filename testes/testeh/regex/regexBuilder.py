
def create(nomeCompleto):

    nomes = nomeCompleto.split(' ')

    regex = f"\\b{nomes[0][0]}(\\.|{nomes[0][1:]})\\s+"
    for nome in nomes[1:-1]:
        regex+= f"({nome[0]}(\\.|{nome[1:]})\\s+)?"

    regex += f"{nomes[-1]}\\b"
    print(regex)



nomeCompleto = input()

create(nomeCompleto)

