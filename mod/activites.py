from mod.tools import Way, Activite
import random as rd

def load_activite():
    return [
    Activite(categorie = "print",
            id = 1,
            points = 1,
            texte = "affichez le nombre 13 a l’aide de print()",
            way = Way.RETURN_STRING,
            string_espected="13"),
    
    Activite(categorie = "print",
            id = 2,
            points = 1 ,
            texte = "affichez \"coucou\"",
            way = Way.RETURN_STRING,
            string_espected="coucou"),

    Activite(categorie = "print",
            id = 3,
            points = 2 ,
            texte = "affichez le resultat de 4+6**0.5",
            way = Way.RETURN_STRING,
            string_espected=4+6**0.5),
    
    Activite(categorie = "input",
            id = 4,
            points = 1 ,
            texte = "input() est automatiquement remplit par APPRONDONS-\nLE-PYTHON, affichez se que le programme envoie",
            way = Way.INPUT_RD,
            ipt = [rd.randint(0,10)],
            check_code = lambda ipt: ipt[0]),
    
    Activite(categorie = "input",
            id = 5,
            points = 2 ,
            texte = "affichez le carré d'une entrée automatique",
            way = Way.INPUT_RD,
            ipt = [rd.randint(0,10)],
            check_code = lambda ipt: ipt[0]**2),
    
    Activite(categorie = "input",
            id = 6,
            points = 2,
            texte = "affichez la somme de 2 entrées automatiques",
            way = Way.INPUT_RD,
            ipt = [rd.randint(0,10),rd.randint(0,10)],
            check_code = lambda ipt: ipt[0]+ipt[1]),
    
    Activite(categorie = "if/else",
            id = 7,
            points = 2,
            texte = "afficher \"vrai\" si l'input est True sinon \"faux\"",
            way = Way.INPUT_RD,
            ipt = [rd.choice([True, False])],
            check_code = lambda ipt: "vrai" if ipt[0] == True else "faux"),
    ]