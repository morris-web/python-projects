import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speak_now():
    engine.say(textv.get())
    engine.runAndWait()

root = Tk()
root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False, False)

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=("Helvetica", 12), bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(obj, text="Text", font=("Helvetica", 12))
lbl.pack(side=tk.LEFT, padx=5)

entry = Entry(obj, textvariable=textv, font=("Helvetica", 12), width=25, bd=5)
entry.pack(side=tk.LEFT, padx=10)

btn = Button(obj, text="Speak", font=("Helvetica", 12), bg="black", fg="white", command=speak_now)
btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
