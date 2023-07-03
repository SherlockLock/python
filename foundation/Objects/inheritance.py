"""
Inheritance In Python

An OOP fundamental, inheritance allows classes to derive properties
or base inplementations of methds from another.

A child class is said to derive from a parent class


There are 4 types of inheritance:
- Single:       child inherits from one other class
- Multi-Level:  child inherits from a class that also inherits from a 
                    another class. (this can repeat up a chain)
- Hierarchical:  different kinds of children can inherit from the same parent
- Multiple:      A child can derive from multiple parents

Same concept as any other language. To inherit just list the class(es)
in the parenthesis after the name of the class in its definition

"""

class Foo(object):
    
    def __init__(self, id):
        self.id = id
        
    def doThing():
        print("Hard at work doing that thing you wanted")
        
        
class Bar(Foo):
    def __init__(self, id, prop):
        super().__init__(id)
        self.prop = prop