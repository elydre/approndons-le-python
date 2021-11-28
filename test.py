from PyParser.segmenteur import launch_segmenter as segmenter
from PyParser.sanalyseur import line

inp = """
for x in range(20):
for x in range(10,20):
for x in range(10,20,2):
"""

for i in inp.split("\n"):
    if i != "":  
        test = line(i)
        test.analyse()
        print(test)