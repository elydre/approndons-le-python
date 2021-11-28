# PY - PARSER

py-parser est un parser de code python en python encore en plien dévlopement.

## analyseur

```py	
from PyParser.analyseur import line

test = line("if 1 == 1:")
test.analyse()

test.print()
```

## segmenteur

```py
from PyParser.segmenteur import launch_segmenter
launch_segmenter(code: str) -> list
```