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
            for debut in range(start_pos,len(string)):
                for fin in range(debut, len(string)+1):
                    if string[debut:fin] == m[1]:
                        end_pos = debut
            if start_pos != None and end_pos != None:
                return string[start_pos:end_pos]
            else:
                return None


print(banana("for x in range(1,2,3):", "for |?| in range(|!|):"))
print(banana("for x in range(1,2,3):", "for |!| in range(|?|):"))


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