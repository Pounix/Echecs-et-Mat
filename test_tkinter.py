# -*- coding: utf-8 -*-
import time
import tkinter
from tkinter import Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

def click_gauche(event):
    x, y = event.x, event.y
    print (x,y)
    image1=Image.open("images\\échiquier.jpg").resize((800, 800))
    label1 = tkinter.Label(fenetre, image=ImageTk.PhotoImage(image1))
    label1.place(x=10, y=20)        
    label1.pack()
    label1.update()


fenetre = Tk()
fenetre.geometry("825x834")

ech = Echiquier()
ech.new_game("blanc")


image1=Image.open("images\\échiquier.jpg").resize((800, 800)) # ech.trace().resize((800, 800))
label1 = tkinter.Label(fenetre, image=ImageTk.PhotoImage(image1))
label1.image=image1
# label1.place(x=10, y=20)
label1.pack()
# label1.update()

fenetre.bind('<Button-1>', click_gauche)

fenetre.mainloop()