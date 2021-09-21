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
month.current(0)

day = ttk.Combobox(root, textvariable=dy, width=3)
day.place(x=1130, y=230)
day['values']=days
day.current(0)

year = ttk.Combobox(root, textvariable=yer, width=4)
year.place(x=1190, y=230)
year['values']=years
year.current(0)

agee = Label(root, text="AGE", bg="#021524", fg="white").place(x=500,y=280)
age = Entry(root)
age.place(x=650, y=277)

g = StringVar()
g.get()
gen = Label(root, text="GENDER", bg="#021524", fg="white").place(x=900, y=280)
r1 = Radiobutton(root, text="Male", variable=g, value="M", bg="#021524", fg="white")
r2 = Radiobutton(root, text="Female", variable=g, value="F", bg="#021524", fg="white")
r1.place(x=1020, y=280)
r2.place(x=1090 , y=280)

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

# delete entry and label
deletebox = Label(root, text='DELETE/UPDATE' ,bg="#052b36", fg="white").place(x=440, y=560)
delete_box = Entry(root, width=25)
delete_box.place(x=570, y=557)


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

def update():
    global gsecond
    conn = sqlite3.connect("management.db")
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE entries SET
    first_name = :frst ,
    last_name = :lst,
    username = :usr,
    date_of_birth = :dobsecond,
    age = :agesecond,
    gender = :gensecond,
    address = :addrsecond,
    phone_number = :phonesecond,
    school = :schoolsecond,
    score = :scoresecond
    WHERE oid = :oid""", {
        'frst': first_name_editor.get(),
        'lst': last_name_editor.get(),
        'usr': username_editor.get(),
        'dobsecond': monthsecond.get() + "/" + daysecond.get() + "/" + yearsecond.get(),
        'agesecond': age_editor.get(),
        'gensecond': gsecond.get(),
        'addrsecond': address_editor.get(),
        'phonesecond': phone_number_editor.get(),
        'schoolsecond': school_editor.get(),
        'scoresecond': score_editor.get(),
        'oid': record_id

    })
    messagebox.showinfo("Success", "Data successfully modified")
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update Data")

    conn = sqlite3.connect("management.db")
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * from entries WHERE oid =" + record_id)

    records = c.fetchall()

    global first_name_editor
    global last_name_editor
    global username_editor
    global age_editor
    global address_editor
    global phone_number_editor
    global school_editor
    global score_editor
    global gsecond
    global daysecond
    global yearsecond
    global monthsecond

    # creating labels and entries for update window

    firsttt = Label(editor, text="FIRST NAME").grid(row=1, column=0, pady=20)
    first_name_editor = Entry(editor)
    first_name_editor.grid(row=1, column=1, pady=20)

    lasttt = Label(editor, text="LAST NAME").grid(row=1, column=2, pady=20)
    last_name_editor = Entry(editor)
    last_name_editor.grid(row=1, column=3, pady=20)

    userrr = Label(editor, text="USERNAME").grid(row=2, column=0, pady=20)
    username_editor = Entry(editor)
    username_editor.grid(row=2, column=1, pady=20)

    dobbbb = Label(editor, text="DATE OF BIRTH").grid(row=2, column=2, pady=20)
    monthsecond = StringVar()
    daysecond = StringVar()
    yearsecond = StringVar()

    monthsecond = ttk.Combobox(editor, textvariable=mon, width=9)
    monthsecond['values'] = months
    monthsecond.current(0)
    monthsecond.grid(row=2, column=3)

    daysecond = ttk.Combobox(editor, textvariable=dy, width=3)
    daysecond['values'] = days
    daysecond.current(0)
    daysecond.grid(row=2, column=4)

    yearsecond = ttk.Combobox(editor, textvariable=yer, width=4)
    yearsecond['values'] = years
    yearsecond.current(0)
    yearsecond.grid(row=2, column=5)


    ageeeee = Label(editor, text="AGE").grid(row=3, column=0, pady=20)
    age_editor = Entry(editor)
    age_editor.grid(row=3, column=1, pady=20)

    gennnn = Label(editor, text="GENDER").grid(row=3, column=2, pady=20)

    gs= StringVar()
    # gs.get()

    gsecond = ttk.Combobox(editor, textvariable=gs, width=7)
    gsecond['values'] = ["MALE","FEMALE"]
    gsecond.current(0)
    gsecond.grid(row=3, column=3)

    # r11 = Radiobutton(editor, text="Male", variable=gsecond, value="M")
    # r22 = Radiobutton(editor, text="Female", variable=gsecond, value="F")
    # r11.grid(row=3, column=3)
    # r22.grid(row=3, column=4)

    addrsss = Label(editor, text="ADDRESS").grid(row=4, column=0, pady=20)
    address_editor = Entry(editor)
    address_editor.grid(row=4, column=1, pady=20)

    phoneee = Label(editor, text="PHONE NUMBER").grid(row=4, column=2, pady=20)
    phone_number_editor = Entry(editor)
    phone_number_editor.grid(row=4, column=3, pady=20)

    previousschoolll = Label(editor, text="PREVIOUS COLLEGE").grid(row=5, column=0, pady=20)
    school_editor = Entry(editor)
    school_editor.grid(row=5, column=1, pady=20)

    marksss = Label(editor, text="GPA").grid(row=5, column=2, pady=20)
    score_editor = Entry(editor)
    score_editor.grid(row=5, column=3, pady=20)

    for record in records:
        first_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        username_editor.insert(0, record[2])
        # date_of_birth_editor.insert(0, record[3])
        age_editor.insert(0, record[4])
        # gender_editor.insert(0, record[5])
        address_editor.insert(0, record[6])
        phone_number_editor.insert(0, record[7])
        school_editor.insert(0, record[8])
        score_editor.insert(0, record[9])

        edit_btn = Button(editor, text="SAVE", command=update).grid(row=7, column=2, pady=20)

# submit and query button
submit_button = Button(root, text="submit", command=submit).place(x=560 , y=440)

#update buttion
update_btn = Button(root, text="Update", command=edit).place(x=690, y=605)

conn.commit()
conn.close()

root.mainloop()