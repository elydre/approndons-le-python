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

version = "0.1.0"

def segmenter_string(code: str) -> list:
    actual = 0
    start = 0
    exit_code = code
    for i in range(len(code)):
        car = code[i]
        if car == "(":
            actual += 1
            if start == 0:
                start = i
        elif car == ")":
            actual -= 1
            if actual == 0:
                exit_code = [code[0:start], [[code[start+1:i]]], code[i+1:]]
                while "" in exit_code:
                    exit_code.remove("")
                break
    return exit_code

def epurer(code: list) -> list:
    return [epurer(l[0]) if type(l) is list and len(l) == 1 and type(l[0]) is list else epurer(l) if type(l) is list else l for l in code]

def edit_liste(liste: list) -> list:
    # transphormer les liste de liste de liste et liste de liste en liste et ajouter a la liste d'avant les liste simple qui ne sont pas de liste ou de liste de liste
    # transphormer sa:
    # [['str', [['1']], ['+str', [[['list', [[['str', [['123123']]]]]]]], '*2']]]
    # en sa:
    # ['str', ['1'], '+str', ['list', ['str', ['123123']]], '*2']
    pass

def parenthese_in_code(code: list) -> bool:
    return True in [ parenthese_in_code(l) if type(l) is list else "(" in l or ")" in l for l in code]

def segmenter(code: list) -> list:
    print(code)
    return [segmenter(l) if type(l) is list else segmenter_string(l) for l in code]


def launch_segmenter(code: str) -> list:
    code = [str(code)]
    while parenthese_in_code(code):
        try:
            code = segmenter(code)
        except Exception as e:
            print(e)
            break
    return code[0]
    # return epurer(code)[0]


test = "str(1)+str(list(str(123123)))*2"
print(launch_segmenter(test))