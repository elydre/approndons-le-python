from PyParser.analyseur import line


i = "if len('coucou') == len('poules'):"


test = line(i)
test.analyse()

test.print()

test.segmenter("var1")
test.segmenter("var2")

test.print()