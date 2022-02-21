##### importations #####
import tkinter as tk
from mod.tools import ZoneBouton, ZoneTexte, ZoneLabel, true_print
import mod.activites as activites

##### parametere de la fenetre #####
fenetre = tk.Tk()
fenetre.geometry('1050x700')
fenetre.resizable(width=0, height=0)
fenetre.title("approndons le python3")
fenetre.configure(background="#000000")

##### création des zones de texte #####
global user_code, rule, py_exit, POINTS

user_code = ZoneTexte(fenetre, x = 10, y = 10, lx = 500, ly = 600, can_write = True)
rule = ZoneTexte(fenetre,x = 520, y = 10, lx = 520, ly = 400, can_write = False)
py_exit = ZoneTexte(fenetre,x = 520, y = 420,lx = 520, ly = 270, can_write = False)

retour = ZoneBouton(fenetre,x = 10, y = 620, lx = 100, ly = 70, txt = "retour", command = lambda: start_activite(max(ACTIVITE-1, 0)))
chek = ZoneBouton(fenetre,x = 120, y = 620, lx = 100, ly = 70, txt = "verifier", command = lambda: check_activite(ACTIVITE))
skip = ZoneBouton(fenetre,x = 230, y = 620, lx = 100, ly = 70, txt = "passer", command = lambda: start_activite(min(ACTIVITE+1, len(activite)-1)))
labelpoints = ZoneLabel(fenetre,x = 340, y = 620, lx = 170, ly = 70, txt = "0 point")

##### liste des activités #####

def input():
    global IPT_IDEX
    IPT_IDEX += 1
    if IPT_IDEX > len(activite[ACTIVITE].ipt):
        print(f"ERREUR: vous utilisez plus d'input que prevu ({len(activite[ACTIVITE].ipt)} max)")
    else:
        return activite[ACTIVITE].ipt[IPT_IDEX-1]

def print(*args):
    py_exit.set_txt(" ".join([str(x) for x in args]))

def check_activite(id):
    global POINTS, IPT_IDEX
    IPT_IDEX = 0
    py_exit.clear_txt()
    try: exec(user_code.get_txt())
    except Exception as e: print(str(f"ERREUR: {e}"))
    py_exit.color_txt("#ff0000")
    if activite[id].check(py_exit):
        py_exit.color_txt("#00ff00")
        POINTS += activite[id].points
        activite[id].points = 0
        labelpoints.set_txt(f"{POINTS} point" if POINTS <= 1 else f"{POINTS} points")
        if id == len(activite)-1 : rule.set_txt("Félicitacions, vous êtes arrivé à la fin")
        else : start_activite(id+1)
    #else: true_print(activite[id].good_output())

def start_activite(id):
    global ACTIVITE
    ACTIVITE = id
    user_code.clear_txt()
    py_exit.clear_txt()
    points = " "*25 + (f"({activite[id].points} point)" if activite[id].points <= 1 else f"({activite[id].points} points)")
    rule.set_txt(f"activité n°{activite[id].id}: {activite[id].categorie}{points}\n\n{activite[id].texte}")

POINTS = 0
activite = activites.load_activite()
start_activite(0)

fenetre.mainloop()