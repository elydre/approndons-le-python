from PyParser.segmenteur import launch_segmenter as segmenter

inp = """
for x in range(0, 10):
    print("cc" + str(x))
"""


print(segmenter(inp))