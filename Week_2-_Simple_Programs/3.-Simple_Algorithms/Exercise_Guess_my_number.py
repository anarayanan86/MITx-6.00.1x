# Exercise: guess my number

# (10/10 points)
# ESTIMATED TIME TO COMPLETE: 15 minutes

# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes
# guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret
# number!

# Here is a transcript of an example session:

# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 81?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 84?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
# Is your secret number 82?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83

# Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or
# c.

# When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then,
# you should re-ask the question, and prompt again for input. For example:

# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
# Sorry, I did not understand your input.
# Is your secret number 91?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c


# Paste your code into this box
low = 0
high = 100
print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')

# Correct
