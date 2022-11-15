global total
y=1
from tkinter import *
from tkinter import ttk



mainwindow = Tk()
mainwindow.title("Trivia >:)")
mainwindow.configure(bg="#ffc0eb")
mainwindow.geometry("650x300")


frame1= ttk.LabelFrame(mainwindow)
frame1.place (x=0,y=0)

imgwrong=PhotoImage(file="wrongcin.gif")
imgright=PhotoImage(file="cin5.gif")
label1 = ttk.Label( frame1,image=imgright)
label1.pack()

n= ttk.Notebook(mainwindow)
popcult= ttk.Frame(n)
spacebtl= ttk.Frame(n)
coode= ttk.Frame(n)
popcult2= ttk.Frame(n)
commonk= ttk.Frame(n)
starfight= ttk.Frame(n)



window= ttk.Frame(n)


def main(x):
    global total
    n.add(popcult, text="One")
    n.add(spacebtl, text="Two")
    n.add(coode, text="Three")
    n.add(popcult2, text="Four")
    n.add(commonk, text="Five")
    n.add(starfight, text="Six")




    total= ttk.Label(window, text="0")
   
    Label(popcult, text="How tall is hello kitty?").grid(row=2,column=2)
    Button(popcult, text="5 apples tall ",command=rightuno).grid(row=3,column=1)
    Button(popcult, text="six feet", command=wrongo).grid(row=3,column=2,)
    Button(popcult, text="8 bananas tall", command=wrongo).grid(row=3,column=3)




    Label(spacebtl, text="who is luke skywalkers father?").grid(row=2,column=2)
    Button(spacebtl, 
    text="obi-wan kenobi ",command=nobueno).grid(row=3,column=1)
    Button(spacebtl, text="darth vader ", command=sibueno).grid(row=3,column=2)
    Button(spacebtl, text="emperor palpatine", command=nobueno).grid(row=3,column=3)

    Label(coode, text="what base is a hexadecimal number?").grid(row=2,column=2)
    Button(coode, text="69",command=incorrect0).grid(row=3,column=1)
    Button(coode, text="16", command=correcto).grid(row=3,column=2)
    Button(coode, text="4", command=incorrect0).grid(row=3,column=3)

    Label(popcult2, text="what sanrio character likes basketball?").grid(row=2,column=2)
    Button(popcult2, text="pochacco",command=right1).grid(row=3,column=1)
    Button(popcult2, text="kuromi", command=wrong1).grid(row=3,column=2)
    Button(popcult2, text="dear daniel", command=wrong1).grid(row=3,column=3)


    Label(commonk, text="which sanrio character can fly by using their ears?").grid(row=2,column=2)
    Button(commonk, text=" Hello kitty",command=youdont).grid(row=3,column=1)
    Button(commonk, text="my melody", command=youdont).grid(row=3,column=2)
    Button(commonk, text=" cinnamoroll", command=yougotitdude).grid(row=3,column=3)

    Label(starfight, text="how many languages can C-3po speak in star wars?").grid(row=2,column=2)
    Button(starfight, text="3",command=no).grid(row=3,column=1)
    Button(starfight, text="32 trillion", command=no).grid(row=3,column=2)
    Button(starfight, text="6 million", command=si).grid(row=3,column=3)
    button_quit=Button(mainwindow, text="Exit", command=mainwindow.quit)
    button_quit.pack()
       

    return total

def rightuno():
    global total
    Label(popcult, text=" Correct :)").grid(row=1,column=2)
    label1.config(image=imgwrong)
    counter()
def wrongo():
    Label(popcult, text=" Incorrect :(").grid(row=1,column=2)

def sibueno():
    global total
    Label(spacebtl, text=" Correct :)").grid(row=1,column=2)
    counter()

def nobueno():
    Label(spacebtl, text="Incorrect :P").grid(row=1,column=2)

def correcto():
    global total
    Label(coode, text=" Correct :)").grid(row=1,column=2)
    counter()

def incorrect0():
    Label(coode, text=" Incorrect >:(").grid(row=1,column=2)

def right1():
    global total
    Label(popcult2, text=" Correct :) ").grid(row=1,column=2)
    counter()

def wrong1():
    Label(popcult2, text=" Incorrect :P").grid(row=1,column=2)

def yougotitdude():
    global total
    Label(commonk, text=" Correct :)").grid(row=1,column=2)
    counter()

def youdont():
    Label(commonk, text=" Incorrect :(").grid(row=1,column=2)

def si():
    global total
    Label(starfight, text=" Correct :)").grid(row=1,column=2)
    counter()

def no():
    Label(starfight, text=" Incorrect :(").grid(row=1,column=2)


def counter():
    global total 
    total['text'] = str(int(total['text']) + 1)

main(y)


n.pack(pady=50)

n.mainloop()