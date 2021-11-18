# -*- coding: utf-8 -*-
import sys
sys.path.append(r'F:\OneDrive\Coding\Python\Python3\EchecEtMat\src')

import tkinter
from src.moves import *
from tkinter import Button, Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

              
class Plateau(Tk):
    ech_coups_possibles={}
    
    def __init__(self):
        Tk.__init__(self)
        self.x = self.y = 0
        self.width=800
        self.height=800
        self.canvas = Canvas(self, width=self.width, height=self.height, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.ech = Echiquier()
        self.ech.new_game()
        self.image = self.ech.trace().resize((self.width, self.height))
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
        self.bind('<Button-1>', self.update)

    def update(self, event):
        ca = self.ech.ma_case(event.x,event.y)
        # Trouver s'il y a une pièce sur cette case...
        p = self.ech.pieces[ca] if ca in self.ech.pieces.keys() else ''
        cur = self.ech.pieces[ca+'p']  if (ca+'p') in self.ech.pieces.keys() else ''
 
        if cur!='': # on a clické sur un cursor
            self.ech.pieces=self.ech_coups_possibles[ca]
            self.ech.cleanCursor()
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
        elif p!='': # on a clické sur une pièce
            couleur_attaquant='noir' if p.couleur=='blanc' else 'blanc'
            self.ech.cleanCursor()
            self.ech_coups_possibles=coups_jouables(self.ech.pieces,ca)
            self.ech_coups_possibles=elimine_coups_provoquant_echec(liste_coups=self.ech_coups_possibles, couleur_attaquant=couleur_attaquant)
            # breakpoint()
            v = 'Bloqué' if self.ech_coups_possibles=={} else 'Select'
            self.ech.pieces[ca+'c']=Piece(couleur="cursor", valeur=v, type=False) # fichier image = valeur_couleur
            v='Possible'
            for c in self.ech_coups_possibles.keys():
                self.ech.pieces[c+'p']=Piece(couleur="cursor", valeur=v, type=False,case_précédente=ca)
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)

   
if __name__ == "__main__":
    app = Plateau()
    app.mainloop()