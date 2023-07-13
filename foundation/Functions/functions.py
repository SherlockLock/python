"""
All the things you can do with functions in python.

"""

#Create a function
def func():
    pass

#Call a function
func()

#Create a funtion with arguments seperated by a comma
def oneArg(one):
    pass

def twoArgs(one, two):
    pass

#If you do not know how many arguments will be passed into the function
#You can add a * before the parameter name
def someArgs(*args):
    for arg in args:
        print(arg) 
        
    print(arg[1])
    pass

someArgs(1,2,3,4,5)

#Order of arguments matters unless you use a keyword when calling the function
twoArgs(1,2)
#Is the same as
twoArgs(two=2, one=1)

#If you do not know how many keyword arguments will be passed into the function
#You can add two asterisks before an argument
def manyKeywordArgs(**args):
    print(args["key"])
    
manyKeywordArgs(key="Some Keyword Arg", anotherKey="Wowza")

#We can provide a default value for an argument in case it might not be provided
def default(variable=1):
    pass

# you can also return any type of variable you want or nothing at all
def returnOneThing():
    return 1

def returnTwoThings():
    return 1, 2


