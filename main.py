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
from src.class_plateau import Plateau
from PIL import Image, ImageTk
import src.settings

         
app = Plateau()
app.mainloop()