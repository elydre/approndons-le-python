from PyParser.analyseur import line
from PyParser.StartEnd import compare


def parser(code: str):
    old_tabs = 0
    for i in code.split('\n'):
        if i.strip() == "":
            continue
        i.replace('\t', '    ')
        old_tabs, tab_chang = compare(old_tabs, i, 4)

        test = line(tab_chang, i.strip())
        test.chek_tab()
        test.analyse()
        test.segmenter()
        for ex in test.exit:
            print(ex)