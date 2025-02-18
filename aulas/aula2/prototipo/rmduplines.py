#!/usr/bin/env python3


from jjcli import * 
'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    - s keep spaces 
    - e remove empty lines 
    - p comentar as linhas que seriam removidas

'''

def remove_linhas_repetidas(cl): 
    linhas_vistas = list()
   
    for linha in cl.input():
        if "-s" in cl.opt:
            ln = linha 
        else:
            ln = linha.strip()

        #a linha pode ser vazia, com conteudo novo, com conteudo repetido
        if "-p" in cl.opt and (ln == "" or ln in linhas_vistas):
            print("##",ln)
            linhas_vistas.append("##" + ln)
        
        elif not ln or ln not in linhas_vistas:
            if "-e" in cl.opt and ln !="":
                print(ln)
                linhas_vistas.append(ln)
            elif "-e" not in cl.opt:
                print(ln)
                linhas_vistas.append(ln)
        

def main (): 
    cl = clfilter(opt="sep", man=__doc__)
    remove_linhas_repetidas(cl)

if __name__ == '__main__': 
    main()