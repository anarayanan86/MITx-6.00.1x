# Problem 8
# 20/20 points (graded)
# Implement a function that meets the specifications below.

# def applyF_filterG(L, f, g):
#    """
#    Assumes L is a list of integers
#    Assume functions f and g are defined for you. 
#    f takes in an integer, applies a function, returns another integer 
#    g takes in an integer, applies a Boolean function, 
#        returns either True or False
#    Mutates L such that, for each element i originally in L, L contains  
#        i if g(f(i)) returns True, and no other elements
#    Returns the largest element in the mutated L or -1 if the list is empty
#    """
#    # Your code here

# For example, the following functions, f, g, and test code:
# def f(i):
#     return i + 2
# def g(i):
#    return i > 5

# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))
# print(L)
# Should print:6
# [5, 6]

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own
# test cases.

 
# Paste your function here
def applyF_filterG(L, f, g):
    newL = []
    for i in L:
        if g(f(i)) == True:
            newL.append(i)
    L[:] = newL
    if len(L) == 0:
        return -1
    else:
        return max(L)

# Correct
