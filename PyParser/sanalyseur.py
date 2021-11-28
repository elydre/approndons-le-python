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
        if ligne[0] == "for":
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
                            "var": ligne[1],
                            "minimum": minimum,
                            "maximum": maximum,
                            "pas": pas}
            else:
                self.exit = {"type": "for-list",
                            "var": ligne[1],
                            "list": ligne[3].strip()[0:-1]}