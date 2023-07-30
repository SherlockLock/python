"""

This python file contains functions that can parse data from files into training sets used in
models represented as numpy arrays


"""
import numpy as np

##XXX:ModuleNotFoundError
from Machine_Learning.Errors.ArgumentTypeMismatchError import ArgumentTypeMismatchError

def load():
    print("Load Data")
        
# #Entry Functions
# def load(path, featureColumns, targetColumns, start, end, skipLines):
    
#     try:
#         if path.endswith(".txt"):
#             valid_text_file_parser_params(path, featureColumns, targetColumns, start, end, skipLines)
#             print("READY TO PARSE :)")
#             # return parse_text_file(path)
#         else:
#             raise Exception("Unsupported file type to load data from")
        
        
#     except ArgumentTypeMismatchError:
#         print("Failed to load Data because of invalid parameters!")
#         exit(-1)
#     except:
#         print("An error occured loading data!")
#         exit(-1)
    
    

# #Parser Functions
# def parse_text_file(path, featureColumns, targetColumn, start=0, end=0, skipLines=[]):
#     """
#     A function that will parse a text file at the path passed and create two numpy arrays
#     of training sets for ML models to train on.
    
    
#     - Assumed all features are numbers
#     Args:
#         path (string): path to the file containing the data
#         start (number): the line number we start reading data from
#         end (number):  the line number we stop reading data from
#         skipLines (list(number)): the line numbers we ignore data on
#         targetColumn (number): the column of data we assign to the target array
#         featureColumns (list(number)): a list of numbers that represent columns we parse data into the feature array

#     Returns:
#         features, targets (np.arrays): NumPy arrays of the features and targets for the model to train on
#     """
    
#     try:
        
#         #Open the file
#         f = open(path, "rt")
        
#         #Skip to the line to start reading data from
#         for _ in start:
#             f.readline()
        
#         #Create lists to hold the data we parse
#         feature_list = []
#         target_list = []
        
#         lineNum = start
        
#         #Loop over the rest of the file
#         for line in f:
            
#             #Break out of loop if it is the end of specified lines to read
#             if lineNum == end:
#                 break
#             #Skip any lines specified in the parameters
#             elif lineNum in skipLines:
#                 continue
            
#             #Parse data from read line
#             split_line = line.split(" ")
#             data = split_line[0:len(split_line)]

#             #Create an empty feature vector
#             feature = np.zeros(len(featureColumns))
            
#             #Parse the data values into the feature vector
#             for i in range(len(feature)):
#                 if not i == targetColumn:
#                     feature[i] = float(data[i])
                
#             #Add found data to the training set
#             feature_list.append(feature)
#             target_list.append(data[targetColumn])
                
        
#         #Close the files
#         f.close()
        
#         #Return Numpy Arrays for our features and targets
#         return np.array(feature_list) , np.array(target_list)

#     except FileNotFoundError:
#         exit("Error: Could not find training data to load")
#     except TypeError:
#         exit("Error: A type error occured somewhere")
#     except:
#         exit("Error: An unknown error occured reading the training data")


# #Helper Functions
# def valid_text_file_parser_params(path, featureColumns, targetColumn, start, end, skipLines):
    
#     if not valid_string_parameter(path):
#         raise ArgumentTypeMismatchError("path", "str", type(path))
    
#     if not valid_number_list_parameter(featureColumns):
#         raise ArgumentTypeMismatchError("featureColumns", "list(int)", type(featureColumns))
    
#     if len(featureColumns) == 0:
#             raise ArgumentTypeMismatchError("featureColumns", "Non-Empty list", "Empty List")
    
#     if not valid_int_parameter(targetColumn):
#         raise ArgumentTypeMismatchError("targetColumn", "int", type(targetColumn))
    
#     if not valid_int_parameter(start):
#         raise ArgumentTypeMismatchError("start", "int", type(start))

#     if not valid_int_parameter(end):
#         raise ArgumentTypeMismatchError("end", "int", type(end))
    
#     if not valid_number_list_parameter(skipLines):
#         raise ArgumentTypeMismatchError("skipLines", "list(int)", type(skipLines))
    
#     return

# #Parameter Validators
# def valid_string_parameter(arg):
#     if type(arg) is str:
#         return True
#     else:
#         return False

# def valid_int_parameter(arg):
#     if type(arg) is int:
#         return True
#     else:
#         return False
    
# def valid_number_list_parameter(arg):
#     if type(arg) is list:
#         for e in arg:
#             if type(e) is not int:
#                 return False
#         return True
#     else:
#         return False


# load()