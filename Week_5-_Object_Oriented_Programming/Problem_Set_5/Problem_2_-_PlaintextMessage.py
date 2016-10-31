# Problem 2 - PlaintextMessage
# 15/15 points (graded)
# For this problem, the graders will use our implementation of the Message class, so don't worry if you did not get the previous parts
# correct.

# PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value. Our class will always
# create an encoded version of the message, and will have methods for changing the encoding.

# Implement the methods in the class PlaintextMessage according to the specifications in ps6.py. The methods you should fill in are:
# __init__(self, text, shift): Use the parent class constructor to make your code more concise.
# The getter method get_shift(self)
# The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone from mutating the 
# original dictionary.
# The getter method get_message_text_encrypted(self)
# change_shift(self, shift): Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines
# of code.

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
        
# Correct
