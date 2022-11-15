from tkinter import*
import random

game = Tk()
game.title= ("Memory game")
game.geometry= ("500x550")

#number code match here
numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

random.shuffle (numbers)

#button frame
frame = Frame(game)
frame.pack (pady=60)

def something():
    pass

bton1 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton2 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton3 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton4 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton5 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton6 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton7 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton8 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton9 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton10 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton11 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton12 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton13 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton14 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton15 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)
bton16 = Button (frame,text= "o", font= ("Comic", 20),height=5,width=6, command= something)


# Grid our Buttons
bton1.grid(row=1, column=0)
bton2.grid(row=1, column=1)
bton3.grid(row=1, column=2)
bton4.grid(row=1, column=3)

bton5.grid(row=2, column=0)
bton6.grid(row=2, column=1)
bton7.grid(row=2, column=2)
bton8.grid(row=2, column=3)

bton9.grid(row=3, column=0)
bton10.grid(row=3, column=1)
bton11.grid(row=3, column=2)
bton12.grid(row=3, column=3)

bton13.grid(row=4, column=0)
bton14.grid(row=4, column=1)
bton15.grid(row=4, column=2)
bton16.grid(row=4, column=3)

game.mainloop()