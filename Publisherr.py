from defaultpage import *
from tkinter import *
from DatabaseHelper import *
from PIL import Image,ImageTk
class PublisherPage(DefaultPage):
    def __init__(self,root,admin_details):
        self.user_details=admin_details
        self.root=root

        print("User home page called")


        super().__init__(root)
        self.root.state('zoomed')
        self.button1=Button(self.f,text="Add Movie",width=40,height=2,activebackground="gray",activeforeground="white",command=self.add_movie)
        self.button2=Button(self.f,text="Check Movie Rating",width=40,height=2,activebackground="gray",activeforeground="white",command=self.check_movie)
        self.logout_button=Button(self.f,text="Logout",width=20,height=2, activebackground="gray",activeforeground="white", command=self.logout)
        self.logout_button.place(x=1200,y=50)
        self.button1.place(x=100,y=130)
        self.button2.place(x=400,y=130)
    def logout(self):
        import MainPage
        self.f.destroy()
        self.panel.destroy()
        self.redirect = MainPage.MainPage(self.root)
    def add_movie(self):
        login_window = Toplevel()
        login_window.title("New Movie")
        self.ff = Frame(login_window, height=200, width=400)
        l1 = Label(self.ff, width=20, text="Enter Movie Name: ")
        self.Movie_name = Entry(self.ff, width=30, fg='black', bg='white')
        self.Movie_name.focus_set()
        self.Movie_Image= Entry(self.ff, width=30, fg='black', bg='white')
        l2 = Label(self.ff, width=20, text="Enter Image: ")
        self.Movie_rating=Entry(self.ff,width=30,fg='black',bg='white')
        l3=Label(self.ff,width=20,text='Enter Rating:')
        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        l3.grid(row=3,column=1,padx=10,pady=10)
        self.Movie_name.grid(row=1, column=4, padx=10, pady=10)
        self.Movie_Image.grid(row=2, column=4, padx=10, pady=10)
        self.Movie_rating.grid(row=3, column=4, padx=10, pady=10)
        b1 = Button(self.ff, text="Submit", height=2, width=10, command=lambda: self.entry(login_window))
        b1.grid(row=4, column=1, padx=10, sticky='e')
        b2 = Button(self.ff, text="Reset", height=2, width=10, command=lambda: self.reset())
        b2.grid(row=4, column=4, padx=10, sticky='w')
        self.ff.pack()
        self.ff.grid_propagate(0)
    def check_movie(self):
        login_window = Toplevel()
        login_window.title("New Movie")
        self.fff = Frame(login_window, height=200, width=400)
        l1 = Label(self.fff, width=20, text="Enter Movie Name: ")
        # storing this inside self because we need this later to get data
        self.Movie = Entry(self.fff, width=30, fg='black', bg='white')
        self.Movie.focus_set()
        b1 = Button(self.fff, text="Submit", height=2, width=10,
                    command=lambda: self.display(login_window))
        self.Movie.grid(row=1,column=2)
        l1.grid(row=1, column=1, padx=10, pady=10)
        b1.grid(row=2, column=1, padx=10, sticky='e')
        b2 = Button(self.fff, text="Reset", height=2, width=10, command=lambda: self.reset1())
        b2.grid(row=2, column=2, padx=10, sticky='w')
        self.fff.pack()
        self.fff.grid_propagate(0)
    def display(self,n):

        p=self.Movie.get()
        n.destroy()

        query = """ select MoviePhoto,MovieName,MovieRating
                    from Movies
                    where MovieName=%s"""
        params=(p,)
        result = DatabaseHelper.get_data(query,params)
        if(result is None or len(result)==0):
            messagebox.showerror("Error", f"{p} Movie Not Pesent")
        else:


            self.new = LabelFrame(self.f, bg="#030202", width=1300, height=575)

            self.ra = Image.open("images/" + result[0])
            self.ra = self.ra.resize((400, 400))
            self.myy = ImageTk.PhotoImage(self.ra)
            v = Button(self.new, image=self.myy)
            l= Label(self.new, width=20, height=3, fg='Black', bg='Pink', text=result[1],
                     font=("Broadway", 18, "bold"), relief=SOLID, borderwidth=2)
            avg= Label(self.new, width=20, height=3, fg='Black', bg='White', text=result[2],
                       font=("Copperplate Gothic Bold", 18, "bold"), relief=SOLID, borderwidth=2)

            v.grid(row=0, column=0, padx=100, pady=100)
            l.grid(row=0, column=1, pady=200, sticky="n")
            avg.grid(row=0, column=1, pady=200, sticky="ews")
            button1 = Button(self.new, text="close", width=40, height=2, activebackground="gray",
                              activeforeground="white", command=lambda:self.close())
            button1.grid(row=0,column=1,sticky="sw",pady=75,padx=50)
            self.new.place(x=50, y=200)
            self.new.grid_propagate(0)

    def close(self):
        self.new.destroy()


    def entry(self,p):
        Img=self.Movie_Image.get()
        name=self.Movie_name.get()
        rate=float(self.Movie_rating.get())
        p.destroy()
        query="""insert into Movies(MoviePhoto,MovieName,MovieRating)
                 values(%s,%s,%s)"""
        params=(Img,name,rate)
        DatabaseHelper.execute_query(query,params)
        messagebox.showinfo('New Movie', "New Movie Added Successfully")
    def reset(self):
        self.Movie_rating.delete(0, END)
        self.Movie_name.delete(0, END)
        self.Movie_Image.delete(0, END)
    def reset1(self):
        self.Movie.delete(0, END)

