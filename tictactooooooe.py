import tkinter as tk 
from tkinter import PhotoImage, messagebox
from tkinter.constants import DISABLED
tictactoe = tk.Tk()
tictactoe.geometry("600x500")
tictactoe.resizable(width = False, height = False)
tictactoe.configure(bg = "#aec599")
tictactoe.title("𓍊𓋼𓍊𓋼𓍊 Kuromi and Melody - Tic tac toe mini-game𓍊𓋼𓍊𓋼𓍊")

#x and o defined
First = "☠️"
Second = "🌸"

#Keep count
clicked = True
count = 0

#disable buttons 
def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

def do_win():
    win()

#check who won
def win():
    global winner 
    winner = False 
    if b1["text"] == First and  b2["text"] == First and  b3["text"] == First:
        b1.configure(bg ="#aec599")
        b2.configure(bg ="#aec599")
        b3.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
    elif b4["text"] == First and  b5["text"] == First and  b6["text"] == First:
        b4.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b6.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
    elif b7["text"] == First and  b8["text"] == First and  b9["text"] == First:
        b7.configure(bg ="#aec599")
        b8.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
    elif b1["text"] == First and  b4["text"] == First and  b7["text"] == First:
        b1.configure(bg ="#aec599")
        b4.configure(bg ="#aec599")
        b7.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
    elif b2["text"] == First and  b5["text"] == First and  b8["text"] == First:
        b2.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b8.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
    elif b3["text"] == First and  b6["text"] == First and  b9["text"] == First:
        b3.configure(bg ="#aec599")
        b6.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
    elif b1["text"] == First and  b5["text"] == First and  b9["text"] == First:
        b1.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
    elif b3["text"] == First and  b5["text"] == First and  b7["text"] == First:
        b3.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b7.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ ☠️ WINS")
        disable_all_buttons()
#o wins

    elif b1["text"] == Second and  b2["text"] == Second and  b3["text"] == Second:
        b1.configure(bg ="#aec599")
        b2.configure(bg ="#aec599")
        b3.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif b4["text"] == Second and  b5["text"] == Second and  b6["text"] == Second:
        b4.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b6.configure(bg ="#aec599")
        winner = True 
        messagebox.showerror("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
    elif b7["text"] == Second and  b8["text"] == Second and  b9["text"] == Second:
        b7.configure(bg ="#aec599")
        b8.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showerror("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS" )
    elif b1["text"] == Second and  b4["text"] == Second and  b7["text"] == Second:
        b1.configure(bg ="#aec599")
        b4.configure(bg ="#aec599")
        b7.configure(bg ="#aec599")
        winner = True 
        messagebox.showerror("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif b2["text"] == Second and  b5["text"] == Second and  b8["text"] == Second:
        b2.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b8.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif b3["text"] == Second and  b6["text"] == Second and  b9["text"] == Second:
        b3.configure(bg ="#aec599")
        b6.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif b1["text"] == Second and  b5["text"] == Second and  b9["text"] == Second:
        b1.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b9.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif b3["text"] == Second and  b5["text"] == Second and  b7["text"] == Second:
        b3.configure(bg ="#aec599")
        b5.configure(bg ="#aec599")
        b7.configure(bg ="#aec599")
        winner = True 
        messagebox.showinfo("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "♥︎ 🌸 WINS")
        disable_all_buttons()
    elif count == 9:
        messagebox.showerror("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊", "IT IS A TIE!")
    return winner

#When the buttons are pressed
def b_pressed(b):
    global clicked, count 
    if b["text"] == " " and clicked == True: 
        b["text"] = First
        clicked = False 
        count += 1 
    elif b["text"] == " " and clicked == False:
        b["text"] = Second
        clicked = True
        count += 1   
    else:
        messagebox.showerror("𓍊𓋼𓍊𓋼𓍊 Tic tac toe𓍊𓋼𓍊𓋼𓍊 ", "⚠︎︎This box has already been selected!")
    do_win()


#nine buttons for each square on tic tac toe
b1 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b1))
b2 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b2))
b3 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b3))

b4 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b4) )
b5 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b5) )
b6 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b6) )

b7 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b7) )
b8 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b8) )
b9 = tk.Button(tictactoe, text = " ", font = ("Times new roman", 20),height = 6, width = 11, relief = "flat", borderwidth= 0.5, bg = "#aec599", command = lambda: b_pressed(b9) )

#Exit button
byebye = tk.Button(tictactoe, text = "Exit",font = ("Stephanie",20), height = 1, width = 1, bg = "#aec599", command = tictactoe.quit )

#Grid for buttons 
b1.grid(row = 1, column = 3,padx = 0, pady = 0)
b2.grid(row = 1, column = 4,padx = 0, pady = 0)
b3.grid(row = 1, column = 5,padx = 0, pady = 0)

b4.grid(row = 2, column = 3,padx = 0, pady = 0)
b5.grid(row = 2, column = 4,padx = 0, pady = 0)
b6.grid(row = 2, column = 5,padx = 0, pady = 0)

b7.grid(row = 3, column = 3,padx = 0, pady = 0)
b8.grid(row = 3, column = 4,padx = 0, pady = 0)
b9.grid(row = 3, column = 5,padx = 0, pady = 0)

byebye.grid(row = 1, column = 6,padx = 0, pady = 20)

tictactoe.mainloop()