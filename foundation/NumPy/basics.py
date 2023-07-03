"""
Some fun with Numerical Python and learning matrix functions available
in Numpy!

Yay, Linear Algebra! 🥳
"""

import numpy as np

#Numpys Major addition to python is traditional (and optimized) arrays as a data type
#they are actually matricies but can be thought of as arrays from a syntax perspective
zeros = np.zeros(10) #creates an array of zeros
arr_0 = np.array(([1,2,3], [4,5,6]))
arr_1 = np.array([1,2,3]) #Just like a normal array
arr_2 = np.array(([1, 1.0, "string"], [1,3,"str"])) # a 2 by 3 matrix with the following values
rand_arr = np.random.random_sample(4) #A array of length 4 filled with random numbers between 0 and 1
rand_arr_2 = np.random.rand(4) #Same as above
incremental = np.arange(4.) # equal to [0,1,2,3]

#access elements as you please
zeros[1] = 1 #second index of zeros is now equal to 1
variable = zeros[3] #Equal to 0
element = arr_0[0][0] #Equal to 1

#Or slice from the array [start:stop:step]
kimbo = arr_1[1:1:1] 

#We can reshape arrays after they have been initialized
arr_0_shaped = arr_0.reshape(1,6) #Turns arr_0 into a matrix that has the dimesions (1,6)
#IMPORTANT: .reshape will not grow or shrink the array and the order of elements will be the same

#Transposing (columns to rows and rows to columns)
arr_0.transpose()

#Flattening: sick of the clutter, reduce the array to 1 dimension using
arr_0.flatten()

#A description of the matricies shape
zeros_shape = zeros.shape # is equal to (10,)
arr_2_shape = arr_2.shape # is equal to (2,3)

#Operations (without the scribbling (or the errors))
addition = arr_1 + arr_1
subtraction = arr_1 - arr_1
multiplication = arr_1 * arr_1
division = arr_1 / arr_1
scalar = arr_1 + 1 #same with the other operations too!

#and some build in methods for more options
np.power(arr_1, 2)
np.log(arr_1)

#Wanting to find an aggregation? Look no further
np.sum(arr_1)
np.mean(arr_1)
np.median(arr_1)
np.min(arr_1)
np.max(arr_1)
np.std(arr_1)

#Sick of your free will, add some verified randomness
rand_1 = np.random.randint(0,10,5) #Creates a One-D array thats 5 elements where each element is an integer between 0 and 10
rand_2 = np.random.randint(0,10, (3,3)) #same as above but a 3x3 matrix

#Really want some randomness? Set a seed and leave your worries at the door
np.random.seed(1)

#Can't decide? Leave it up to fate
rand_element = np.random.choice(rand_1) #can be an array or a slice of an array
# you can add a parameter after the array to replace the selection with 

#The dot product to end all implementations
np.dot(arr_1, arr_1)