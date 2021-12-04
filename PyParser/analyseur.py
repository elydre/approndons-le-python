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

def launch_segmenter(dico):
    for k in dico.keys():
        if k.startswith("§"):
            if k.startswith("§§"):
                for i in range(len(dico[k])):
                    dico[k][i] = segmenter(dico[k][i])
            else:
                dico[k] = segmenter(dico[k])
        elif k.startswith("$"):
            dico[k] = launch_segmenter(dico[k])
    return dico

class line:
    def __init__(self, tab_chang: str, inp: str):
        self.brut = inp
        self.tab_chang = tab_chang
        self.exit = []

    def print(self):
        print(self.brut.strip())
        for ex in self.exit:
            print(" -",ex["type"].upper(),"-")
            for k in ex.keys():
                if k != "type":
                    print(" ",k, ":", ex[k])
            print("")

    def segmenter(self):
        for i in range(len(self.exit)):
            self.exit[i] = launch_segmenter(self.exit[i])
    
    def chek_tab(self):
        if self.tab_chang == "-":
            self.exit.append({"type": "end"})

    def analyse(self) -> dict:
        # parser python
        ligne = self.brut.split(" ")
        ligne_brut = self.brut
        if ligne[0].startswith("for"):
            self.exit.append(al.forA(ligne_brut))

        elif ligne[0].startswith("if"):
            self.exit.append(al.ifA(ligne_brut))

        elif ligne[0].startswith("elif"):
            self.exit.append(al.elifA(ligne_brut))

        elif ligne[0].startswith("else"):
            self.exit.append(al.elseA(ligne_brut))
        
        elif ligne[0].startswith("while"):
            self.exit.append(al.whileA(ligne_brut))
        
        elif ligne[0].startswith("return"):
            self.exit.append(al.returnA(ligne_brut))

        elif ligne[0].startswith("break"):
            self.exit.append(al.breakA(ligne_brut))
        
        elif ligne[0].startswith("pass"):
            self.exit.append(al.passA(ligne_brut))
        
        elif ligne[0].startswith("continue"):
            self.exit.append(al.continueA(ligne_brut))

        elif ligne[0].startswith("print"):
            self.exit.append(al.printA(ligne_brut))
        
        elif ligne[0].startswith("import"):
            self.exit.append(al.importA(ligne_brut))