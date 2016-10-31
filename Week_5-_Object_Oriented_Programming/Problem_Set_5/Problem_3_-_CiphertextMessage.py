# Problem 3 - CiphertextMessage
# 15/15 points (graded)
# For this problem, the graders will use our implementation of the Message and PlaintextMessage classes, so don't worry if you did not get
# the previous parts correct.

# Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial. If message is the encrypted
# message, and s is the shift used to encrypt the message, then apply_shift(message, 26-s) gives you the original plaintext message. Do you
# see why?

# The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift!
# We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes the number of
# English words in the decoded message, we can decrypt their cipher! A simple indication of whether or not the correct shift has been found
# is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual
# words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various
# strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

# Fill in the methods in the class CiphertextMessage acording to the specifications in ps6.py. The methods you should fill in are:
# __init__(self, text): Use the parent class constructor to make your code more concise.
# decrypt_message(self): You may find the helper function is_word(wordlist, word) and the string method split() useful. Note that is_word
# will ignore punctuation and other special characters when considering whether a word is valid.

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_counter = 0
        max_count = 0
        for i in range(26):
            for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                if is_word(self.valid_words, j):
                    word_counter += 1
                if word_counter > max_count:
                    max_count = word_counter
                    shift_value = i
                    decrypted_msg = super(CiphertextMessage, self).apply_shift(i)
                        
        return (shift_value, decrypted_msg)
