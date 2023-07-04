"""

A simple Multi Variable Linear Regression Model to estimate the cost of an apartment.


Author: Isaac Lock
"""

import numpy as np
import matplotlib.pyplot as plt


def loadTrainingSet(path):
    """
    
    - Assumed the first line in the text files is a description of the data
    - Assumed that the last line of the data is the target
    - Assumed all features are numbers
    Args:
        path (String): path to the file containing the data

    Returns:
        features, targets (np.arrays): NumPy arrays of the features and targets for the model to train on
    """
    
    #Initalize Training Data
    features = np.array([])
    targets = np.array([])
    
    try:
        f = open(path, "rt")
        
        #Skip the first line
        f.readline()
        
        #Loop over the rest of the file
        for line in f:
            #Parse data from read line
            data = line.split(" ")
            new_features = data[0:len(data) - 1]
            target = float(data[-1])
            
            print("Here")
            #Create a feature vector of floats
            new_features_cleaned = np.array([])
            for feature in new_features:
                print(f"Appending feature {feature}")
                new_features_cleaned.append(float(feature))
                print(f"appended feature {feature}")
            
            
        #Add found data to the training set
        features.append(new_features_cleaned)
        targets.append(target)
        
        f.close()
    except FileNotFoundError:
        print("Error: Could not find training data to load")
    except TypeError:
        print("Error: A type error occured somewhere")
    except:
        print("Error: An unknown error occured reading the training data")
    
    return features, targets



features, targets = loadTrainingSet("Machine_Learning/linear_regression/data/apts_data.txt")

print(f"Found features {features}")