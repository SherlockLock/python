"""
This file is a simple implementation for gradient descent
to calculate the best parameters for a univariate linear
regression model.

Author: Isaac Lock
"""

######### IMPORTS #####################
import numpy as np
import matplotlib.pyplot as plt

######### FUNCTIONS ###################

def model_function(x, m, b):
    """
    Some univariate linear regression model
    
    In this case, we will be using a line represented in slope intercept form
    i.e.: f(x) = mx + b

    Args:
        x (number): feature / input
        m (number): Parameter / coefficent (in this instance it is the slope of the line)
        b (number): Parameter / coefficent (in this instance it is the y-intercept)

    Returns:
        y (number): target / output
    """
    return (m * x) + b

def sqrd_error_cost_function(x_values, y_values, m, b):
    """
    This function is our implementation of the squared error cost function.
    
    For this example, the function is as follows:
    
    J(m,b) = (1 / 2n) * (from 1 to n) ∑ (f(x_i) - y_i) ^ 2
    
    Where:
    
    J(m,b)  : is the cost of the function used with the parameters m and b
    m & b   : are the parameters being tested for the cost function
    n       : is the total number of values in the training set
    i       : is the training set number being evaluated
    x_i     : is the ith value in the x value set
    y_i     : is the ith value in the y values set
    f(x_i)  : is our model function being evaluated with x_i

    Args:
        x_values (np.array): training set for x values
        y_values (np.array): training set for y values
        m (number): slope parameter being tested
        b (number): y-intercept parameter being tested

    Returns:
        J(m,b) (number): represention of the cost of the function with the chosen parameter values
    """
    
    #Initalize local parameters
    j = 0 # intial value of J(m,b)
    n = len(x_values) 
    
    for i in range(n):
        x_i = x_values[i]
        y_i = y_values[i]
        f_x_i = model_function(x_i , m, b)
        
        j += (f_x_i - y_i) ** 2
        
    return (1 / (2 * n)) * j

def sqrd_error_derivative_wrt_m(x_values, y_values, m, b):
    """
    Derivative of the Squared Error Cost Function using
    our model function with respect to m results in the
    following equation:
    
    (1 / n) * (from 1 to n) ∑ (f(x_i) - y_i) * x_i
    
    Where:
    
    m & b   : are the parameters being tested
    n       : is the total number of values in the training set
    x_i     : is the ith value in the x value set
    y_i     : is the ith value in the y values set
    f(x_i)  : is our model function being evaluated with x_i

    Args:
        x_values (np.array): training set for x values
        y_values (np.array): training set for y values
        m (number): slope parameter being tested
        b (number): y-intercept parameter being tested

    Returns:
        r (number): represention of the cost of the function with the chosen parameter values
    """
    
    #Initialize local variables
    r = 0
    n = len(x_values)
    
    for i in range(n):
        x_i = x_values[i]
        y_i = y_values[i]
        f_x_i = model_function(x_i, m, b)
        r += (f_x_i - y_i) * x_i
    
    return ( 1 / n) * r

def sqrd_error_derivative_wrt_b(x_values, y_values, m, b):
    """
    Derivative of the Squared Error Cost Function using
    our model function with respect to b results in the
    following equation:
    
    (1 / n) * (from 1 to n) ∑ (f(x_i) - y_i)
    
    Where:
    
    m & b   : are the parameters being tested
    n       : is the total number of values in the training set
    x_i     : is the ith value in the x value set
    y_i     : is the ith value in the y values set
    f(x_i)  : is our model function being evaluated with x_i

    Args:
        x_values (np.array): training set for x values
        y_values (np.array): training set for y values
        m (number): slope parameter being tested
        b (number): y-intercept parameter being tested

    Returns:
        r (number): represention of the cost of the function with the chosen parameter values
    """
    
    #Initialize local variables
    r = 0
    n = len(x_values)
    
    for i in range(n):
        x_i = x_values[i]
        y_i = y_values[i]
        f_x_i = model_function(x_i, m, b)
        r += (f_x_i - y_i)
    
    return ( 1 / n) * r

def compute_gradient_descent(x_values, y_values, m, b):
    """
    This method returns the computed values for gradient descent with the passed in parameters

    Args:
        x_values (np.array): training set for x values
        y_values (np.array): training set for y values
        m (number): slope parameter being tested
        b (number): y-intercept parameter being tested
        
    Returns:
        m_result (number) : found minimum for parameter m
        b_result (number) : found minimum for parameter b
    """
    
    #Initialize local variables
    m_result = 0
    b_result = 0
    n = len(x_values)
    
    #Loop over the values
    for i in range(n):
        m_result += sqrd_error_derivative_wrt_m(x_values, y_values, m, b)
        b_result += sqrd_error_derivative_wrt_b(x_values, y_values, m, b)
        
        # tmp_m = sqrd_error_derivative_wrt_m(x_values, y_values, m, b)
        # tmp_b = sqrd_error_derivative_wrt_b(x_values, y_values, m, b)
        # m_result += tmp_m
        # b_result += tmp_b
    
    #Calculate average
    m_result = m_result / n
    b_result = b_result / n

    return m_result, b_result
    
    
    
    
    # grad_cost_m = 0
    # grad_cost_b = 0
    
    # #Loop over the training examples
    # for i in range(len(x_values)):
    #     grad_cost_m += derivative_wrt_m(m, b, i)
    #     grad_cost_b += derivative_wrt_b(m, b, i)
        
    # grad_cost_b = grad_cost_b / len(x_values)
    # grad_cost_m = grad_cost_m / len(y_values)
    
    # return grad_cost_m, grad_cost_b
        
def run_gradient_descent(x_values, y_values, m_init, b_init, alpha, iterations):
    """
    This method is the algorithm to find the best parameters for the model
    using gradient descent.
    
    The goal is to minimize the result of the cost function
    described in the method sqrd_error_cost_function by updating the values of 
    m and b.

    Returns:
        _type_: _description_
    """
    
    #Initial local variables
    m = m_init
    b = b_init
        
    for _ in range(iterations):
        
        m_grad, b_grad = compute_gradient_descent(x_values, y_values, m, b)
        
        tmp_m = m - (alpha * m_grad)
        tmp_b = b - (alpha * b_grad)
        m = tmp_m
        b = tmp_b
        
        
        
    return m, b

######### MODEL PARAMETERS ############

#Training Data
x_train = np.array([1,  2,  3,  4,  5,  6,  7,  8,   9,   10])
y_train = np.array([25, 56, 65, 67, 74, 87, 94, 123, 140, 155])

#Gradient Descent Parameters
alpha = 0.01        #Learning Rate
iterations = 100    #Number of Gradient Descent Iterations
m_init = 0          #Initial Value for slope
b_init = 0          #Initial Value for y-intercept


######### RUN #########################

#Plot Training Data
plt.scatter(x_train, y_train, marker='o', c='k', label="Training Data")

#Calculate Gradient Descent Model
m_final, b_final = run_gradient_descent(x_train, y_train, m_init, b_init, alpha, iterations)
found_model = model_function(x_train, m_final, b_final)

#Plot Gradient Descent Model
plt.plot(x_train, found_model, c='b', label=f"Found Model (α={alpha}, i={iterations}, ({m_init}, {b_init}))")

#Set Up Table
plt.title("Gradient Descent Plot")
plt.ylabel("Y-Values")
plt.xlabel("X-Values")
plt.legend()
plt.show()