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
            if start_pos is not None:
                end_pos = string.find(m[1])
                if end_pos is not None:
                    if end_pos < start_pos: end_pos = len(string)
                    return string[start_pos:end_pos]