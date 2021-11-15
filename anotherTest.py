# -*- coding: utf-8 -*-
# https://youtu.be/N4M4W7JPOL4

import webbrowser
from tkinter import *
from tkinter import ttk


def open_JMOconseil_website():
    webbrowser.open_new("www.jmoconseil.com")


window = Tk()
window.title("JMO conseil")
window.geometry("1080x720")
window.minsize(600, 300)
window.iconbitmap(
    "F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico"
)
window.config(background="#41B77F")

frame = Frame(window, bg="#41B77F", bd=1, relief=SUNKEN)

label_title = Label(
    frame, text="COUCOU c'es MOI", font=("Courrier", 40), bg="#41B77F", fg="white"
)
label_title.pack()
label_subtitle = Label(
    frame, text="--- the best ---", font=("Courrier", 20), bg="#41B77F", fg="white"
)
label_subtitle.pack()

yt_button = Button(
    frame, text="mon canal", font=("Courrier", 20), bg="white", fg="#41B77F",command=open_JMOconseil_website
)
yt_button.pack(pady=25, fill=X)

frame.pack(expand=YES)


window.mainloop()
