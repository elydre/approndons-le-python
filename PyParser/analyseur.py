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

import analyseur_line as al

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
        ligne_brut = self.brut
        if ligne[0].startswith("for"):
            self.exit = al.forA(ligne_brut)

        if ligne[0].startswith("if"):
            self.exit = al.ifA(ligne_brut)

        if ligne[0].startswith("elif"):
            self.exit = al.elifA(ligne_brut)
            
        if ligne[0].startswith("else"):
            self.exit = {"type": "else"}