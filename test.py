from PyParser.segmenteur import launch_segmenter as segmenter
from PyParser.analyseur import line

inp = """
for x in range(20):
for x in range(10,20):
for x in range(10,20,2):
for x in blabla:
if x == 3:
if x != 3:
if x < 3:
elif x > 3:
else:
while x < 3:
return x
break
pass
continue
print("coucou",1)
"""

for i in inp.split("\n"):
    if i != "":  
        test = line(i)
        test.analyse()
        test.print()