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