import random

word_list = ['banana', 'mango', 'orange', 'plantain', 'avocado-pear']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.word_guessed[i] = guess
            print("".join(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left")
            if self.num_lives < 1:
                print("You lose")
                return True
        return '_' not in self.word_guessed

    def ask_for_input(self):
        print("Hangman Game")
        print("Guess the word: " + "".join(self.word_guessed))

        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess.lower())
                if self.check_guess(guess):
                    print("Congratulations! You win!")
                    break

game = Hangman(word_list)
game.ask_for_input()
