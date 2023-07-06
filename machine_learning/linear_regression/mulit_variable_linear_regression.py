"""

A simple Multi Variable Linear Regression Model to estimate the cost of an apartment.


Author: Isaac Lock
"""

######### IMPORTS #####################
import numpy as np
import copy, math
import matplotlib.pyplot as plt

######### FUNCTIONS ###################

def loadTrainingSet(path):
    """
    TODO: 
    
    generalize for any file path and any number of data variables
    
    - Assumed the first line in the text files is a description of the data
    - Assumed that the last line of the data is the target
    - Assumed all features are numbers
    Args:
        path (String): path to the file containing the data

    Returns:
        features, targets (np.arrays): NumPy arrays of the features and targets for the model to train on
    """
    
    try:
        
        #Open the file and skip the first line
        f = open(path, "rt")
        f.readline()
        
        #Create lists to hold the data we parse
        feature_list = []
        target_list = []
        
        #Loop over the rest of the file
        for line in f:
            
            #Parse data from read line
            split_line = line.split(" ")
            data = split_line[0:len(split_line) - 1]
            target = float(split_line[-1])
            
            #Create an empty feature vector
            feature = np.zeros(len(data))
            
            #Parse the data values into the feature vector
            for i in range(len(feature)):
                feature[i] = float(data[i])
                
            #Add found data to the training set
            feature_list.append(feature)
            target_list.append(target)
                
        
        #Close the files
        f.close()
        
        #Return Numpy Arrays for our features and targets
        return np.array(feature_list) , np.array(target_list)

    except FileNotFoundError:
        exit("Error: Could not find training data to load")
    except TypeError:
        exit("Error: A type error occured somewhere")
    except:
        exit("Error: An unknown error occured reading the training data")

def model(inputs, weights, constant):
    """
    A basic multivariate model which returns the dot product of the
    input and weight vectors summed with the constant

    Args:
        inputs (np.array): vector of inputs
        weights (np.array]): vector of weights
        
    Returns:
        y (number): target / output
    """
        
    return np.dot(inputs, weights) + constant
   
# def sqrd_error_derivative_wrt_j(features, target, weights, constant, j):

#     # tmp = features
#     # print(f"Looking at {features}")
#     m = features.shape[0]
#     sum = 0
    
#     for i in range(m):
#         sum += (model(features, weights, constant) - target) * features[j]

#     return ( 1 / m ) * sum

# def sqrd_error_derivative_wrt_constant(features, target, weights, constant):
    
#     m = features.size
#     sum = 0
    
#     for i in range(m):
#         sum += model(features[i], weights, constant) - target


#     return ( 1 / m ) * sum


def compute_gradient_descent(features, targets, weights, constant):
    
    #Initialize local variables
    grad_weights = np.zeros((features.shape[1],))
    grad_constant = 0.
    
    #Loop over the values
    for i in range(len(features)):
        
        y = model(features[i], weights, constant)
        grad_constant = grad_constant + y
        for j in range(len(features[i])):
            grad_weights[j] = grad_weights[j] + y * features[i, j]
            # print(f"Setting constant[{j}] = {sqrd_error_derivative_wrt_constant(features[i], targets[i], weights, constant)}")
            # grad_weights[j] += sqrd_error_derivative_wrt_j(features[i], targets[i], weights, constant, j)
        
        # grad_constant += sqrd_error_derivative_wrt_constant(features[i], targets[i], weights, constant)
        
    #Calculate average
    grad_constant = grad_constant / features.shape[0]
    grad_weights = grad_weights / features.shape[0]

    return grad_weights, grad_constant

def run(features, targets, weights_init, constant_init, alpha, iterations):
    
    weights = copy.deepcopy(weights_init)
    constant = constant_init
    
    for _ in range(iterations):
        w_grad, con_grad = compute_gradient_descent(features, targets, weights, constant)
    
        tmp_w = weights - (alpha * w_grad)
        tmp_con = constant - (alpha * con_grad)
        weights = tmp_w
        constant = tmp_con
    
    return weights, constant
        

######### MODEL PARAMETERS ############
 
 #Path to training data
# path = "Machine_Learning/linear_regression/data/apts_data_1.txt"
path = "Machine_Learning/linear_regression/data/test.txt"
    
#Gradient Descent Parameters
alpha = 5e-7                        #Learning Rate
iterations = 1000                   #Number of Gradient Descent Iterations
weights_init = [1,1,1,1]            #Initial value for slope
constant_init = 0                   #Initial value for the constant 



######### RUN #########################

print("\n*******************************************\n")

print(f"Loading Training Data from {path}")
features, targets = loadTrainingSet(path)
# print(f"Found features:\t{features}")
# print(f"Found targets:\t{targets}")

print("\n*******************************************\n")

print("Running Gradient Descent with following Params:")
print(f"weights_init:\t{weights_init}")
print(f"constant_init:\t{constant_init}")
print(f"alpha:\t\t{alpha}")
print(f"iterations:\t{iterations}")
weights, constant = run(features, targets, weights_init, constant_init, alpha, iterations)

print("-------------------------------------------")

print(f"Found weights:\t{weights}")
print(f"Found constant:\t{constant}")

print("\n*******************************************\n\n")

print(f"Comparing found weights to training data\n")

for i in range(2):
    data_set = np.random.randint(0, features.shape[0])
    print(f"For feature with data: {features[data_set]}")
    print(f"\tTarget Value\t\t{targets[data_set]}")
    print(f"\tModel Prediction\t{model(features[data_set], weights, constant)}\n")

print("\n*******************************************\n\n")

# sqft = 700
# bed = 1
# bath = 1
# balcony = 0
# print(f"Estimation for {sqft} sqft bedroom with {bed} bed, {bath} bath, & {balcony} balconies")
# print(f"\t\t$ {model([sqft, bed, bath, balcony], weights, constant)}")

# print("\n*******************************************\n\n")



