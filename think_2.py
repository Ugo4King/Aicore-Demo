import random
import tkinter as tk

# define a list of random words
words = ["python", "programming", "computer", "algorithm", "function", "syntax"]

# Ask for the ASCII arts for the hangman
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

# define a function that chooses a random word from the list
def choose_word():
    return random.choice(words)

def update_hangman(mistake):
    hangman_label.config(text=hangman_art[mistake])

def check_guess():
    global word_with_blank
    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_with_blank = word_with_blank[:i] + guess + word_with_blank[i+1:]
        
        word_label.config(text=word_with_blank)
        
        if word_with_blank == word:  # Check if all letters have been guessed correctly
            end_game("Win")
    else:
        global mistake
        mistake += 1
        update_hangman(mistake)
        
        if mistake == 6:
            end_game("Lose")

    update_hangman(mistake)  # Update hangman art after checking guess

def end_game(result):
    if result == "Win":
        result_text = "You Win!"
    else:
        result_text = "You Lose, the word was " + word
    
    result_label.config(text=result_text)
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

root = tk.Tk()
root.title("Hangman Game")

hangman_label = tk.Label(root, font=("Courier", 20))
hangman_label.grid(row=0, column=0)

word = choose_word()
word_with_blank = "-" * len(word)
word_label = tk.Label(root, text=word_with_blank, font=("Arial", 24))
word_label.grid(row=1, column=0)

guess_entry = tk.Entry(root, width=3, font=("Arial", 24))
guess_entry.grid(row=2, column=0)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.grid(row=2, column=1)

result_label = tk.Label(root, font=("Arial", 24))
result_label.grid(row=3, column=0)

mistake = 0
update_hangman(mistake)

root.mainloop()