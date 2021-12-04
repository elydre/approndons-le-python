from PyParser.analyseur import line

i = "if len('coucou') == 5:"

test = line(i)
test.analyse()
test.segmenter()
print(test.exit)