"""

variables and functions are limited in their availability based on their scope.

"""

globalVariable = "I am accessible everywhere within this file"

def foo():
    localFooVariable = "I am only available within the foo function"
    pass

def updateGlobalVariable():
    global globalVariable
    globalVariable = "update the global variable like this"

def createNewGlobal():
    global newGlobalVariable
    newGlobalVariable = "I am a new global variable that will be accessible everywhere"
    pass


    
def bar():
    
    #This function is only available within the bar function
    def localBarFunc():
        localBarFuncVariable = "I am only avaiable within the localBarFun function"
        pass
    
    pass

