# -*- coding: utf-8 -*-
import sys
sys.path.append(r'F:\OneDrive\Coding\Python\Python3\EchecEtMat\src')
# sys.path.append(r'C:\Users\jmoug\OneDrive\Coding\Python\Python3\EchecEtMat\src')
# sys.path.append(r'C:\Python_Virtual_Env\Virtual39Picture\Scripts')

import tkinter
from src.moves import *
from tkinter import Button, Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk
import src.settings
              
class Plateau(Tk):
    ech_coups_possibles={}
    
    def __init__(self):
        Tk.__init__(self)
        self.x = self.y = 0
        self.width=800
        self.height=800
        self.geometry(str(self.width)+'x'+str(self.height))
        self.title('JMO conseil - entrainement aux échecs')
        self.iconbitmap(r".\images\JMOfavicon.ico")
        frame=Frame(self, background='#41B77F')
        self.canvas = Canvas(self, width=self.width, height=self.height, cursor="cross")
        self.canvas.pack(side="top", fill="both")
        self.ech = Echiquier()
        self.ech.new_game()
        self.image = self.ech.trace().resize((self.width, self.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
        # self.bouton_newgame = Button(self, text="New Game", font=("Courrier", 25), bg='#41B77F')
        self.bind('<Button-1>', self.update)

    def initial(self,event):
        self.ech.new_game()
        
    def update(self, event):
        ca = self.ech.ma_case(event.x,event.y)
        # Trouver s'il y a une pièce sur cette case...
        p = self.ech.pieces[ca] if ca in self.ech.pieces.keys() else ''
        cur = self.ech.pieces[ca+'p']  if (ca+'p') in self.ech.pieces.keys() else ''
 
        if cur!='': # on a clické sur un cursor
            self.ech.pieces=self.ech_coups_possibles[ca]
            self.ech.cleanCursor()
            # self.ech.check_échec()    TODO !!
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
        elif p!='': # on a clické sur une pièce
            couleur_attaquant=1- p.couleur
            self.ech.cleanCursor()
            self.ech_coups_possibles=coups_jouables(self.ech.pieces,ca)
            self.ech_coups_possibles=elimine_coups_provoquant_echec(liste_coups=self.ech_coups_possibles, couleur_attaquant=couleur_attaquant)
            co = 2 if self.ech_coups_possibles=={} else 3   # Bloqué si aucun coup possible ou sinon Select
            self.ech.pieces[ca+'c']=Piece(couleur=co, valeur=6)
            for c in self.ech_coups_possibles.keys():
                self.ech.pieces[c+'p']=Piece(couleur=4, valeur=6)
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)

   
if __name__ == "__main__":
    app = Plateau()
    app.mainloop()