# -*- coding: utf-8 -*-
# https://youtu.be/N4M4W7JPOL4

import random
import string
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(all_chars) for x in range(random.randint(password_min, password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    

window = Tk()
window.title("Generateur de mote de passe")
window.geometry("720x480")
window.iconbitmap(
    "F:\\OneDrive\\01 - JMO conseil\\30-Logos\\JMO conseil\\JMOfavicon.ico"
)
window.config(background="#4065A4")

frame = Frame(window, bg="#4065A4")

#  creation image
width = 300
height = 300
image = (
    PhotoImage(file="F:/OneDrive/Coding/ICONS/JMOcubeLogo02greenTRSP carré 700x700.png")
    .zoom(1)
    .subsample(3)
)
canvas = Canvas(
    frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0
)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# sous boite
right_frame = Frame(frame, bg="#4065A4")
right_frame.grid(row=0, column=1, sticky=W)

label_title = Label(
    right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#4065A4", fg="white"
)
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg="#4065A4", fg="white")
password_entry.pack()

generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg="#4065A4", fg="white",command=generate_password)
generate_password_button.pack(fill=X, pady=10)

frame.pack(expand=YES)  # Expand X pour centrer

#barre de menus
menu_bar = Menu(window)
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier",menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()
