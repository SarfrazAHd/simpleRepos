from tkinter import *

def btnClick(number):
    global operator
    operator= operator+str(number)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set((""))


def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "


root=Tk()
root.title("Calculator")

operator=""
text_input=StringVar()

inpt=Entry(root,font=('times',20,'bold'), textvariable=text_input,bd=30,insertwidth=4,justify="right",bg="powder blue",fg='blue')
inpt.grid(columnspan=4)

# 0 . AC -

b0 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="0",bd=8,command=lambda:btnClick(0))
b0.grid(row=1,column=0)

bdot = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text=".",bd=8,command=lambda:btnClick('.'))
bdot.grid(row=1,column=1)

b_clear = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="C",bd=8,command=btnClear)
b_clear.grid(row=1,column=2)

b_minus = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='white',bg='orange',text="-",bd=8,command=lambda:btnClick('-'))
b_minus.grid(row=1,column=3)

# 7 8 9 +

b7 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="7",bd=8,command=lambda:btnClick(7))
b7.grid(row=2,column=0)

b8 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="8",bd=8,command=lambda:btnClick(8))
b8.grid(row=2,column=1)

b9 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="9",bd=8,command=lambda:btnClick(9))
b9.grid(row=2,column=2)

bAddition = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='white',bg='orange',text="+",bd=8,command=lambda:btnClick('+'))
bAddition.grid(row=2,column=3)

#4 5 6  *

b4 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="4",bd=8,command=lambda:btnClick(4))
b4.grid(row=3,column=0)

b5 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="5",bd=8,command=lambda:btnClick(5))
b5.grid(row=3,column=1)

b6 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="6",bd=8,command=lambda:btnClick(6))
b6.grid(row=3,column=2)

bMultiplication = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='white',bg='orange',text="*",bd=8,command=lambda:btnClick("*"))
bMultiplication.grid(row=3,column=3)


# 1 2 3 /

b1 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="1",bd=8,command=lambda:btnClick(1))
b1.grid(row=4,column=0)

b2 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="2",bd=8,command=lambda:btnClick(2))
b2.grid(row=4,column=1)

b3 = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='black',text="3",bd=8,command=lambda:btnClick(3))
b3.grid(row=4,column=2)

bDivide = Button(root,padx=16,pady=16, font=('arial',20,'bold'),fg='white',bg='orange',text="/",bd=8,command=lambda:btnClick('/'))
bDivide.grid(row=4,column=3)

# Equal sign

bEqual=Button(root,padx=134,font=('times',30,'bold'),bd=8,height=-2,fg='black',text="=",command=btnEqual)
bEqual.grid(columnspan=4)




















root.mainloop()
