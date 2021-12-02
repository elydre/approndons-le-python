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

import PyParser.analyseur_line as al
from PyParser.segmenteur import launch_segmenter as segmenter

version = "0.1.4"


class line:
    def __init__(self, inp: str):
        self.brut = inp
        self.exit = None

    def print(self):
        print(self.brut.strip())
        print(" -",self.exit["type"].upper(),"-")
        for k in self.exit.keys():
            if k != "type":
                print(" ",k, ":", self.exit[k])
        print("")

    def segmenter(self, element: str):
        self.exit[element] = segmenter(self.exit[element])
    
    def analyse(self) -> dict:
        # parser python
        ligne = self.brut.split(" ")
        ligne_brut = self.brut
        if ligne[0].startswith("for"):
            self.exit = al.forA(ligne_brut)

        elif ligne[0].startswith("if"):
            self.exit = al.ifA(ligne_brut)

        elif ligne[0].startswith("elif"):
            self.exit = al.elifA(ligne_brut)

        elif ligne[0].startswith("else"):
            self.exit = al.elseA(ligne_brut)
        
        elif ligne[0].startswith("while"):
            self.exit = al.whileA(ligne_brut)
        
        elif ligne[0].startswith("return"):
            self.exit = al.returnA(ligne_brut)

        elif ligne[0].startswith("break"):
            self.exit = al.breakA(ligne_brut)
        
        elif ligne[0].startswith("pass"):
            self.exit = al.passA(ligne_brut)
        
        elif ligne[0].startswith("continue"):
            self.exit = al.continueA(ligne_brut)

        elif ligne[0].startswith("print"):
            self.exit = al.printA(ligne_brut)
        
        elif ligne[0].startswith("import"):
            self.exit = al.importA(ligne_brut)