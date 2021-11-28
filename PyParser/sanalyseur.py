'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

version = "0.1.3"

class line:
    def __init__(self, inp: str):
        self.brut = inp
        self.exit = None

    def __str__(self):
        return str(self.exit)
    
    def analyse(self):
        # parser python
        ligne = self.brut.split(" ")
        match ligne:
            case "for", var, "in", end:
                if "range" in ligne[3]:
                    args = [x.strip() for x in "".join(ligne[3:]).replace("range", "").strip()[1:-2].split(",")]
                    if len(args) == 1:
                        minimum = 0
                        maximum = int(args[0])
                        pas     = 1
                    elif len(args) == 2:
                        minimum = int(args[0])
                        maximum = int(args[1])
                        pas     = 1
                    elif len(args) == 3:
                        minimum = int(args[0])
                        maximum = int(args[1])
                        pas     = int(args[2])
                    self.exit = {"type": "for-range",
                                "var": var,
                                "minimum": minimum,
                                "maximum": maximum,
                                "pas": pas}