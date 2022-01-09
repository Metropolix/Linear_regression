import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

def show_all_datas(X, y, theta, cost):
    print("X: ", X)
    print("--------")
    print("y: ", y)
    print("--------")    
    print("theta: ", theta)
    print("--------")
    print("cost:", cost)

def plot_data(X, y, theta, cost):
    predictions = hypothesis(X, theta)
    plt.scatter(X[:,1], y)
    plt.plot(X[:,1], predictions, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def load_data_matrix_from_csv(filename):
    '''Goal is to read data from csv and set correct matrix with first row as 1'''
    my_data = genfromtxt(filename, delimiter=',')
    my_data = np.delete(my_data, (0), axis=0) # Remove first row (csv title row)
    my_data = my_data[np.argsort(my_data[:, 0])] # Sort the matrix by first column (X)
    X, y = np.split(my_data, 2, axis=1)
    b = np.ones((y.size,1)) 
    X = np.hstack((b,X)) # Add a first column (of 1) to X 
    return(X, y)

def feature_scaling_with_mean_normalization(X):
    ''' Feature scaling for large range of X using mean normalization'''
    X = (X - np.mean(X)) / (np.max(X) - np.min(X))
    return(X)

def hypothesis(X, theta):
    predictions = np.dot(X, theta)
    return(predictions)

def gradient_descent(X, y, theta, alpha, m):
    ''' Gradient descent algorithm'''
    predictions = hypothesis(X,theta)
    res = sum((predictions - y) * X)
    res = res[np.newaxis]
    theta = theta - (alpha * (1/m) * res.T)
    return(theta)

def cost_function(X, y, theta):
    '''Goal is to minimize this function'''
    predictions = hypothesis(X, theta)
    sqrt_error = sum(np.square(predictions - y))
    cost = (1/(2*m)) * sqrt_error
    return(cost)

if __name__ == "__main__":
    ''' Variable initialisation'''
    X, y = load_data_matrix_from_csv('data.csv')
    X = feature_scaling_with_mean_normalization(X)
    theta = np.array([[0],[0]])
    alpha = 0.1
    m = y.size
    num_iter = 4000
    cost = 0
    cost_history = np.array([])

    for i in range(0, num_iter):
        theta = gradient_descent(X, y, theta, alpha, m)
        cost_history = np.append(cost_history, cost_function(X, y, theta))
    np.savetxt("theta_file.csv", theta, delimiter=",")
    plot_data(X, y, theta, cost)