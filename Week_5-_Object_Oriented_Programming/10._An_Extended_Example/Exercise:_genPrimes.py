# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...



None
def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2

# Correct
