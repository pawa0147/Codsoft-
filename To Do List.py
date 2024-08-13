from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
tasks=[]

#To quit the application
def quitapp():
    root.destroy()

#To show about
def about():
    showinfo("To Do List","To Do List by Pawan")

#To show task
def show_task():
    global tasks
    listbox.delete(0,END)
    for i,task in enumerate(tasks,1):
        listbox.insert(END,f"{i}. {task}")

#To add the task
def add_task():
    user=userentry.get()
    if user:
        tasks.append(user)
        userentry.delete(0,END)
        show_task()
    else:
        messagebox.showwarning("Warning","Please enter something")

#To update the task
def update_task():
    try:
        selected_task=listbox.curselection()[0]
        new_task=userentry.get()
        if new_task:
            tasks[selected_task]=new_task
            userentry.delete(0,END)
            show_task()
        else:
            messagebox.showwarning("Warning", "Please enter a new task")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update")

#To delete the task
def delete_task():
    try:
        selected_task=listbox.curselection()[0]
        del tasks[selected_task]
        show_task()
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to delete")

#To delete all tasks
def delete_all():
    try:
        for i in range(len(tasks)):
            del tasks[i]
        show_task()
    except:
        pass

#To create interface
root= Tk()
root.geometry("330x433")
root.minsize(340,433)
root.maxsize(340,433)
root.title("To Do List")
root.configure(bg="light blue")

#To create menu bar
menubar=Menu(root)

#To create a file menu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Quit",command=quitapp)
root.config(menu=menubar)
menubar.add_cascade(label="Files",menu=filemenu)

#To create help menu
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

label=Label(root,text="To Do List",font="lucid 15 bold",bg="light blue").pack(pady=10)
#To create frame for Tasks
frame=Frame(root,bg="grey")
frame.pack(padx=10,pady=10)

#To add scrollbar to listbox
scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)

#To add listbox for tasks
listbox=Listbox(frame,width=52,height=10,yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH,padx=2,pady=2)
scrollbar.config(command=listbox.yview)

#To get input from user
userlabel=Label(root,text="Enter something",pady=20,font="bold")
userlabel.pack()
entryframe=Frame(root,bg="grey")
entryframe.pack(padx=10,pady=10)
userentry=Entry(entryframe,width=50)
userentry.pack(padx=2,pady=2,side=LEFT)

#To create frame for buttons
buttonframe=Frame(root,bg="grey")
buttonframe.pack(side=BOTTOM,pady=10,padx=10)

#To add buttons
addbutton=Button(buttonframe,text="Add Task",command=add_task)
addbutton.grid(row=0,column=0,padx=5,pady=5)

updatebutton=Button(buttonframe,text="Update Task",command=update_task)
updatebutton.grid(row=0,column=1,padx=5,pady=5)

deletebutton=Button(buttonframe,text="Delete Task",command=delete_task)
deletebutton.grid(row=0,column=2,padx=5,pady=5)

deleteallbutton=Button(buttonframe,text="Delete All",command=delete_all)
deleteallbutton.grid(row=0,column=3,padx=5,pady=5)

root.mainloop()
