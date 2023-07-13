"""

To create a module, just save the file containing the code to the module in a .py file.

"""

#Then use the import statement
import scope
#or give the module a name like
import classes as classy
#Or selections of a module using 
from inheritance import Foo


# you can access variable and functions within the module
scope.globalVariable = "I have been updated from modules.py"

#View all the functions and variables avaiable in the module with 
dir(scope)