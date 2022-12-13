# importing packages

import matplotlib.pyplot as plt
import numpy as np

my_data = np.genfromtxt('data.csv', delimiter=",") # read data
X = my_data[:, 0].reshape(-1, 1) # reshape(-1,1) tells python to convert the array into a matrix with one coloumn.
                                # “-1” tells python to figure out the rows by itself.
ones = np.ones([X.shape[0], 1]) # create a array containing only ones
X = np.concatenate([ones, X], 1) # cocatenate the ones to X matrix
y = my_data[:, 1].reshape # create the y matrix

print(plt.scatter(my_data[:, 0].reshape(-1, 1), y))