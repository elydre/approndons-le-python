from PyParser.analyseur import line

i = "if len('coucou') == 5: print('coucou')"

test = line(i)
test.analyse()

print(test.exit)
test.segmenter()
print(test.exit)