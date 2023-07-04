"""
Fun With Tuples in Python

Tuples are used to store multiple data types in a single variable.

It is an ordered collection that is not mutable and allows duplicates
"""

#Initialization
some_tuple = (1, "hey", 3.3)

#Access elements
element = some_tuple[0]

#Determine the length of the tuple
tuple_len = len(some_tuple)

#Can use negative indexes like lists to access from the back
last_element = some_tuple[-1]

#Or get a subset of the tuple with a range
subset = some_tuple[1:2]

#Check if a value exists
if "hey" in some_tuple:
    pass

#while you can not update a tuple directly, you can do a workaround
#by converting it to a list and then back to a tuple
listy = list(some_tuple)
#do any modifications to the 'tuple'
listy.append("new")
some_tuple = tuple(listy)


#When we create a tuple we are packing it. This can go in reverse with
#Python (called unpacking)

pack = (1,2,3)
(unpack_1, unpack_2, unpack_3) = pack

#While unpacking requries the number of variables to amtch the tuple exactly
# we can use an asterisk to combine values into a list like so

pack_2 = (1,2,3,4,5)
(var1, *var2) = pack_2
#var1 will equal 1
#var2 will equal a list contianing the remainding values in the tuple

#Loop tuples just like any other iterable collection
for element in some_tuple:
    pass

#Join two tuples with the '+' operator
new = some_tuple + some_tuple

#Or multiple the content a given number of times with the '*' oeprator
multiplied = some_tuple * 4

#And lastly, two main methods used with tuples
some_tuple.count('1') #returns the number of times an value occurs inside
some_tuple.index('1') #returns the first index of the element found in the tuple