from tkinter import *
from datetime import date

def CalculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    result_label.config(text=f"{nameValue.get()}, your age is {age}", font=("Helvetica", 30))

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Age Calculator")

photo = PhotoImage(file=r"C:\Users\MORIS\Downloads\Documents\Age Calculator.png")
myimage = Label(image=photo)
myimage.pack(padx=15, pady=15)

Label(text="Name", font=("Helvetica", 23)).place(x=200, y=250)
Label(text="Year", font=("Helvetica", 23)).place(x=200, y=300)
Label(text="Month", font=("Helvetica", 23)).place(x=200, y=350)
Label(text="Day", font=("Helvetica", 23)).place(x=200, y=400)

nameValue = StringVar()
nameEntry = Entry(root, textvariable=nameValue, width=30, bd=3, font=("Helvetica", 20))
nameEntry.place(x=300, y=250)

yearEntry = Entry(root, width=30, bd=3, font=("Helvetica", 20))
yearEntry.place(x=300, y=300)

monthEntry = Entry(root, width=30, bd=3, font=("Helvetica", 20))
monthEntry.place(x=300, y=350)

dayEntry = Entry(root, width=30, bd=3, font=("Helvetica", 20))
dayEntry.place(x=300, y=400)

result_label = Label(root, text="", font=("Helvetica", 30))
result_label.place(x=300, y=500)

Button(text="Calculate age", font=("Helvetica", 20), bg="black", fg="white", width=11, height=2, command=CalculateAge).place(x=300, y=450)

root.mainloop()
