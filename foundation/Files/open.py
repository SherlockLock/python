"""
Opening files in python
"""

##The open function takes two parameters: the file name and the mode
filename = "name"
read_mode = "r"
append_mode = "a"
write_mode = "w"
create_mode = "x"

#These values are appended to the end of the mode to determine how to
#what data we will be working with in the specific modde
handling_text = "t"
handling_binary = "b"

try:
    file = open("file.txt", "rt") #Open the file 'file.txt' in as a text file in read mode
    #It is assumed the file is in the same directory, so this file will not be found
except:
    print("Could not find file")

try: 
    #If the file is in a differrent location, specify its location
    alt_file_open = open("Foundation/Files/Example/file.txt", "rt")
    print("Found File 'file' in example_files directory")
    
    #Then close up after yourself :)
    alt_file_open.close()
except:
    print("Could not find file")
    

    