# -*- coding: utf-8 -*-

import time
import tkinter
from tkinter import Button, Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

IMG1 = "F:\\OneDrive\\Coding\\Python\\Python3\\EchecEtMat\\images\\Roi_noir.png"
IMG2 = "F:\\OneDrive\\Coding\\Python\\Python3\\EchecEtMat\\images\\Tour_blanc.png"

class ExampleApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.x = self.y = 0
        self.width=800
        self.height=800
        self.canvas = Canvas(self, width=self.width, height=self.height, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.ech = Echiquier()
        self.ech.new_game("blanc")

        self.image = self.ech.trace().resize((self.width, self.height))

        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image((0, 0), anchor="nw", image=self.photo)

        self.bind('<Button-1>', self.update)

    def update(self, event):
        colonne, ligne = self.ech.ma_case(event.x,event.y)

        # Trouver s'il y a une pièce sur cette case...
        ca=''.join(colonne+ligne)
        flg=''
        for p in self.ech.echiquier:
            if p.case==ca:
                flg=p
                break
        
        if isinstance(flg,Piece):
            self.ech.cleanCursor()
            self.ech.echiquier.append(Piece(couleur="cursor", valeur="Select", ligne=ligne, colonne=colonne,type='cursor'))  # fichier image = valeur_couleur


   


        
            for c in cj:
                self.ech.echiquier.append(Piece(couleur="cursor", valeur="Possible", colonne=c[0], ligne=c[1],type='cursor'))
            
            
            self.image = self.ech.trace().resize((self.width, self.height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image((0, 0), anchor="nw", image=self.photo)
   
if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()