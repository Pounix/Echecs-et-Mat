# -*- coding: utf-8 -*-

import tkinter


from tkinter import Button, Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

class Plateau(Tk):

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
        try:
            p=self.ech.pieces[ca]
        except KeyError:
            p=''
        
        if isinstance(p,Piece):
            self.ech.cleanCursor()
            self.ech.pieces[ca+'c']=(Piece(couleur="cursor", valeur="Select", type=False,case_précédente=ca))  # fichier image = valeur_couleur

            # for c in cj:
            #     self.ech.echiquier.append(Piece(couleur="cursor", valeur="Possible", colonne=c[0], ligne=c[1],type='cursor'))
            
            
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
   
if __name__ == "__main__":
    app = Plateau()
    app.mainloop()