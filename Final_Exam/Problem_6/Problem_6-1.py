# Problem 6-1
# 10.0/10.0 points (graded)
# This question has 3 parts

# Consider the following hierarchy of classes:

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)
        
# As written, this code leads to an infinite loop when using the Arrogant Professor class.

# Change the definition of ArrogantProfessor so that the following behavior is achieved:

# e = Person('eric') 
# le = Lecturer('eric') 
# pe = Professor('eric') 
# ae = ArrogantProfessor('eric')

# >>> e.say('the sky is blue')
# eric says: the sky is blue

# >>> le.say('the sky is blue')
# eric says: the sky is blue

# >>> le.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# >>> pe.say('the sky is blue')
# eric says: I believe that eric says: the sky is blue

# >>> pe.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# >>> ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that eric says: the sky is blue

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own
# test cases.


# Paste your class here
class ArrogantProfessor(Person): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

# Correct
