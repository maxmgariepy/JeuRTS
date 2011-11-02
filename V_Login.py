# -*- encoding: ISO-8859-1 -*-
from tkinter import *

class V_Login(object):
    def __init__(self,parent):
        self.parent=parent #Vue
        self.cadreMain=Frame(self.parent.root)
        self.cadreAdresse=Frame(self.cadreMain)
        self.cadreChat=Frame(self.cadreMain)
        self.cadreInfo=Frame(self.cadreMain)
        
    def menu(self):
        print("menu")
        #Etiquettes
        self.etiquetteNom=Label(self.cadreAdresse,text="Votre nom")
        self.etiquetteServeur=Label(self.cadreAdresse,text="L'adresse du serveur(IPv4)")
        self.etiquetteEx=Label(self.cadreAdresse,text="Ex: 127.0.0.1")
        self.etiquetteHote=Label(self.cadreAdresse,text="Hôte")
        self.etiquetteHoteNom=Label(self.cadreAdresse,text="bob")
        self.etiquetteChat=Label(self.cadreChat,text="Chat")
        
        #Champ
        self.champNom=Entry(self.cadreAdresse)
        self.champServeur=Entry(self.cadreAdresse)
        
        #Liste
        self.listeChat=Listbox(self.cadreChat)  
        
        #Bouton
        self.boutonConnect=Button(self.cadreAdresse,text="Connection",command="")      
        
        self.cadreMain.pack()
        self.cadreInfo.grid_configure(rowspan=2)
        self.cadreInfo.grid(column=1,row=0)
        self.cadreAdresse.grid(column=0,row=0)
        self.cadreChat.grid_configure(sticky=S)
        self.cadreChat.grid(column=0,row=1)
        
        self.etiquetteNom.grid(column=0,row=0)
        self.champNom.grid(column=0,row=1)
        self.etiquetteServeur.grid(column=0,row=2)
        self.champServeur.grid(column=0,row=4)
        self.etiquetteEx.grid(column=0,row=3)
        self.etiquetteHote.grid(column=0,row=5)
        self.etiquetteHoteNom.grid(column=0,row=6)
        self.boutonConnect.grid(column=0,row=7)
        self.etiquetteChat.grid(column=0,row=0)
        self.listeChat.grid(column=0,row=1)
        
        
        #Etiquettes Info
        for i in range(16):
            self.etiquetteInfo=Label(self.cadreInfo,text="Joueur "+str(i+1))
            self.etiquetteInfo.grid(column=0,row=(i*2)+1)
            
            self.champInfo=Entry(self.cadreInfo)
            self.champInfo.grid(column=0,row=(i+1)*2)
            
            self.etiquetteCouleur=Label(self.cadreInfo,text="Couleur")
            self.etiquetteCouleur.grid(column=1,row=(i*2)+1)
            
            self.champCouleur=Entry(self.cadreInfo)
            self.champCouleur.grid(column=1,row=(i+1)*2)
            
            self.etiquettePolitique=Label(self.cadreInfo,text="Politique")
            self.etiquettePolitique.grid(column=2,row=(i*2)+1)
            
            self.champPolitique=Entry(self.cadreInfo)
            self.champPolitique.grid(column=2,row=(i+1)*2) 
            
            self.etiquetteReligion=Label(self.cadreInfo,text="Religion")
            self.etiquetteReligion.grid(column=3,row=(i*2)+1)
            
            self.champReligion=Entry(self.cadreInfo)
            self.champReligion.grid(column=3,row=(i+1)*2)       
        
    
        
        