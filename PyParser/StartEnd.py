def counting(space_in_tabs, l):
    t = 0
    while l.startswith(" "*t): t += space_in_tabs
    return(int((t - space_in_tabs)/space_in_tabs))

def compare(old, i, space_in_tabs = 4):
    new = counting(space_in_tabs, i)
    if new > old:
        return new, "+"
    elif new < old:
        return new, "-"
    else:
        return new, "="