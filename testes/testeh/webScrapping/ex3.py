import requests
from bs4 import BeautifulSoup
import json

def get_cursos_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    uCs = []

    #encontar o primeiro table
    table = soup.find('table')
    rows = table.find_all('tr')[1:] #para ignorar o cabeçalho e encontrar todos os tr

    for row in rows:
        cols = row.find_all('td')

        if len(cols) == 3:
            link_tag = cols[1].find('a')
            curso_nome = link_tag.text
            curso_link = link_tag['href']
            uCs.append({
                        'nome' : curso_nome,
                        'link' : curso_link})
    return uCs

def get_detalhes_curso(curso):

    r=requests.get(curso['link'])
    soup = BeautifulSoup(r.text,'html.parser')

    desc_class = soup.find('div', class_='uc_descricao')
    descr = desc_class.find('p')
    descricao = descr.text

    return descricao

def main():
    base_url = 'https://www.uminho.pt/cursos/lei/ucs'
    cursos = get_cursos_list(base_url)
    resultado = {}
    for c in cursos:
        des = get_detalhes_curso(c)
        resultado[c['nome']] = des
    
    with open('modalidades.json','w',encoding='utf-8') as f:
        json.dump(resultado,f,ensure_asci = False, indent=4)

if __name__ == '__main__':
    main()