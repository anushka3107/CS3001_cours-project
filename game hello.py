
from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox

#main window

root = Tk()

#The window size of the game.
root.resizable(width=False, height=False)
root.geometry('1000X752')
root.configure(background='black')
root.title("HELLO")

#defining command for buttons
def Gameplay():
    messagebox.showinfo("Be the first player to send all your 3 pawns to home.", "Click Play my Chance on your turn and follow the task that pops up."" 2.If all your color tokens reach home after that first. YOU WIN." "If only 2 players are playing, Game will be over","If the players are three or four players , game continues between the ones whose tokens haven't reached Home.")
   
#background image
c = Canvas(root,bg = "grey",height = 1000,width = 752)
c.pack()
Photo = PhotoImage(file="gameboard.png")
PhotoImage = Label(image= Photo, bg = "black" , height = 900, width = 652).place(x = 0,y = 0)


#Title of the Game
Label(root, text = 'HELLO!',fg = "white",bg = "red",font =(300)).place(x = 620,y = 200)
   
#creating buttons
button1 = Button(root, text = "Start Game", fg = "white", bg = "yellow", padx = 25, pady = 5).place(x = 910, y = 480)
button2 = Button(root, text = "Gameplay", fg = "white", bg = "yellow", padx = 22, pady = 5, command = Gameplay).place(x = 910, y = 550)
button3 = Button(root, text = "Exit Game", fg = "white", bg = "yellow",padx = 25, pady = 5, command = root.destroy).place(x = 910, y = 620)

#main event loop for screen
root.mainloop()






























































































































