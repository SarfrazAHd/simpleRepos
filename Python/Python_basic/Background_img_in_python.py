

from tkinter import *

root=Tk()
root.title("Background Image")



canvs=Canvas(root,width=400,height=400)
canvs.pack()

my_img=PhotoImage(file="gif_image.gif")

canvs.create_image(0,0, anchor=NW,image=my_img)





l1=Label(text="Welcome to BG image",font=("arial",15,'bold'),fg="white",bg="black")
l1.place(x=100,y=10)

root.mainloop()
