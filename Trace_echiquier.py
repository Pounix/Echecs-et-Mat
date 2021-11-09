# -*- coding: utf-8 -*-

from tkinter import *
 
class Board(Canvas):
    def __init__(self, master=None, color='white', width=200, height=200):
        Canvas.__init__(self, master, bg=color, width=width, height=height)
        self.height = width
        self.width = height
        self.pack()
 
    def create_square(self, x, y, size, color='black'):
        for i in range(x, self.width, size*2):
            for j in range(y, self.height, size*2):
                self.create_rectangle(i, j, i+size, j+size, fill=color)
 
 
def create_board(master, color_bg, x=0, y=0, size=20, color='black'):
    my_board = Board(master, color_bg)
    my_board.create_square(x, y, size, color)
    return my_board
     
 
root = Tk()
board = create_board(root, 'white')
root.mainloop()