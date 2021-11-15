# -*- coding: utf-8 -*-
import class_echiquier
from src.class_echiquier import Echiquier
from PIL import Image, ImageTk
from tkinter import *

    
class Partie:

    def __init__(self, echiquier):
        self.window = Tk()
        self.window.title("JMO conseil")
        self.window.geometry("825x834")
        self.window.minsize(480, 360)
        self.window.iconbitmap("F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico")
        self.window.config(background='#41B77F')
        frame = Frame(self.window)
        ech = Echiquier()
        ech.new_game("blanc")
        width=800
        height=800
        img = ech.trace().resize((width, height))
        canvas=Canvas(frame,width=width,height=height,bg="#4065A4", bd=0,highlightthickness=0)
        canvas.create_image(width/2, height/2,image=img)
        frame.pack()




