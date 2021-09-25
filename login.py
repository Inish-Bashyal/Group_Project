from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def login():
    uname=e1.get()
    pwd=e2.get()

    users=["INISH","BIKASH","BIBASH","MANISH","ADMIN"]

    #applying empty validation
    if uname=='' or pwd=='':
        messagebox.showerror("Error", "All fields required")
    else:
        for i in users:
            if uname==i and pwd=="ADMIN":
                messagebox.showinfo("SUCCESS", "WELCOME")
                login_screen.destroy()
                import Student_Management_System
                break
        j=uname != "INISH" or uname != "BIBASH" or uname != "BIKASH" or uname != "MANISH" or uname!= "ADMIN"
        if j and pwd != "ADMIN":
            messagebox.showerror("Error", "Wrong username or password!!!")
            e1.delete(0, END)
            e2.delete(0, END)





def loginform():

    global login_screen

    login_screen = Tk()
    login_screen.title("LOG IN")





    login_screen.maxsize(width=700, height=500)
    login_screen.minsize(width=700, height=500)


    global e1
    global e2


    e1 = StringVar()
    e2 = StringVar()
    message=StringVar()


    loginname = Label(login_screen, text="USERNAME", font=("Sylfaen", 14), fg="BLACK", bg="white").place(x=400, y=140)
    e1=Entry(login_screen,bg="#db38c5", width=25)
    e1.place(x=400, y=170)


    loginpassword = Label(login_screen, text="PASSWORD", font=("Sylfaen", 14), fg="BLACK", bg="white").place(x=400, y=200)
    e2=Entry(login_screen, show="*", bg="#db38c5", width=25)
    e2.place(x=400, y=230)
    #this label i used for displaying the message of success failed or any error
    # Label(login_screen, text="", textvariable=message).place(x=170,y=240)

    login_btn=Button(login_screen, text="Login", command=login).place(x=400,y=300)



    login_screen.mainloop()

loginform()


