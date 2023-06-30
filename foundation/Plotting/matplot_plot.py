import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([8, 5, 6, 2, 5])

#Some function to graph
def linear_function(values, m, b):
    outputs = np.zeros(len(values))
    for i in range(len(values)):
        outputs[i]= m * values[i] + b
    return outputs


linear_func_1 = linear_function(x_values, 1, 0)
linear_func_2 = linear_function(x_values, 2, 5)

#Plot our first linear function
plt.plot(x_values, linear_func_1, c='b', label="f(x)= x")

#Plot our second linear function
plt.plot(x_values, linear_func_2, c='y', label="f(x)= 2x + 5")

#Plot the x and y values
plt.scatter(x_values, y_values, marker='x', c='r', label="Data Points")

#Set the title
plt.title("Some Plot")

#Set the y-axis label
plt.ylabel("Y-Values")

#Set the x-axis label
plt.xlabel("X-Values")

#Show the plot
plt.legend()
plt.show()
