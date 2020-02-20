'''Game of hangman played from the command line.'''
#Make method to read options from file
wordList = ["cat","cow","dog","horse"]

import random
import re
def hangman():
    #Setup: Choose a word, keep track of guesses, keep track of mistakes
    wordToGuess = random.choice(wordList)
    guessedLetters = "" #Make method to show guessed letters
    mistakes = 0

    print("Welcome to hangman!")
    while mistakes < 6:
	    #The word shown to show player progress. Composed of guessed letters and to be guessed letters.
	    #Built by comparing the word to be guessed and the guessed letters 
	    wordShow = ""
	    for letter in wordToGuess:
		    if letter in guessedLetters:
			    wordShow += letter
		    else:
			    wordShow += "*" #could be _, ?, or * depending on appearance
	    #Break condition for correctly guessing the word
	    if wordShow == wordToGuess:
		    print("Congratulations you correctly guessed your word was: " + wordShow)
		    break
	    print(wordShow + " is your word.")
	    #Asks for a single letter guess, checks that it's obeyed
	    guess = input("What letter would you like to guess?\n").lower()
	    while (len(guess) != 1) or (not re.match("^[a-z]*$", guess)):
	        guess = input("Your guess must be a single letter from a to z. Please guess again.\n")
	    #Counts mistakes and breaks if they reach 6
	    #Consider drawing a graphic using O | / \ 
	    if guess not in wordToGuess:
	        mistakes += 1
	        print("Sorry, that letter is not in your word.")
	        #print(" O") print as much as needed based on mistakes = 1,2,3,4,5,6
		    #print("/|\\")
		    #print("/ \\")
	    if mistakes == 6:
	        print("6 mistakes! You lose! Your word was: " + wordToGuess)
	    guessedLetters += guess
	    
hangman()