from PyParser.analyseur import line
from PyParser.StartEnd import compare


def parser(code: str):
    old_tabs = 0
    for i in code.split('\n'):
        if i.strip() == "":
            continue
        i.replace('\t', '    ')
        old_tabs, tab_chang = compare(old_tabs, i, 4)

        par = line(tab_chang, i.strip())
        par.chek_tab()
        par.analyse()
        par.segmenter()
        for ex in par.exit:
            print(ex)