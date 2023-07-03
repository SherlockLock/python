"""
    While Loops in Python
"""


i = 0

#While Syntax
while i < 10:
    i += 1
    
#While with break
i = 0
while i < 10:
    if i == 5:
        break #exits the loop
    
#While with continue
i = 0
while i < 10:
    if i == 5:
        i += 2
        continue #Go to the next loop iteration
    i += 1
    
#While...Else
i = 0
while i < 10:
    i += 1
else: 
    pass #Code to execute when while condition evaluates to false