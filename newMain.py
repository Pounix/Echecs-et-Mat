# -*- coding: utf-8 -*-
import time
import tkinter
from tkinter import Label, Tk, Pack, Frame, Canvas
from tkinter.constants import NW
from src.class_echiquier import Echiquier
from src.class_piece import Piece
from PIL import Image, ImageTk

def choix_piece(event):
    
    x, y = event.x, event.y
    # print('{}, {}'.format(x, y))
    colonne, ligne = ech.ma_case(x,y)
    ech.cleanCursor()
    # breakpoint()
    t1=time.time()
    print(t1)
    
    ech.echiquier.append(Piece(couleur="cursor", valeur="Select", ligne='5', colonne='A',type='cursor'))  # fichier image = valeur_couleur
    image1 = ech.trace().resize((300, 300))

    test = ImageTk.PhotoImage(image1)
    
    t2=time.time()
    print(t2)
    print(t2-t1)
    label1 = tkinter.Label(fenetre, image=test)
    
    label1.place(x=10, y=20)
    label1.pack()
    label1.update()


fenetre = Tk()
# fenetre.geometry("825x834")
# fenetre.iconbitmap('F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico')
# fenetre.title("JMO conseil")
# frame = Frame(fenetre)
# frame.pack()
# fenetre['bg']='blue'

champ_label = Label(fenetre, text="Les échecs c'est la vie !")
champ_label.pack()

ech = Echiquier()
ech.new_game("blanc")

image1 = ech.trace().resize((800, 800))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(fenetre, image=test)
label1.place(x=10, y=20)
label1.pack()
label1.update()

time.sleep(2)

# ech.echiquier.append(Piece(couleur="cursor", valeur="Select", ligne='2', colonne="E",type='cursor'))

image1 = ech.trace().resize((800, 800))   # Image.open("images\\échiquier.jpg").resize((800, 800))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(fenetre, image=test)
label1.place(x=10, y=20)
label1.update()

  
fenetre.bind('<Button-1>', choix_piece)


fenetre.mainloop()

