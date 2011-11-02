# -*- encoding: ISO-8859-1 -*-
from tkinter import *
from V_Login import *
from V_Serveur import *

class Vue(object):
    def __init__(self,parent):
        self.parent=parent #Controleur
        self.root=Tk()
        self.v_login=V_Login(self)
        self.v_serveur=V_Serveur(self)
        self.v_login.menu()
        self.root.mainloop()
        
        
        
if __name__ == "__main__":
    v=Vue(1)
        