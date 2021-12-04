from PyParser.tools import banana

def find_comparateur(ligne):
    for c in ["==", "!=", ">", "<", ">=", "<="]:
        if c in ligne: return c

def forA(ligne):
    var = banana(ligne, "for |?| in |!|")
    if "range" in ligne:
        args = banana(ligne, "for |!| in range(|?|):")
        args = [arg.strip() for arg in args.split(",")]
        if len(args) == 1:
            mini, maxi, pas = 0, args[0], 1
        elif len(args) == 2:
            mini, maxi, pas = args[0], args[1], 1
        elif len(args) == 3:
            mini, maxi, pas = args[0], args[1], args[2]
        return {"type": "for-range", "§var": var, "min": mini, "max": maxi, "pas": pas}
    else:
        var = banana(ligne, "for |?| in |!|:")
        liste = banana(ligne, "for |!| in |?|:")
        return {"type": "for-list", "§var": var, "§liste": liste}

def ifA(ligne):
    comparateur = find_comparateur(ligne)
    var1 = banana(ligne, f"if |?| {comparateur} |!|:")
    var2 = banana(ligne, f"if |!| {comparateur} |?|:")
    return {"type": "if", "§var1": var1, "§var2": var2, "comparateur": comparateur}

def elifA(ligne):
    comparateur = find_comparateur(ligne)
    var1 = banana(ligne, f"elif |?| {comparateur} |!|:")
    var2 = banana(ligne, f"elif |!| {comparateur} |?|:")
    return {"type": "elif", "§var1": var1, "§var2": var2, "comparateur": comparateur}

def elseA(ligne):
    return {"type": "else"}

def whileA(ligne):
    comparateur = find_comparateur(ligne)
    var1 = banana(ligne, f"while |?| {comparateur} |!|:")
    var2 = banana(ligne, f"while |!| {comparateur} |?|:")
    return {"type": "while", "§var1": var1, "§var2": var2, "comparateur": comparateur}

def returnA(ligne):
    var = ligne.replace("return", "").strip()
    return {"type": "return", "§var": var}

def breakA(ligne):
    return {"type": "break"}

def passA(ligne):
    return {"type": "pass"}

def importA(ligne):
    element = [e.strip() for e in "".join(banana(ligne, "import |?|").strip()[1:-1]).split(" ")]
    return {"type": "import", "§element": element}

def continueA(ligne):
    return {"type": "continue"}

def printA(ligne):
    element = [e.strip() for e in "".join(banana(ligne, "print|?|").strip()[1:-1]).split(",")]
    return {"type": "print", "§element": element}