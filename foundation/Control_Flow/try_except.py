"""

"If you fail to plan, you are planning to fail"
    - Benjamin Franklin

"""

#Basic Outline
try:
    #To execute code that might raise an exception
    pass
except:
    #Recover from an exception if it occurs (Fail Gracefully)
    pass

#Handling specific exceptions
try:
    pass
except NameError:
    pass
except:
    pass

#Append an else block to execute code when the try hsa succeded
try:
    pass
except:
    pass
else:
    #Only executes if no exceptions were raised in the try
    pass

#Or run some code when it finished entirely no matter the outcome
try: 
    pass
except:
    pass
finally:
    pass


#You can raise an exception like so
try:
    raise Exception("Some error")
except:
    pass

#You can raise an a specific exception
try:
    raise TypeError("Some error with types")
except:
    pass

#Or create custom Exception classes
class CustomException(Exception):
    pass

try:
    raise CustomException()
except CustomException:
    pass