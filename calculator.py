from tkinter import *

#To perform operation and getting values of buttons.
def click(event):
    global screenvalue
    text=event.widget.cget("text")
    if text=="=":
        if screenvalue.get().isdigit():
            value=int(screenvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                screenvalue.set("")
                screen.update()
        try:
            screenvalue.set(value)
            screen.update()
        except:
            pass
    elif text=="AC":
        screenvalue.set("")
        screen.update()
    elif text=="C":
        screenvalue.set("")
        screen.update()
    else:
        screenvalue.set(screenvalue.get()+text)
        screen.update()

#To create a GUI window
root=Tk()
root.geometry("330x433")
root.minsize(330,433)
root.maxsize(330,433)

#To give a title for window
root.title("Calculator - By Pawan")

title=Label(root,text="Calculator",font="comicsansms 18 bold",pady=10)
title.pack()

#To create a screen to take input
screenvalue=StringVar()
screenvalue.set("")
screen=Entry(root,textvariable=screenvalue,font="lucid 20 bold")
screen.pack(fill=X,ipady=52,pady=10)

button_frame=Frame(root,bg="grey")
button_frame.pack(side=BOTTOM,fill=X)


#To create buttons
x=["AC",'%','C','/','7','8','9','*','4','5','6','-','1','2','3','+',"00",'0','.','=']
for i in range(5):
    for j in range(4):
        index=i*4+j
        if index<len(x):
            label=x[index]
            b=Button(button_frame,text=label,font="lucid 15 bold")
            b.grid(row=i,column=j,sticky="nsew",padx=1,pady=1)
            b.bind("<Button-1>",click)

#To expand buttons properly
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    button_frame.grid_columnconfigure(j, weight=1)

root.mainloop()