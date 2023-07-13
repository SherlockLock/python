"""

Lamdas are small anonymous functions that can take multiple
arguments but only one expression.

Useful when you are using a function for a short period of time


"""

#Basic addition lamda

add = lambda a, b : a + b
add(1,2) #returns 3

#Usage as an anonymous function inside of another function
def incrementer(num):
    return lambda x : x + num

incByTwo = incrementer(2)
incByTwo(1) #will return 3

incByThree = incrementer(3)
incByThree(1) #will return 4

