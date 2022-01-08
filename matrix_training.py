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

def hypothesis(X, theta):
    predictions = np.dot(X, theta)
    return(predictions)

def gradient_descent(X, y, theta, alpha, m):
    ''' Gradient descent algorithm'''
    predictions = np.dot(X, theta)
    res = sum((predictions - y) * X)
    res = res[np.newaxis]
    theta = theta - (alpha * (1/m) * res.T)
    return(theta)

def cost_function(X, y, theta):
    '''Goal is to minimize this function'''

    predictions = np.dot(X, theta)
    sqrt_error = sum(np.square(predictions - y))
    cost = (1/(2*m)) * sqrt_error

    return(cost)

if __name__ == "__main__":
 
    ''' Parsing'''
    my_data = genfromtxt('test_decrement.csv', delimiter=',')
    my_data = np.delete(my_data, (0), axis=0)
    my_data = my_data[np.argsort(my_data[:, 0])]

    X, y = np.split(my_data, 2, axis=1)
    b = np.ones((y.size,1))
    X = np.hstack((b,X))

    ''' Variable initialisation'''
    theta = np.array([[0],[0]])
    alpha = 0.001
    m = y.size
    num_iter = 700
    cost = 0
    cost_history = np.array([])

    # show_all_datas(X, y, theta, cost)
    ''' Feature scaling'''

    ''' Cost function'''
    cost = cost_function(X, y, theta)
    print(cost)

    ''' Gradient descent'''

    for i in range(0, num_iter):
        cost = cost_function(X, y, theta)
        theta = gradient_descent(X, y, theta, alpha, m)
        
        cost_history = np.append(cost_history, cost_function(X, y, theta))
    
    print(cost_history)
    print(theta)
    ''' Predictions'''
    predictions = hypothesis(X, theta)
    # print(predictions)
    ''' Plot data'''
    plt.scatter(list(range(0,num_iter)), cost_history)
    # plt.scatter(X[:,1], y)
    # plt.scatter(X[:,1], predictions, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()