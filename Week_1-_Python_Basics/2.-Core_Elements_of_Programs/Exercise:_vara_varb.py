# Exercise: vara varb

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# Assume that two variables, varA and varB, are assigned values, either numbers or strings.

# Write a piece of Python code that prints out one of the following messages:
# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

None
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')
