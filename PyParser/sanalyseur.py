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

def banana(string, model):
    """
    string:   if 1 == 3:
    model:    if |?| == |!|:
    return    1
    """
    model = model.split("|!|")
    for m in model:
        if "|?|" in m:
            m = m.split("|?|")
            start_pos, end_pos = None, None
            for debut in range(len(string)):
                for fin in range(debut, len(string)+1):
                    if string[debut:fin] == m[0]:
                        start_pos = fin
                        break
            if start_pos != None:
                for debut in range(start_pos,len(string)):
                    for fin in range(debut, len(string)+1):
                        if string[debut:fin] == m[1]:
                            end_pos = debut
                            break
                if end_pos != None:
                    return string[start_pos:end_pos]


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
        if ligne[0] == "for":
            var = banana(ligne_brut, "for |?| in |!|")
            if "range" in banana(ligne_brut, "for |!| in |?|"):
                args = banana(ligne_brut, "for |!| in range(|?|):")
                args = [arg.strip() for arg in args.split(",")]
                if len(args) == 1:
                    mini, maxi, pas = 0, args[0], 1
                elif len(args) == 2:
                    mini, maxi, pas = args[0], args[1], 1
                elif len(args) == 3:
                    mini, maxi, pas = args[0], args[1], args[2]
                self.exit = {"type": "for-range", "var": var, "min": mini, "max": maxi, "pas": pas}
        if ligne[0] == "if":
            if "==" in ligne_brut:
                comparateur = "=="
            elif "!=" in ligne_brut:
                comparateur = "!="
            elif "<=" in ligne_brut:
                comparateur = "<="
            elif ">=" in ligne_brut:
                comparateur = ">="
            elif "<" in ligne_brut:
                comparateur = "<"
            elif ">" in ligne_brut:
                comparateur = ">"

            var1 = banana(ligne_brut, f"if |?| {comparateur} |!|:")
            var2 = banana(ligne_brut, f"if |!| {comparateur} |?|:")
            self.exit = {"type": "if-less-equal", "var1": var1, "var2": var2, "comparateur": comparateur}