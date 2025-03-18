import re 
import requests
import shelve 
from bs4 import BeautifulSoup as bs
import jjcli

d = shelve.open("pagecache.db")

def myget(url):
    if url not in d:
        txt = requests.get(url).text
        d[url] = txt
    return d[url] 


def main():
    cl = jjcli.clfilter("s:")
    sep = cl.opt.get("-s", "::")

    for url in cl.args:
        txt = myget(url)
        dt = bs(txt, 'lxml')
        n=0
        for tab in dt.find_all('table'):
            n=1
            csv = ""
            for tr in tab.find_all("tr"):
                filhos = [re.sub("\s+", " ", f.text) for f in tr.find_all("td")]
                csv += sep.join(filhos) + "\n"
            print(f"==>{url}//{n}\n{csv}")
main()

d.close()