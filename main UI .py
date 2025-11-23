import tkinter as tk
from tkinter import messagebox

# 🌈 Create window
root = tk.Tk()
root.title("Moy Goodyukin Tic Tac Toe")
root.configure(bg="#ffe4b5")  # light peach background

# Global variables
turn = True  # True = X's turn, False = O's turn
board = [""] * 9

# Winning combos
wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

# Button click handler
def click(pos):
    global turn
    if board[pos] == "":
        board[pos] = "X" if turn else "O"
        buttons[pos].config(text=board[pos], fg="#2f4f4f", bg="#add8e6" if turn else "#90ee90")
        buttons[pos]["state"] = "disabled"

        if check_win():
            messagebox.showinfo("✨ Game Over ✨", f"{board[pos]} wins! 🎉")
            reset()
        elif "" not in board:
            messagebox.showinfo("😐 Game Over", "It's a draw! 🤝")
            reset()
        else:
            turn = not turn

# Check for a winner
def check_win():
    for win in wins:
        a, b, c = win
        if board[a] == board[b] == board[c] and board[a] != "":
            return True
    return False

# Reset game
def reset():
    global turn, board
    board = [""] * 9
    turn = True
    for btn in buttons:
        btn.config(text="", state="normal", bg="#f0f0f0")

# 🔘 Create 9 buttons in a grid
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Comic Sans MS", 20, "bold"),
                    width=5, height=2, command=lambda i=i: click(i), bg="#f0f0f0")
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Run the app
root.mainloop()
