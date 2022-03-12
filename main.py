from stickman import HangmanGame
from os import system
from time import sleep

def new_game():

    word = input("Think of a word, phrase or sentance: ")
    print()
    while not all(c.isalpha() or c.isspace() for c in word) or not word:
        word = input("Please use only alphabet letters and spaces: ")
        print()

    hint = input("You can give a hint: ")

    system('cls')
    next_turn(word, hint)

def next_turn(word, hint):

    used = []
    used_all = []
    mistake = 0
    hangman = HangmanGame()

    word = list(word)
    hidden_word = ["_" if letter != " " else " " for letter in word]

    while mistake < 7:
        hangman.output(hint, hidden_word, used, mistake)

        guess = input("Enter your guess: ").lower()
        print()
        while guess in used_all or not guess.isalpha() or len(guess) > 1:
            guess = input("Please enter a letter that haven't been used: ").lower()
            print()
        used_all.extend(guess)

        indices = [i for i, letter in enumerate(word) if letter.lower() == guess]
        if indices:
            for i in indices:
                hidden_word[i] = word[i]

            if hidden_word == word:
                hangman.output(hint, hidden_word, used, mistake)
                print("Congrats! You won!\n")
                try_again()

        else:
            mistake += 1
            used.extend(guess)
        
    hangman.output(hint, hidden_word, used, mistake)
    try_again()
        
def try_again():

    again = input("Do you want to play again? (y/n): ").lower()
    print()

    if again == "y":
        system('cls')
        new_game()
        
    else:
        print("Have a good day!")
        sleep(2)
        quit()

if __name__ == "__main__":
    new_game()
