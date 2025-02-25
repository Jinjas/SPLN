import sys
import re
from collections import Counter
import jjcli

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def pretty_print(freq,relative_freq,opt):
    if("-a" in opt):
        for word,count in freq.most_common():
            print(f"{word}      {count}")
    else:
        for word,count in relative_freq.most_common():
            print(f"{word:.2f}      {count}")

def ratio(relative_freq1,relative_freq2):
    result = {}
    r2 = dict(relative_freq2)
    for word, count in relative_freq1:
        result.update(word,count,r2.get(word,1/1000000))
    return result

def counter(tokens):
    total_tokens = sum(tokens.values())
    return {word: (count, count / total_tokens*1000000) for word, count in tokens.items()} if total_tokens > 0 else {}

def main():
    """Options:
        -a absolute frequency
        -m 700: top 700 words
        -j:sjon output
    """
    cl =jjcli.clfilter("am:",doc=main.__doc__)
    tokens=[]

    for txt in cl.text():
        t=lexer(txt)
        tokens.extend(t)
    c=Counter(tokens)
    relative_frequencies = counter(c)
    pretty_print(c,relative_frequencies,cl)

if __name__ == "__main__":
    main()