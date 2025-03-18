import re
import shelve
import requests
from bs4 import BeautifulSoup as bs
d = shelve.open("pagecashe.db")

def myget(url):
    if url not in d:
        d[url] = requests.get(url).text    
    return d[url]

d_pt_cn=[]

def proc_filho(txt,cat):
    dtf = bs(txt, 'lxml')
    for tab in dtf.find_all("table",class_="mytable2"):
        for tr in dtf.find_all("tr"):
            print(tr)
            filhos = tr.find_all("td")
            if len(filhos) == 3:
                pt,py,cn = filhos
                d_pt_cn.append({"pt":pt.text,"py":py.text,"cn":cn.text,"dom":cat})

def main():
    url = "https://www.jonsay.co.uk/dictionary.php?langa=Portuguese&langb=Chinese"
    txt = myget(url)
    dt = bs(txt,'lxml')

    n=1
    for link in dt.find_all("a",class_="nav"):
        cat = link.text
        txt2 = myget(link["href"])
        proc_filho(txt2,cat)
        n += 1
        if n == 4 : break
    d.close()

main()

print(d_pt_cn)