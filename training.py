import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import sys

def show_all_datas(X, y, theta, cost):
    print("X: ", X)
    print("--------")
    print("y: ", y)
    print("--------")    
    print("theta: ", theta)
    print("--------")
    print("cost:", cost)

def plot_data(X, y, theta, cost, cost_history, num_iter, initial_X):
    predictions = hypothesis(X, theta)
    fig, ax = plt.subplots(2, 2)
    fig.suptitle('Results of Training')
    ax[0,0].set_title('Linear regression:')
    ax[0,0].scatter(X[:,1], y)
    ax[0,0].plot(X[:,1], predictions, color='red')
    ax[0,1].set_title('Cost function:')
    ax[0,1].scatter(range(0, num_iter), cost_history)
    ax[1,0].set_title('Data repartition:')
    hx, hy, _ = ax[1,0].hist(initial_X, bins=50,color="lightblue")
    ax[1,0].grid()

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
    try:
        X, y = load_data_matrix_from_csv('tests/data.csv')
        initial_X = X[:,1]
        print(initial_X)
        X = feature_scaling_with_mean_normalization(X)
    except:
        sys.exit('Error: Impossible to load data csv file')
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
    # print(X)
    plot_data(X, y, theta, cost, cost_history, num_iter, initial_X)