import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        # Create widgets
        self.label = tk.Label(root, text="Guess a number between 1 and 100 Wanzwa here Natasha ")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("NKUTENDA PUMBA Invalid input", "Please enter a valid number")
            return

        self.attempts += 1

        if guess < self.target_number:
            self.result_label.config(text="Too low! Try again.Pumba Noku")
        elif guess > self.target_number:
            self.result_label.config(text="Too high! Try again Pumba Noku.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!Musoro wako ")
            self.reset_game()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()
