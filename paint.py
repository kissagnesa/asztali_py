import random
from tkinter import *
from tkinter.colorchooser import askcolor

lenyom = False
utolso_x, utolso_y = None, None
aktualis_szin = "#000000"  

def buttonclick(event):  
    global lenyom, utolso_x, utolso_y
    lenyom = True
    utolso_x, utolso_y = event.x, event.y
    return

def buttonreleased(event): 
    global lenyom, utolso_x, utolso_y
    lenyom = False
    utolso_x, utolso_y = None, None
    return

def motion(event): 
    global lenyom, utolso_x, utolso_y, aktualis_szin
    if lenyom:
        if utolso_x is not None and utolso_y is not None:
            w.create_line(utolso_x, utolso_y, event.x, event.y, fill=aktualis_szin, width=2)
        utolso_x, utolso_y = event.x, event.y
    return

def szinvalasztas():
    global aktualis_szin
    szin = askcolor()[1]  
    if szin:
        aktualis_szin = szin

master = Tk()
master.title("Egyszerű Paint")
w = Canvas(master, width=800, height=600, bg="white")
w.bind('<ButtonPress-1>', buttonclick)
w.bind('<ButtonRelease-1>', buttonreleased)
w.bind('<Motion>', motion)
w.pack()

szin_gomb = Button(master, text="Színválasztás", command=szinvalasztas)
szin_gomb.pack()

mainloop()
