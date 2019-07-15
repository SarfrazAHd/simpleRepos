from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("Tic Tac Toe")
click=True

def TicTac(buutons):
    global click
    if buutons["text"] == " " and click == True:
        buutons["text"] = "X"
        click =False

    elif buutons["text"] == " " and click == False:
        buutons["text"] = "O"
        click = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
         button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
         tkinter.messagebox.showinfo("Winner X", "X! You won this game" )
        
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" ):
         tkinter.messagebox.showinfo("Winner O", "O! You won this game" )

buttons=StringVar()

button1=Button(root, text=" " , font=('Times 26 bold'),width=6, height=2,fg="blue",command=lambda:TicTac(button1))
button1.grid(row=1 ,column=0, sticky = S+N+E+W )

button2=Button(root, text=" " , font=('Times 26 bold'),height=2, width=6 ,fg="blue",command=lambda:TicTac(button2))
button2.grid(row=1 ,column=1, sticky = S+N+E+W )

button3=Button(root, text=" " , font=('Times 26 bold '),height=2, width=6 ,fg="blue",command=lambda:TicTac(button3))
button3.grid(row=1 ,column=2, sticky = S+N+E+W )

button4=Button(root, text=" " , font=('Times 26 bold '),height=2, width=6 ,fg="blue",command=lambda:TicTac(button4))
button4.grid(row=2 ,column=0, sticky = S+N+E+W )

button5=Button(root, text=" " , font=('Times 26 bold '),height=2, width=6 ,fg="blue",command=lambda:TicTac(button5))
button5.grid(row=2 ,column=1, sticky = S+N+E+W )

button6=Button(root, text=" " , font=('Times 26 bold'),height=2, width=6,fg="blue",command=lambda:TicTac(button6))
button6.grid(row=2 ,column=2, sticky = S+N+E+W )

button7=Button(root, text=" " , font=('Times 26 bold '),height=2, width=6 ,fg="blue",command=lambda:TicTac(button7))
button7.grid(row=3 ,column=0, sticky = S+N+E+W )

button8=Button(root, text=" " , font=('Times 26 bold'),height=2, width=6 ,fg="blue",command=lambda:TicTac(button8))
button8.grid(row=3 ,column=1, sticky = S+N+E+W )

button9=Button(root, text=" " , font=('Times 26 bold'),height=2, width=6 ,fg="blue",command=lambda:TicTac(button9))
button9.grid(row=3 ,column=2, sticky = S+N+E+W )

root.mainloop()
