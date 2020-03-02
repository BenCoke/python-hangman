'''Game of hangman played from the command line.'''
#Read word options from file and make a list of possible choices
file = open('animals.txt', 'r')
wordList = file.read().split(', ')

import random
import re
def hangman():
    #Setup: Choose a word, keep track of guesses, keep track of mistakes
    wordToGuess = random.choice(wordList)
    guessedLetters = ""
    mistakes = 0

    print("Welcome to hangman!")
    while mistakes < 6:
        #The word showing player progress. Composed of guessed letters and * characters.
        #Built by comparing the word to be guessed and the guessed letters 
        wordShow = ""
        for letter in wordToGuess:
            if letter in guessedLetters:
                wordShow += letter
            else:
                wordShow += "*"
        #Break condition for correctly guessing the word
        if wordShow == wordToGuess:
            print("Congratulations you guessed correctly your word was: " + wordShow)
            break
        #Updates for player
        print("\n" + wordShow + " is your word.")
        if len(guessedLetters) > 0: print("You have guessed the letters: " + guessedLetters)
        if mistakes == 1: print("You have made " + str(mistakes) + " mistake.")
        if mistakes > 1: print("You have made " + str(mistakes) + " mistakes.")
        #Asks for a single letter guess, checks that the response is a-z, - or a space
        guess = input("What letter would you like to guess?\n").lower()
        print("--------------------------------------")
        while (len(guess) != 1) or (not re.match("^[a-z -]*$", guess)) or (guess in guessedLetters):
            if (len(guess) != 1):
                guess = input("Your guess must be a single letter. Please guess again.\n")
            if (not re.match("^[a-z -]*$", guess)):
                guess = input("Your guess must be a letter from a to z. Please guess again.\n")
            if guess in guessedLetters:
                guess = input("You have already guessed that letter. Please guess again.\n")
        #Counts mistakes and informs player a mistake has been made
        if guess not in wordToGuess:
            mistakes += 1
            print("Sorry, that letter is not in your word.")
        #Draws a hangman based on mistakes made
        if mistakes >= 1: print(" O")
        if mistakes == 2: print(" |")
        if mistakes == 3: print("/|")
        if mistakes >= 4: print("/|\\")
        if mistakes == 5: print("/")
        if mistakes == 6: print("/ \\")
        if mistakes == 6: print("\n6 mistakes! You lose! Your word was: " + wordToGuess)
        guessedLetters += guess
    playAgain = input("Would you like to play again?(y/n)\n")
    if playAgain == "y": hangman()

hangman()

file.close()