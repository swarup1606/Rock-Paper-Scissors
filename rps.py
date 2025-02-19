## ROCK PAPER SCISSORS GAME ##

import tkinter as tk
from tkinter import messagebox
import random

# Creating functions
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

def play():
    global user_score, computer_score
    user_choice = user_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

    update_score(result)

def update_score(result):
    global user_score, computer_score
    if "win" in result.lower():
        user_score += 1
    elif "lose" in result.lower():
        computer_score += 1

    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("450x250") 

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# User's choice
user_var = tk.StringVar()

# Scores
user_score = 0
computer_score = 0

# Header label
header_label = tk.Label(root, text="Rock, Paper, Scissors", font=('Helvetica', 18), pady=10)
header_label.pack()

# User's choice label and radio buttons
choice_label = tk.Label(root, text="Choose your move:")
choice_label.pack()

for choice in choices:
    radio_button = tk.Radiobutton(root, text=choice, variable=user_var, value=choice)
    radio_button.pack()

# Score label
score_label = tk.Label(root, text="Score: You 0 - 0 Computer")
score_label.pack()

# Play button
play_button = tk.Button(root, text="Play", command=play, bg='#4CAF50', fg='white', padx=10, pady=5)
play_button.pack()

# Run the Tkinter event loop
root.mainloop()
