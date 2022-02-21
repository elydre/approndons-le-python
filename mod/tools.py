import tkinter as tk
import pprint

##### simplification de tkinter #####
class ZoneTexte:
    def __init__(self,fenetre,x,y,lx,ly,can_write=True):
        self.txt = tk.Text(fenetre,background="#212338",foreground="#b1e1f0",insertbackground="#00ffff",font=("consolas", 12))
        self.txt.place(x= x ,y=y,width= lx,height=ly)
        self.state="normal" if can_write else "disabled"
        self.txt.configure(state=self.state)
        
    def add_txt(self,txt):
        self.txt.configure(state="normal")
        self.txt.insert(0.0,txt)
        self.txt.configure(state=self.state)

    def get_txt(self):
        return self.txt.get("0.0", "end")

    def clear_txt(self):
        self.txt.configure(state="normal")
        self.txt.delete("0.0", "end")
        self.txt.configure(state=self.state)

    def color_txt(self,color):
        self.txt.configure(foreground=color)

    def set_txt(self,txt):
        self.clear_txt()
        self.add_txt(txt)

class ZoneBouton:
    def __init__(self,fenetre,x,y,lx,ly,txt,command):
        self.bouton = tk.Button(fenetre,text=txt,command=command,background="#212338",foreground="#b1e1f0",font=("consolas", 12))
        self.bouton.place(x= x ,y=y,width= lx,height=ly)

class ZoneLabel:
    def __init__(self,fenetre,x,y,lx,ly,txt):
        self.label = tk.Label(fenetre,text=txt,background="#212338",foreground="#b1e1f0",font=("consolas", 12))
        self.label.place(x= x ,y=y,width= lx,height=ly)

    def set_txt(self,txt):
        self.label.configure(text=txt)

##### class activité #####
class Way:
    RETURN_STRING = "print str"
    INPUT_RD = "input random"

class Activite:
    def __init__(self, categorie, id, texte, way, points, **kwargs):
        self.categorie = categorie
        self.id = id
        self.points = points
        self.texte = texte
        self.test_way = way
        self.string_espected = str(kwargs.get("string_espected", None))
        self.check_code = kwargs.get("check_code", None)
        self.ipt = kwargs.get("ipt", None)

    def check(self,py_exit):
        return self.good_output() == py_exit.get_txt()[0:-1]

    def good_output(self):
        if self.test_way == Way.RETURN_STRING:
            return self.string_espected
        elif self.test_way == Way.INPUT_RD:
            return str(self.check_code(self.ipt))
        else:
            return False

def true_print(*args):
    pprint.PrettyPrinter(indent=4).pprint(" ".join(str(x) for x in args))