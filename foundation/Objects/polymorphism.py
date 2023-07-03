"""
Polymorphism in Python

Not the same as the 5e spell 🧙‍♀️

Just method overridding.

Change the method of a parent class in the childs implementation

"""

class Foo(object):
    def __init__(self, id):
        self.id = id
        
    def thing(self):
        print("Doing Foo's thing")
        
class Bar(Foo):
    def thing(self):
        print("Doing Bar's things")