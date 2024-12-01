import random
from tkinter import *

def buttonclick(event):  
    global lenyom
    lenyom=True 
    return

def buttonreleased(event): 
    global lenyom
    lenyom=False
    return

def motion(event): 
  if lenyom:
   # w.create_line(event.x,event.y,event.x+5,event.y+5, fill="#476042")
      w.create_oval(event.x,event.y,event.x+5,event.y+5)    
  return

master = Tk()
w = Canvas(master, width=1000,height=1000)
w.bind('<Button>',buttonclick)
w.bind('<ButtonRelease>',buttonreleased)
w.bind('<Motion>',motion)
w.pack()
mainloop()