from PyParser.segmenteur import launch_segmenter as segmenter
from PyParser.sanalyseur import line

inp = "for x in range(10):"

test = line(inp)

test.analyse()

print(test)