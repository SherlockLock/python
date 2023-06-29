# ============  GENERAL VARIABLES IN PYTHON =================== #


#Variables do not require a command in its declaration
msg = "VARIABLES IN PYTHON" # msg is a string
print(msg)

# There is no strict typing in python. It does not require a typ declaration
# and a variable can change type throughout its lifetime.
msg = 1 # msg is now an integer

#You can find out the type of a variable using the function
type(msg) #returns the class of the variable

#You can cast a variable to a specific type
some_int = int(1)
some_int_from_a_string = int("1")


#The del keyword will delete any object
del msg #will delete the msg variable

