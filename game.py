import tkinter as tk
from tkinter import messagebox
import random


def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"Computer chooses {computer_choice}. {result}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"


root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(background="lightblue")  


def button_click(choice):
    play_game(choice)


rock_btn = tk.Button(root, text="Rock", width=20, command=lambda: button_click("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=20, command=lambda: button_click("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=20, command=lambda: button_click("Scissors"))
scissors_btn.pack(pady=5)


root.mainloop()
