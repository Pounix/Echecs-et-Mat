# -*- coding: utf-8 -*-
import time
import tkinter
from tkinter import Button, Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

def choix_piece(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    colonne, ligne = ech.ma_case(x,y)
    ech.echiquier.append(Piece(couleur="cursor", valeur="Select", ligne='5', colonne='A',type='cursor'))  # fichier image = valeur_couleur
    img = ech.trace().resize((800, 800))
    photo=ImageTk.PhotoImage(img)
    canvas=Canvas(frame,width=width,height=height,bg="#4065A4", bd=0,highlightthickness=0)
    canvas.create_image(width/2, height/2, image=photo)
    canvas.pack()
    frame.pack(pady=10)

window = Tk()
window.title("JMO conseil")
window.geometry("825x825")
window.minsize(480, 360)
window.iconbitmap("F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico")
window.config(background='#41B77F')
frame = Frame(window)
ech = Echiquier()
ech.new_game("blanc")
width=800
height=800

img = ech.trace().resize((width, height))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(frame,width=width,height=height,bg="#4065A4", bd=0,highlightthickness=0)
canvas.create_image(width/2, height/2, image=photo)
canvas.pack()
frame.pack(pady=10)

window.bind("<Button 1>",choix_piece)
window.mainloop()
