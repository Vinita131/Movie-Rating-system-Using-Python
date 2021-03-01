from defaultpage import *
from tkinter import *
from DatabaseHelper import *
from Components.scrollableframe import VerticalScrolledFrame
from Components.ButtonComponent import ImageButton
from PIL import Image,ImageTk
class UserHomePage(DefaultPage):
    def __init__(self,root,user_details):
        self.user_details=user_details
        self.root=root
        print("User home page called")
        super().__init__(root)
        self.root.state('zoomed')
        self.result=self.r=self.my=None
        self.logout_button=Button(self.f,text="Logout",width=20,height=2, activebackground="gray",activeforeground="white", command=self.logout)
        self.logout_button.place(x=1200,y=50)
        self.add_frame()
        self.add_Movies()
    def add_frame(self):
        self.Movie_frame=VerticalScrolledFrame(self.f, bg="#030202",width=1400,height=675)
        self.Movie_frame.place(x=50,y=100)
    def logout(self):
        import MainPage
        self.f.destroy()
        self.panel.destroy()
        self.redirect = MainPage.MainPage(self.root)




    def add_Movies(self):
        query= """ select MoviePhoto,MovieName,MovieRating
                   from Movies"""
        self.result=DatabaseHelper.get_all_data(query)
        self.d={}
        l={}
        avg={}
        self.raw={}
        self.im={}
        j=0
        r=0
        c=0
        xco=100
        yco=500
        for i in self.result:
            self.r=Image.open("images/"+i[0])
            self.r=self.r.resize((400,400))
            self.my=ImageTk.PhotoImage(self.r)
            v=ImageButton(self.Movie_frame,self.my,self.rate,i[0])
            l[j]=Label(self.Movie_frame,width=25,height=3,fg='Black',bg='Pink',text=i[1],font=("Lucida Sans Typewriter",20,"bold"),  relief=SOLID, borderwidth=2)
            avg[j]=Label(self.Movie_frame,width=15,height=3,fg='Black',bg='White',text=f"rating={i[2]}",font=("Copperplate Gothic Bold",18,"bold"),  relief=SOLID, borderwidth=2)
            self.raw[j]=self.r
            self.im[j]=self.my
            v.grid(row=r,column=c,padx=100,pady=25)
            l[j].grid(row=r+1,column=c,pady=5)
            avg[j].grid(row=r+2,column=c)


            if (c==1):
                r=r+3
                c=0
                xco=100
                yco=yco+400
            else:
                c=c+1
                xco=xco+500



            j=j+1




    def rate(self,n):
        x=None
        for i in self.result:
            if(i[0]==n):
                x=i
                break
        tple=(0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5)
        self.add_frame()
        self.r = Image.open("images/" + x[0])
        self.r = self.r.resize((400, 400))
        self.my = ImageTk.PhotoImage(self.r)
        v = Button(self.Movie_frame, image=self.my)
        v.grid(row=0,column=0,padx=100,pady=100)
        new= Label(self.Movie_frame, width=25, height=3, fg='Black', bg='Pink', text=x[1],
                     font=("Broadway", 18, "bold"), relief=SOLID, borderwidth=2)
        new2 = Label(self.Movie_frame, width=10, height=3, fg='Black', bg='White', text=f"rating={x[2]}",
                       font=("Copperplate Gothic Bold", 18, "bold"), relief=SOLID, borderwidth=2)
        new.grid(row=0,column=1,pady=200,sticky="n")
        new2.grid(row=0,column=1,pady=200,sticky="ews")
        self.sss=IntVar()
        self.vv=Spinbox(self.Movie_frame,values=tple,textvariable=self.sss,width=40)
        l=Label(self.Movie_frame, width=7, height=1, fg='Black', bg='white', text="RATING", font=("Broadway", 18, "bold"),
              relief=SOLID, borderwidth=2)
        l.grid(row=0,column=0,padx=40,pady=45,sticky="sw")
        self.vv.grid(row=0,column=0,pady=50,sticky="s")
        bu=Button(self.Movie_frame,text="submit",width=20,height=2, activebackground="gray",activeforeground="white", command=lambda:self.run(self.sss,x))
        bu.grid(row=0,column=1,sticky="s",pady=75)



    def run(self,p,movie):
        print(p.get())
        p=p.get()
        print(movie)
        if(movie[2]==0.0):
            pass

        else:
            p=movie[2]+p
            p=p/2

        query=""" select *
                  from rating
                  where customerid=%s """
        params=(self.user_details[0])
        res=DatabaseHelper.get_all_data(query,params)
        print(res)
        if(res is None or len(res)==0):
            query=""" insert into rating(customerid,ratedMovies)
                      values(%s,%s)"""
            params=(self.user_details[0],movie[1])
            DatabaseHelper.execute_query(query, params)
            query = """update Movies
                        set MovieRating=%s
                        where MovieName=%s """
            params = (p, movie[1])
            DatabaseHelper.execute_query(query, params)
        else:

            al = res[-1][2]
            print(al)

            ra=movie[1]
            if(al.find(ra)!=-1):
                messagebox.showerror('INVALID',"you have already rated this Movie")

            else:
                query = """update Movies
                            set MovieRating=%s
                            where MovieName=%s """
                params = (p, movie[1])
                DatabaseHelper.execute_query(query, params)
                messagebox.showinfo('rating successfull', "we have registered your rating")
                s = al+","+ra
                query = """ insert into rating(customerid,ratedMovies)
                                                  values(%s,%s)"""
                params = (self.user_details[0], s)
                DatabaseHelper.execute_query(query, params)
        self.add_frame()
        self.add_Movies()


if(__name__=="__main__"):
    root=Tk()
    m=UserHomePage(root)
    root.mainloop()