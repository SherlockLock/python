# =========== List =========== 
#   KEYWORD: list
# Similar to, but not as efficient as, arrays in other languages
# Items are ordered, changeable, and allow duplicate values
# Lists are iterable objects and their items can be of any data type

# --- List Access
list = [1, "2", 3.3, True]
access_item = list[0] # equals 1
parking_in_rear = list[-2] #equals 3.3
walker_texas = list[1:3] #equals ["2", 3.3] (first number included and second number excluded)
to_the_moon = list[2:] # equals [3.3, True] (From the index to the end)

if 1 in list:
    #Checks to see if the value is in the list
    pass #Do nothing function

# --- num elements in a list
list.count()
        
# --- Add to list
list.append("element") #add any element
list.insert(1, "kiwi") # inserts at the specified index
list.extend((1,2)) #Can add on any iterable object
list = list + list # joins two iterables
list.extend(list) #Same as above
    
# --- List Modification
list[1] = False #Change a specific element
list[1:3] = [1,2] #Replaces the range with the element(s) provided
list.insert(1, "new") #Inserts an element at the specified index


# --- Remove from a list
list.remove(False) #Removes the first item that matches the elemnent provided
list.pop(1) #Removes the item at the specified index
list.pop() #Removes the last item
del list[0] #also removes at the specified index
list.clear() #Will empty the list

#--- Loop through a list

#Go through entire list
for element in list:
    pass 

for element_index in range(len(list)):
    pass 

#list comprehension: Creating a new list from an existing list based on a conditional


#newlist = [expression for item in iterable]    OR
#newlist = [expression for item in iterable if conditional]

#Where expression is the current item in the iteration but is
#   also the outcome to be added to the list
# And 'item in iterable' is like the for loop above
#And 'if conditional' is an optional filter for the newlist


#--- Sorting Lists

#.sort() is an instance method called on a list and modifies the list it
# was called on
list.sort() #Sorts list ascending
list.sort(reverse=True) #Sorts list descending
list.reverse() # reverses the order of the list

def someSortFunction(a,b):
    if a < b:
        return -1  # a comes before b
    elif a > b:
        return 1  # a comes after b
    else:
        return 0  # a and b are equal
list.sort(key=someSortFunction) #custom sort Function

newlist = sorted(list, key=None) #Returns a new sorted list

#--- Copy Lists
copied = list.copy() # Creates a shallow copy of the list
copied = list(list)

