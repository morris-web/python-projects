from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Blank Not Allowed")

    elif username == "Parvat" and password == "admin":
        messagebox.showinfo("", "Login successful")

    else:
        messagebox.showinfo("", "Incorrect username or password")

root = Tk()
root.title('Login')
root.geometry("300x200")

entry1 = Entry(root, bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(root, bd=5, show="*")  # Use 'show' to hide the password
entry2.place(x=140, y=70)

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120)

root.mainloop()
