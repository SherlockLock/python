"""
This program shows a graph that represents the output for a 
generic univariate linear regression model using y=mx+b
(slope-intercept form) as the model to predict the values.
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_model(values, m, b):
    """
    Compute values for the linear model using the model function
    f(x) = mx + b

    Args:
        x (array): values to compute for
        m, b (integers): parameters to compute with
    Returns:
        y (array): models calculated target values in an array
    """
    
    #Initalize return value
    f_x = np.zeros(len(values)) #Create an empty array for all the values to compute for
    
    #Loop over the ppassed in values and compute the result of the model
    for i in range(len(values)):
        #model function
        f_x[i]= m * values[i] + b
    
    return f_x

# Random training set for the model
x_train = np.array([1.0, 2.0, 3.0, 4.0])
y_train = np.array([175.0, 450.0, 650.0, 725.0])

#Estimated values for optimal Parameters / Coefficents / Weights
m = 200
b = 0

#Calculate
model_output = calculate_model(x_train, m, b)

#Plot our model output
plt.plot(x_train, model_output, c='b', label="Model Prediction")

#Plot the training data points
plt.scatter(x_train, y_train, marker='o', c='r', label="Training Set")

#Set the title
plt.title("Example Univariate Linear Regression Model")

#Set the y-axis label
plt.ylabel("Y - Values")

#Set the x-axis label
plt.xlabel("X - Values")

#Show the plot
plt.legend()
plt.show()
