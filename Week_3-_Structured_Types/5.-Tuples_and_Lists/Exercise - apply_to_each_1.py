# Exercise: apply to each 1

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 2 minutes

# Here is the code for a function applyToEach:

# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

# Assume that
# testList = [1, -4, 8, -9]

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList
# has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated
# value. You may need to write a simple procedure in each question to help with this process.
#

# Your Code Here
def absolute(a):
    return abs(a)

applyToEach(testList, absolute)
# Correct
