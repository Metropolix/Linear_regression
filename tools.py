import sys
import numpy as np
from numpy import genfromtxt
import numpy as np

def load_data_matrix_from_csv(filename):
    '''Goal is to read data from csv and set correct matrix with first row as 1'''
    try:
        my_data = genfromtxt(filename, delimiter=',')
        my_data = np.delete(my_data, (0), axis=0) # Remove first row (csv title row)
        my_data = my_data[np.argsort(my_data[:, 0])] # Sort the matrix by first column (X)
        X, y = np.split(my_data, 2, axis=1)
        b = np.ones((y.size,1)) 
        X = np.hstack((b,X)) # Add a first column (of 1) to X 
        return(X, y)
    except:
        sys.exit("Can't read and load datafile")