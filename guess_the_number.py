import tkinter as tk
import random
from pyvirtualdisplay import Display
from PIL import ImageGrab

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        
        self.target_number = random.randint(1, 100)
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack()
        
        self.feedback = tk.Label(root, text="")
        self.feedback.pack()
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < self.target_number:
                self.feedback.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.feedback.config(text="Too high! Try again.")
            else:
                self.feedback.config(text="Correct! You guessed the number.")
        except ValueError:
            self.feedback.config(text="Please enter a valid number.")

if __name__ == "__main__":
    display = Display(visible=0, size=(800, 600))
    display.start()
    
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    
    root.update()
    root.after(1000, lambda: ImageGrab.grab().save("screenshot.png"))
    root.mainloop()
    
    display.stop()
