from tkinter import *
from tkinter import messagebox
import random
import string

def generate():
    try:
        length = int(uservalue.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Please enter a valid length")
            return

        characters = ""
        if digitvalue.get() == 1:
            characters += string.digits
        if smallvalue.get() == 1:
            characters += string.ascii_lowercase
        if capitalvalue.get() == 1:
            characters += string.ascii_uppercase
        if symbolvalue.get() == 1:
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character type")
            return

        password = "".join(random.choice(characters) for i in range(length))
        output_label.config(text=password)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number")
        uservalue.set("")

root = Tk()
root.geometry("500x450")
root.minsize(500, 450)
root.maxsize(500, 450)
root.title("Password Generator - By Pawan")
root.config(bg="rosybrown3")

title = Label(root, text="Password Generator", font="forte 38 bold", bg="rosybrown3", fg="white")
title.pack(fill=X)

screen = Frame(root,bg="rosybrown3")
screen.pack(pady=10)

uservalue = StringVar()
digitvalue = IntVar()
capitalvalue = IntVar()
smallvalue = IntVar()
symbolvalue = IntVar()

entrylabel = Label(screen, text="Enter the length of password",bg="rosybrown3")
entrylabel.grid(row=0, column=0, pady=2)

userentry = Entry(screen, textvariable=uservalue,font="lucid 10 bold")
userentry.grid(row=1, column=0)

digitentry = Checkbutton(screen, text="Add digits in password", variable=digitvalue,bg="rosybrown3")
digitentry.grid(row=2, column=0, pady=10)

capitalentry = Checkbutton(screen, text="Add capital letters in password", variable=capitalvalue,bg="rosybrown3")
capitalentry.grid(row=3, column=0, pady=10)

smallentry = Checkbutton(screen, text="Add small letters in password", variable=smallvalue,bg="rosybrown3")
smallentry.grid(row=4, column=0, pady=10)

symbolentry = Checkbutton(screen, text="Add symbols in password", variable=symbolvalue,bg="rosybrown3")
symbolentry.grid(row=5, column=0, pady=10)

button = Button(screen, text="Generate", command=generate)
button.grid(row=6, column=0)

output_frame = Frame(root)
output_frame.pack()

output_label = Label(output_frame, text="", font="Arial 15", bg="aqua")
output_label.pack()

root.mainloop()
