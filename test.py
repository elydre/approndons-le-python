from PyParser.analyseur import line

i = "if len('coucou') == len('poules'):"

test = line(i)
test.analyse()

print(test.exit)
test.segmenter("var1")
print(test.exit)
test.segmenter("var2")
print(test.exit)