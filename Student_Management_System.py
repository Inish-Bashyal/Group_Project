from tkinter import *
from tkinter import messagebox, ttk
#from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Student Management System")
# root.geometry("1400x800")
root.maxsize(width=1400, height=800)
root.minsize(width=1400, height=800)

conn = sqlite3.connect("management.db")
c = conn.cursor()

# creating tables
#
# c.execute("""CREATE TABLE entries(
# first_name text,
# last_name text,
# username text,
# date_of_birth text,
# age integer,
# gender text,
# address text,
# phone_number integer,
# school text,
# score text
# )""")
# print("Table Successfully Created")


# creating labels and entries


first = Label(root, text="FIRST NAME", bg="#021524", fg="white").place(x=500, y=180)
first_name = Entry(root)
first_name.place(x=650,y=177)

last = Label(root, text="LAST NAME", bg="#021524", fg="white").place(x=900, y=180)
last_name = Entry(root)
last_name.place(x=1020, y=177)

user = Label(root, text="USERNAME", bg="#021524", fg="white").place(x=500, y=230)
username = Entry(root)
username.place(x=650, y=227)

months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December"
]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
mon = StringVar()
dy = StringVar()
yer = StringVar()

dob = Label(root, text="DATE OF BIRTH", bg="#021524", fg="white").place(x=900, y=230)
month = ttk.Combobox(root, textvariable=mon, width=9)
month.place(x=1020, y=230)
month['values']= months


day = ttk.Combobox(root, textvariable=dy, width=3)
day.place(x=1130, y=230)
day['values']=days


year = ttk.Combobox(root, textvariable=yer, width=4)
year.place(x=1190, y=230)
year['values']=years


agee = Label(root, text="AGE", bg="#021524", fg="white").place(x=500,y=280)
age = Entry(root)
age.place(x=650, y=277)

g = StringVar()
g.get()
gen = Label(root, text="GENDER", bg="#021524", fg="white").place(x=900, y=280)
r1 = Radiobutton(root, text="Male", variable=g, value="M", bg="#021524", fg="white")
r2 = Radiobutton(root, text="Female", variable=g, value="F", bg="#021524", fg="white")
r1.place(x=1050, y=280)
r2.place(x=1120 , y=280)

addrs = Label(root, text="ADDRESS", bg="#021524", fg="white").place(x=500, y=330)
address = Entry(root)
address.place(x=650, y=327)

phone = Label(root, text="PHONE NUMBER", bg="#021524", fg="white").place(x=900, y=330)
phone_number = Entry(root)
phone_number.place(x=1020, y=327)

previousschool = Label(root, text="PREVIOUS COLLEGE", bg="#021524", fg="white").place(x=500, y=380)
school = Entry(root)
school.place(x=650 ,y=377)

marks = Label(root, text="GPA", bg="#021524", fg="white").place(x=900, y=380)
score = Entry(root)
score.place(x=1020, y=377)

def submit():
    conn = sqlite3.connect("management.db")
    c = conn.cursor()


    c.execute("INSERT INTO entries VALUES(:first_name, :last_name, :username, :date_of_birth, :age, :gender, :address,"
              " :phone_number, :school, :score)", {
                  "first_name": first_name.get(),
                  "last_name": last_name.get(),
                  "username": username.get(),
                  "date_of_birth": mon.get() + "/" + dy.get() + "/" + yer.get(),
                  "age": age.get(),
                  "gender": g.get(),
                  "address": address.get(),
                  "phone_number": phone_number.get(),
                  "school": school.get(),
                  "score": score.get()
              })



    first_name.delete(0, END)
    last_name.delete(0, END)
    username.delete(0, END)
    # date_of_birth.delete(0, END)
    age.delete(0, END)
    # g.delete(0, END)
    address.delete(0, END)
    phone_number.delete(0, END)
    school.delete(0, END)
    score.delete(0, END)

    messagebox.showinfo("Success", "Data added successfully")

    conn.commit()
    conn.close()
# submit and query button
submit_button = Button(root, text="submit", command=submit).place(x=560 , y=440)


conn.commit()
conn.close()

root.mainloop()