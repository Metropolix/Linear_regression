from matplotlib.pyplot import get
from numpy import genfromtxt, newaxis
import numpy as np
from matrix_training import hypothesis
import tools
import sys

def feature_scaling_with_mean_normalization(X):
    ''' Feature scaling for large range of X using mean normalization'''
    X = (X - np.mean(X)) / (np.max(X) - np.min(X))
    return(X)

def hypothesis(X, theta):
    predictions = np.dot(X, theta)
    return(predictions)

def get_user_input(X, theta):
    ''' Get user input and formalize it with feature scaling and mean normalization'''
    try:
        user_input = float(input("Enter your value:"))
    except:
        sys.exit('Error: Value must be a number (eg: 1.2 or 10)')
    user_input = np.array([1, user_input])
    user_input = (user_input - np.mean(X)) / (np.max(X) - np.min(X))
    return(user_input)

if __name__ == "__main__":
    ''' Variable initialization'''
    theta = genfromtxt('theta_file.csv', delimiter=',')
    theta = theta[newaxis].T
    X, y = tools.load_data_matrix_from_csv('data.csv')
    user_input = get_user_input(X, theta)

    res = hypothesis(user_input, theta)
    print("Predicted price:", res)