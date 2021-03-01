from tkinter import *
from PIL import Image,ImageTk
class DefaultPage:
    def __init__(self,root):
        self.root=root
        self.root.iconbitmap('images/Movie.ico')
        self.root.title('MyMovies')
        self.f=Frame(self.root,width=1600,height=900)
        self.raw_image = Image.open("images/6921.jpg")
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)
        self.panel = Label(self.f, image=self.img)
        self.m = Message(self.f, width=600, font=("BankGothic Md BT",20,"bold","italic"),text="MyMovies",bg="White",relief=RAISED,borderwidth=4)

        self.m.place(x=675,y=50)
        self.footer=Label(self.f,bg="ivory3",height=1,width=500,text="@Copyright 2020 MYMovies. All rights reserved")
        self.footer.pack(side=BOTTOM,fill=X)

        self.panel.pack()
        self.panel.pack_propagate(0)


        self.f.pack()
        self.f.pack_propagate(0)


if(__name__=="__main__"):
    root=Tk()
    d=DefaultPage(root)
    root.mainloop()
