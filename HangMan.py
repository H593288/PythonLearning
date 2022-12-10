#Hangman game
import random

#choose a secret word
words = ["bat", "mint", "cool", "easy", "games"]

#random from the list
word = random.choice(words)

#List of underscores same length as the word
blankline = ["_" for i in range(len(word))]

#number of incorrect guesses tp 0
incorrect_guesses = 0

#Loop that will run until the user guess it right or made too many incorrect guesses
while incorrect_guesses < 15:
    #Read the letter the user guess
    guess = input("Enter a letter: ")

    #Check if the letter was guessed right
    if guess in word:
    #if its correct > update hidden word with the correct letter
        for i in range(len(word)):
         if word[i] == guess:
            blankline[i] = guess

    if "_" not in blankline:

        print("Correct, the word was " + word)
        break
    else:
        #if guessed letter not in the word, increment with 1
         incorrect_guesses +=1

    #Show the current state of the hidden word and remaining incorrect guesses
    print("".join(blankline))
    print("Incorrect guesses remaining " + str(15 - incorrect_guesses))

#too many incorrect guesses > display message
if incorrect_guesses >= 15:
    print("You lose! The word was " + word)