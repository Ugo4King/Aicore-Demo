import random

class HangmanGame:
    def __init__(self):
        self.words = ["python", "programming", "computer", "algorithm", "function", "syntax"]
        self.hangman_art = [
            "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
            "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
        ]
        self.word = ""
        self.word_with_blank = ""
        self.mistake = 0
        self.game_won = False
        self.game_ended = False
        self.guessed_letters = set()

    def choose_word(self):
        self.word = random.choice(self.words)
        self.word_with_blank = "-" * len(self.word)

    def update_hangman(self):
        print(self.hangman_art[self.mistake])

    def check_guess(self, guess):
        if self.game_ended:
            return

        if guess in self.guessed_letters:
            print("You have guessed this letter before!")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_with_blank = self.word_with_blank[:i] + guess + self.word_with_blank[i+1:]

            print("Correct guess!")
            print("Word: " + self.word_with_blank)

            if self.word_with_blank == self.word:
                self.game_won = True
                self.end_game("Win")
                self.game_ended = True
        else:
            self.mistake += 1
            print("Wrong guess!")
            self.update_hangman()

            if self.mistake == 6:
                self.end_game("Lose")
                self.game_ended = True

    def end_game(self, result):
        if result == "Win":
            print("Congratulations! You Win!")
        else:
            print("Sorry, You Lose. The word was " + self.word)

    def play(self):
        print("Hangman Game")
        self.choose_word()
        self.update_hangman()
        print("Guess the word: " + self.word_with_blank)

        while not self.game_ended:
            guess = input("Enter your guess: ")
            self.check_guess(guess)

game = HangmanGame()
game.play()
