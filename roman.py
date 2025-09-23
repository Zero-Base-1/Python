"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""

import random
import tkinter as tk
from tkinter import ttk

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
# Add ties counter and rounds history
ties_count = 0
rounds = []

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "player"
    return "computer"

def play(player_choice):
    global player_score, computer_score, ties_count, rounds
    computer = random.choice(choices)
    result = decide_winner(player_choice, computer)

    if result == "tie":
        ties_count += 1
        result_text = "It's a tie!"
    elif result == "player":
        player_score += 1
        result_text = "You win!"
    else:
        computer_score += 1
        result_text = "Computer wins!"

    computer_label.config(text=f"Computer chose: {computer}")
    result_label.config(text=result_text)

    # Record round and insert into history view
    round_num = len(rounds) + 1
    rounds.append({'round': round_num, 'player': player_choice, 'computer': computer, 'result': result})
    history.insert('', 'end', values=(round_num, player_choice.title(), computer.title(), result_text))

    # Update the detailed count labels
    player_count_label.config(text=f"You: {player_score}")
    computer_count_label.config(text=f"Computer: {computer_score}")
    ties_count_label.config(text=f"Ties: {ties_count}")

def on_quit():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Labels
title_label = ttk.Label(mainframe, text="Choose Rock, Paper, or Scissors", font=("Segoe UI", 14))
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 12))

computer_label = ttk.Label(mainframe, text="Computer chose: -")
computer_label.grid(row=1, column=0, columnspan=3)

result_label = ttk.Label(mainframe, text="Make your move", font=("Segoe UI", 12))
result_label.grid(row=2, column=0, columnspan=3, pady=(6, 6))

# Detailed count labels (replaces previous score_label)
scoreboard_frame = ttk.Frame(mainframe)
scoreboard_frame.grid(row=3, column=0, columnspan=3, pady=(0, 12))

player_count_label = ttk.Label(scoreboard_frame, text=f"You: {player_score}", width=16)
player_count_label.grid(row=0, column=0)

ties_count_label = ttk.Label(scoreboard_frame, text=f"Ties: {ties_count}", width=16)
ties_count_label.grid(row=0, column=1)

computer_count_label = ttk.Label(scoreboard_frame, text=f"Computer: {computer_score}", width=16)
computer_count_label.grid(row=0, column=2)

# Buttons
rock_btn = ttk.Button(mainframe, text="Rock", width=12, command=lambda: play('rock'))
rock_btn.grid(row=4, column=0, padx=4, pady=4)

paper_btn = ttk.Button(mainframe, text="Paper", width=12, command=lambda: play('paper'))
paper_btn.grid(row=4, column=1, padx=4, pady=4)

scissors_btn = ttk.Button(mainframe, text="Scissors", width=12, command=lambda: play('scissors'))
scissors_btn.grid(row=4, column=2, padx=4, pady=4)

# Add round history (detailed scoreboard)
history_label = ttk.Label(mainframe, text="Round History", font=("Segoe UI", 11))
history_label.grid(row=5, column=0, columnspan=3, pady=(8, 0))

columns = ('round', 'player', 'computer', 'result')
history = ttk.Treeview(mainframe, columns=columns, show='headings', height=8)
history.heading('round', text='Round')
history.heading('player', text='Player')
history.heading('computer', text='Computer')
history.heading('result', text='Result')
history.column('round', width=60, anchor='center')
history.column('player', width=100, anchor='center')
history.column('computer', width=100, anchor='center')
history.column('result', width=140, anchor='center')
history.grid(row=6, column=0, columnspan=3, pady=(4, 8), sticky=(tk.W, tk.E))

# Optional vertical scrollbar for history
vsb = ttk.Scrollbar(mainframe, orient="vertical", command=history.yview)
history.configure(yscrollcommand=vsb.set)
vsb.grid(row=6, column=3, sticky=(tk.N, tk.S))

quit_btn = ttk.Button(mainframe, text="Quit", command=on_quit)
quit_btn.grid(row=7, column=0, columnspan=3, pady=(0, 0))

# Keyboard bindings
def handle_key(event):
    key = event.char.lower()
    if key == 'r':
        play('rock')
    elif key == 'p':
        play('paper')
    elif key == 's':
        play('scissors')
    elif key == 'q':
        on_quit()

root.bind('<Key>', handle_key)

# Start the GUI
root.mainloop()

