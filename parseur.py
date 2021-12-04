from PyParser.analyseur import line
from PyParser.StartEnd import compare, counting


def parser(code: str):
    old_tabs = 0
    sortie = []
    
    for i in code.split('\n'):
        i.replace('\t', '    ')
        if i.strip() == "":
            continue
        latest = i
        old_tabs, tab_chang = compare(old_tabs, i, 4)
        par = line(tab_chang, i.strip())
        for e in par.make():
            sortie.append(e)
    for _ in range(counting(4, latest)):
        sortie.append({"type": "opening"})
    return sortie