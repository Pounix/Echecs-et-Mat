# -*- coding: utf-8 -*-
import tkinter
from tkinter import Label, Tk, Pack
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.geometry("825x834")
champ_label = Label(fenetre, text="Les échecs c'est la vie !")
champ_label.pack()


ech = Echiquier()

# test
ech.new_game('blanc')
image1=ech.trace().resize((800,800))
test=ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
# label1.image = test

label1.place(x=10,y=20)

fenetre.mainloop()