
#imports-------------------------------------
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
from tkinter.constants import DISABLED
import pygame, sys
from pygame.font import Font
from pygame.locals import *
import random, time
from tkinter.ttk import *
#windowbuilding-------------------------------
# creates a Tk() object
window = Tk()
window.geometry("1000x750")
window.resizable(width = False, height = False)
window.configure(bg = "pink")
window.title("𖧷ꕥ Sanrio Fun Time ꕥ𖧷")
background1=ttk.Frame(window)
background1.place(x=0,y=0)
backgroundmg=PhotoImage(file="Frensfrfr.gif")
title=ttk.Label(background1,image=backgroundmg)
title.pack()
title = Label(window)

 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("memory game ")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x600")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
 
# a button widget which will open a
# new window on button click
btn = Button(window,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady =100)
 
# mainloop, runs infinitely
mainloop()

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()

 

 
# a button widget which will open a
# new window on button click
bbtn = Button(window,
             text ="Click to open a new window",
             command = openNewWindow)
bbtn.pack(pady = 100)
 

# mainloop, runs infinitely
mainloop()