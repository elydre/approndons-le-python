from tools import banana

def forA(ligne):
    var = banana(ligne, "for |?| in |!|")
    if "range" in banana(ligne, "for |!| in |?|"):
        args = banana(ligne, "for |!| in range(|?|):")
        args = [arg.strip() for arg in args.split(",")]
        if len(args) == 1:
            mini, maxi, pas = 0, args[0], 1
        elif len(args) == 2:
            mini, maxi, pas = args[0], args[1], 1
        elif len(args) == 3:
            mini, maxi, pas = args[0], args[1], args[2]
        return {"type": "for-range", "var": var, "min": mini, "max": maxi, "pas": pas}

def ifA(ligne):
    if "==" in ligne:
        comparateur = "=="
    elif "!=" in ligne:
        comparateur = "!="
    elif "<=" in ligne:
        comparateur = "<="
    elif ">=" in ligne:
        comparateur = ">="
    elif "<" in ligne:
        comparateur = "<"
    elif ">" in ligne:
        comparateur = ">"

    var1 = banana(ligne, f"if |?| {comparateur} |!|:")
    var2 = banana(ligne, f"if |!| {comparateur} |?|:")
    return {"type": "if", "var1": var1, "var2": var2, "comparateur": comparateur}

def elifA(ligne):
    if "==" in ligne:
        comparateur = "=="
    elif "!=" in ligne:
        comparateur = "!="
    elif "<=" in ligne:
        comparateur = "<="
    elif ">=" in ligne:
        comparateur = ">="
    elif "<" in ligne:
        comparateur = "<"
    elif ">" in ligne:
        comparateur = ">"

    var1 = banana(ligne, f"elif |?| {comparateur} |!|:")
    var2 = banana(ligne, f"elif |!| {comparateur} |?|:")
    return {"type": "elif", "var1": var1, "var2": var2, "comparateur": comparateur}