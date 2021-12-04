from PyParser.analyseur import line

i = "if len('coucou') == len('poules') and coucou == True:"

test = line(i)
test.analyse()

print(test.exit)
test.segmenter()
print(test.exit)