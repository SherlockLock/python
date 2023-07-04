"""
How to read from files in python
"""

#Open a file
try: 
    
    file = open("Foundation/Files/Example/file.txt", "rt")
    
    #Reads the entire file
    entire_file = file.read()
    
    #Reads the specified number of characters from the file
    first_10 = file.read(10)
    
    #Reads one line in the file
    first_line = file.readline()
    
    #But the stream of characters is sequentially updated each time
    # a read method is called, so after the first read method 
   
    file.close()
except:
    print("Could not find file")