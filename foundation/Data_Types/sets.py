#A set is collection data type in python that is unordered, unchangeable, and unindexed
#While the data type of a declared set and its items can not be changed, you can remove and add items to a set

some_set = {1,2,3}

#You are not allowed to have duplicate values in a set
invalid_set = {1,1}
another_invalid_set = {1, True}

#Get the length of a set
length = len(some_set)

#A set has no restrictions on data types it contains
multi_type_set = {1, "one"}


#Updating a set
multi_type_set.add(2)
multi_type_set.update(some_set) #performs a union of the the set with any iterable
multi_type_set.union(some_set) #identical to above
multi_type_set.intersection_update(some_set) #keeps only items in the intersection of sets
new_set_1 = multi_type_set.intersection(some_set) #returns a new set identical to the result above
multi_type_set.symmetric_difference_update(some_set) #keeps only items not found in the intersection of sets
new_set_2 = multi_type_set.symmetric_difference(some_set) #returns a new set identical to the result above


#Removing Items
multi_type_set.discard(4) #removes if a member
multi_type_set.remove(1) #Must be a member
multi_type_set.pop() #removes a random item
multi_type_set.clear()


#Other set methods
new_set_1.isdisjoint(some_set) #returns whether there is an intersection
new_set_1.issubset(some_set) #returns wheter another set contains this set
new_set_1.issuperset(some_set) #returns where the set contains another set

#Can loop through set items with a for loop
for e in some_set:
    pass

