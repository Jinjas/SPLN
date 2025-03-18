import re
import shelve
import requests
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

d = shelve.open("pagecashe.db")

def myget(url):
    if url not in d:
        d[url] = requests.get(url).text    
    return d[url]

d_pt_cn=[]


def main():
    url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/27-05-77-80-mil-assassinatos/"
    txt = myget(url)
    dt = bs(txt,'lxml')

    for table in dt.find_all("table"):
        for tr in table.find_all("tr")[3:]:
            td = tr.find_all("td")
            if len(td)>=2:
                href = td[1].a["href"]
                print(href)


main()
d.close()
