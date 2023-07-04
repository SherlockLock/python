"""
Deleting things with Python
"""

import os

if os.path.exists("some_made_up_file.txt"):
    os.remove("theMadeUpFile.txt")

#Can only remove empty folders, so you would need to delete all files in the folder
if os.path.exists("some_made_up_folder"):
    os.rmdir("MadeUpFolder")