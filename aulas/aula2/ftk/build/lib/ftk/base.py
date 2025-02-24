import re
import jjcli

def lexer(txt):
    return re.findall(r'\w+(-\w+)*|[\W\s]+',txt)

def main():
    cl= jjcli.clfilter()
    for txt in cl.text():
        print(lexer(txt))

    
