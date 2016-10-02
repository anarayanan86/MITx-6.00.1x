# Exercise: fourth power

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 2 minutes

# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise exercise (you don't need to redefine square in this box;
# when you call square, the grader will use our definition).

# This function takes in one number and returns one number.


def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

# Correct
