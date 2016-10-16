# Problem 4 - The Game

# (15/15 points)
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an
# interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions,
# isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a
# random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When
# you enter in your solution in the tutor, you only need to give your hangman function.

# Consider using lower() to convert user input to lower case. For example:
# guess = 'A'
# guessInLowerCase = guess.lower()
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:
# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed
# from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've
# already guessed that - so try again!).

# Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to
# paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the
# problem. If you use additional helper functions, you will need to paste those definitions here.

# Your function should include calls to input to get the user's guess.


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue

# Correct
