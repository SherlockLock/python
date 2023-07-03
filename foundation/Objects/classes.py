"""
Basics of Classes and Objects in Python!
"""

#Python is an OOP and almost everything in Python is an Object with properties and methods

#Create a class using the 'class' keyword
class Foo:
    pass #Can use the keyword pass to skip implementation like a placeholder

class BasicNumber:
    number = 1 #A property called number with a default value of 1
    
#Create on object 
num = BasicNumber()
#Access a property
num.number


#Example Class
class Person:
    
    #some other attribute
    birthplace = "Earth"
    
    #Define the Initialization method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #Returns a string that will be printed anytime the object is passed into the print method
    def __str__(self):
        return f"{self.name} is a Person who is {self.age} years old"
    
    #Some method that can be executed
    def func(self):
        print(f"Exectuing func on Person with name {self.name}")

person = Person("Chris", 50)
person.name
person.age
print(person)
person.func()
#Set a new value for a property
person.name = "Adrian"
#Create a new property
person.weight = 100
#Or remove a property completely (be wary)
del person.weight

#You can also delete the entire object
del person
