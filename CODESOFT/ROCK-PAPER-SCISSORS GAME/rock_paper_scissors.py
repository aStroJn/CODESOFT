import tkinter as tk
import random

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x500")
window.config(bg="#2C3E50")

# Global variables for score tracking
user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

# Game logic function
def play_game(user_choice):
    global user_score, computer_score
    
    # Get computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
    
    # Update the display
    computer_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Reset game function
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score: You 0 - 0 Computer")
    computer_label.config(text="Computer chose: Waiting...")
    result_label.config(text="Make your choice!")

# Create GUI widgets
title_label = tk.Label(window, text="Rock Paper Scissors", 
                       font=("Arial", 24, "bold"), 
                       bg="#2C3E50", fg="white")
title_label.pack(pady=20)

instruction_label = tk.Label(window, text="Choose your move:", 
                            font=("Arial", 14), 
                            bg="#2C3E50", fg="white")
instruction_label.pack(pady=10)

# Button frame for better layout
button_frame = tk.Frame(window, bg="#2C3E50")
button_frame.pack(pady=20)

# Create choice buttons with styling
rock_button = tk.Button(button_frame, text="🪨 Rock", 
                       font=("Arial", 12, "bold"),
                       bg="#E74C3C", fg="white",
                       width=10, height=2,
                       command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="📄 Paper", 
                        font=("Arial", 12, "bold"),
                        bg="#3498DB", fg="white",
                        width=10, height=2,
                        command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", 
                           font=("Arial", 12, "bold"),
                           bg="#2ECC71", fg="white",
                           width=10, height=2,
                           command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Result display labels
computer_label = tk.Label(window, text="Computer chose: Waiting...", 
                         font=("Arial", 12), 
                         bg="#2C3E50", fg="white")
computer_label.pack(pady=15)

result_label = tk.Label(window, text="Make your choice!", 
                       font=("Arial", 16, "bold"), 
                       bg="#2C3E50", fg="#F39C12")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score: You 0 - 0 Computer", 
                      font=("Arial", 14), 
                      bg="#2C3E50", fg="white")
score_label.pack(pady=15)

# Reset button
reset_button = tk.Button(window, text="🔄 Reset Game", 
                        font=("Arial", 12, "bold"),
                        bg="#95A5A6", fg="white",
                        width=15, height=2,
                        command=reset_game)
reset_button.pack(pady=20)

# Start the main event loop
window.mainloop()