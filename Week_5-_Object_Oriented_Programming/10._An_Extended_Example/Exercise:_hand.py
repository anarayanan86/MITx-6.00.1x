# Exercise: hand
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 14 minutes

# In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem
# Set 4. You'll then be asked to implement one of its methods. Note that the implementation of the object-oriented version of the hand
# is a bit different than how we did things with the functional implementation; pay close attention to doc strings and read through the
# implementation carefully.

# To begin: Download hand.py and read through the file. Be sure to understand what's going on in the file. Make a few instances of the
# Hand class, and play around with the existing methods.

# When you have completed reading through the file, implement the update method.

# Paste the entire Hand class in the box below.

# The __str__ method is this:

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output
        
# A more concise version of this code might be

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        for letter in sorted(self.hand.keys()):
            output += letter * self.hand[letter]
        return output
        
# Use whichever __str__ method you like. This will make sure the grading of the hand's display is consistent.

 

# Paste the entire Hand class in this box
class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.
 
        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}
 
        # Build the hand
        numVowels = self.HAND_SIZE // 3
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here
        word_letter_list = list(word)
        hand_letter_list = []
        for i in self.hand.keys():
            for j in range(self.hand[i]):
                hand_letter_list.append(i)
                
        def isValidWord(word):
            """
            Returns True if word is entirely composed of letters in the hand.
            Otherwise, returns False.

            Does not mutate hand or wordList.
   
            word: string
            hand: dictionary (string -> int)
            wordList: list of lowercase strings
            """
            # TO DO ... <-- Remove this comment when you code this function
            output = self.hand.copy()
            letter_check = set(list(word)) <= set(output.keys())
            for letter in word:
                if letter in output.keys():
                    output[letter] -= 1

            value_check = all(i >= 0 for i in output.values())    
            if letter_check == True and value_check == True:
                return True
            else:
                return False                
                
        
        if isValidWord(word) == True:
            output = self.hand.copy()
            for letter in word_letter_list:
                if letter in output.keys():
                    output[letter] -= 1
            self.hand = {k: output[k] for k in output if output[k] != 0}
            return True
        else:
            return False

# Correct
