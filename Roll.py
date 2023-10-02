from tkinter import *
import random

root = Tk()
root.geometry("700x450")
root.title("Roll Dice")

label = Label(root, text="", font=("times", 260))

def roll():
    dice = ['\u2680', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')

button = Button(root, text="Let's roll....", width=40, height=5, font=("Helvetica", 10), bg="white", bd=2, command=roll)

label.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)

root.mainloop()
