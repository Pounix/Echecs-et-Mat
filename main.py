# -*- coding: utf-8 -*-
import tkinter
from tkinter import Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.geometry("825x834")
fenetre.iconbitmap('F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico')
fenetre.title("JMO conseil")
frame = Frame(fenetre)
frame.pack()
# fenetre['bg']='blue'

champ_label = Label(fenetre, text="Les échecs c'est la vie !")
champ_label.pack()

ech = Echiquier()
ech.new_game("blanc")
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='1', colonne="A",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='2', colonne="B",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='3', colonne="C",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Possible", ligne='4', colonne="D",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='5', colonne="E",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='6', colonne="F",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='7', colonne="G",type='cursor'))
ech.echiquier.append(Piece("cursor", valeur="Select", ligne='8', colonne="H",type='cursor'))

#ech.cleanCursor()

image1 = ech.trace().resize((800, 800))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(fenetre, image=test)
label1.place(x=10, y=20)




fenetre.mainloop()
