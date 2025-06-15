import requests
from bs4 import BeautifulSoup
import json

def get_modalidade_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    modalidades = []

    #encontar o primeiro table com classe identificada
    table = soup.find('table',class_='modalities-table')
    rows = table.find_all('tr')[1:] #para ignorar o cabeçalho e encontrar todos os tr

    for row in rows:
        cols = row.find_all('td')
        
        #ex de cols neste caso
        #<td>120 minutos</td>
        #<td> <a href="https://www.ginasio.pt/modalidades/ciclismo"> Ciclismo </a> </td>
        #<td>Fácil</td>
        if len(cols) == 3:
            link_tag = cols[1].find('a')
            modalidade_nome = link_tag.text
            modalidade_link = link_tag['href']
            dificuldade = cols[2].text
            modalidades.append({
                        'nome' : modalidade_nome,
                        'link' : modalidade_link, 
                        'dificuldade' : dificuldade})

    return modalidades

def get_detalhes_modalidade(modalidade):
    r=requests.get(modalidade['link'])
    soup = BeautifulSoup(r.text,'html.parser')
    instrutor = ''
    horarios = []
    detalhes = soup.find('ul',class_='sport-details')
    detalhe = detalhes.find_all('li')
    ultimo = detalhe[1]
    instrutor = ultimo.text.replace('instrutor=','')
    
    table=soup.find('table',class_='schedule-table')
    rows = table.find_all('tr')[1:] #skip cabeçalho
    for row in rows:
        cols = row.find_all('td')
        if len(cols) ==2 :
            horarios.append(cols[1].text)
    return{
        'dificuldade':modalidade['dificuldade'],
        'instrutor': instrutor,
        'horarios': horarios
    }


def main():
    base_url = 'https://www.ginasio.pt/modalidades'
    modalidades = get_modalidade_list(base_url)
    resultado = {}
    for m in modalidades:
        d = get_detalhes_modalidade(m)
        resultado[m['nome']] = d
    
    with open('modalidades.json','w',encoding='utf-8') as f:
        json.dump(resultado,f,ensure_asci = False, indent=4)
    

if __name__ == '__main__':
    main()