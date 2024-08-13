from tkinter import *
from tkinter import messagebox
import random

# To determine the computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissor"])

def submit():
    computer_choice = get_computer_choice()
    player_choice = var.get()

    # To determine the player's choice
    if player_choice == 1:
        player_choice_str = "Rock"
    elif player_choice == 2:
        player_choice_str = "Paper"
    elif player_choice == 3:
        player_choice_str = "Scissor"
    else:
        player_choice_str = None

    # To update the labels
    label1.config(text=f"Your Choice: {player_choice_str}")
    label2.config(text=f"Computer's Choice: {computer_choice}")

    # To determine the result
    if player_choice_str == computer_choice:
        label3.config(text="The Game Is Tie...")
    elif (player_choice_str == "Rock" and computer_choice == "Scissor") or \
         (player_choice_str == "Paper" and computer_choice == "Rock") or \
         (player_choice_str == "Scissor" and computer_choice == "Paper"):
        label3.config(text="You Win The Game...")
    elif (player_choice_str == "Scissor" and computer_choice == "Rock") or \
         (player_choice_str == "Rock" and computer_choice == "Paper") or \
         (player_choice_str == "Paper" and computer_choice == "Scissor"):
        label3.config(text="Computer Win The Game...")
    else:
        messagebox.showwarning("Warning","Please select a choice.")

    # To show the Play Again and Quit buttons
    play_again_button.grid(row=0, column=0, padx=10, pady=10)
    quit_button.grid(row=0, column=3, padx=10, pady=10)
    submit_button.grid_forget()  # Hide the submit button

def play_again():
    # To reset the selected choice
    var.set(0)
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")

    #To hide the Play Again and Quit buttons
    play_again_button.grid_forget()
    quit_button.grid_forget()
    
    #To show the submit button again
    submit_button.grid(row=1, column=1, pady=20)

def quit_game():
    root.destroy()

root = Tk()
root.geometry("500x450")
root.minsize(500,450)
root.maxsize(500,450)
root.config(bg="light blue")
root.title("Rock Paper Scissor - By Pawan")

title = Label(root, text="Rock Paper Scissor", font="forte 38 bold",bg="light blue",fg="white")
title.pack(fill=X,pady=10)

frame = Frame(root,bg="light blue")
frame.pack(pady=40)

var = IntVar()
rock_button = Radiobutton(frame, text="Rock", padx=14, variable=var, value=1, font="lucid 12 bold")
rock_button.grid(row=0, column=0)
paper_button = Radiobutton(frame, text="Paper", padx=14, variable=var, value=2, font="lucid 12 bold")
paper_button.grid(row=0, column=1)
scissor_button = Radiobutton(frame, text="Scissor", padx=14, variable=var, value=3, font="lucid 12 bold")
scissor_button.grid(row=0, column=2)

submit_button = Button(frame, text="Submit", command=submit,bg="light green")
submit_button.grid(row=1, column=1, pady=20)

#To create frame for Play Again and Quit buttons
frame1 = Frame(root,bg="light blue")
frame1.pack(side=BOTTOM, pady=20)

play_again_button = Button(frame1, text="Play Again", command=play_again,bg="yellow")
play_again_button.grid(row=0, column=0, padx=10, pady=10)
play_again_button.grid_forget() #To hide button initially

quit_button = Button(frame1, text="Quit", command=quit_game,bg="red")
quit_button.grid(row=0, column=3, padx=10, pady=10)
quit_button.grid_forget() #To hide button initially

#To create output frame
output_frame = Frame(root,bg="light blue")
output_frame.pack(pady=40)

#To create labels
label1 = Label(output_frame, text="",bg="light blue")
label1.pack()
label2 = Label(output_frame, text="",bg="light blue")
label2.pack()
label3 = Label(output_frame, text="",bg="light blue",font="lucid 12 bold")
label3.pack()

root.mainloop()
