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
            start_pos = string.find(m[0]) + len(m[0])
            end_pos = string.find(m[1])
            if -1 not in [start_pos, end_pos]:
                if end_pos < start_pos: end_pos = len(string)
                return string[start_pos:end_pos]