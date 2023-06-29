############## Boolean ##############
#     KEYWORD:          str
true = True
false = False
lie = 10 < 9
truth = "hello" == "world"

#Can also use the bool function to evaluate any value and get 
# a True or False

truthy_1 = bool("123") == True
truthy_2 = bool("") == False
truthy_3 = bool(1) == True
truthy_4 = bool(0) == False
truthy_5 = bool(-1) == True
truthy_6 = bool([]) == False
truthy_7 = bool([1]) == False
truthy_8 = bool(None) == False

class someClass():
    def __len__(self): 
        return 0 # or False will cause bool function to evaluate to False
    
classy = someClass()
truthy_9 = bool(bool(classy)) == False
