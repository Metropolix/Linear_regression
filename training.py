from traceback import print_tb
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import sys
import tools

def plot_data(X, y, theta, cost, cost_history, num_iter, initial_X):
    ''' Plot Linear Regression, Cost function and Data repartition'''
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
        X, y = tools.load_data_matrix_from_csv(sys.argv[1])
        initial_X = X[:,1]
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
    print("\033[92mDone.\033[0m Please open 'theta_file.csv' to know the slope and the intercept")
    plot_data(X, y, theta, cost, cost_history, num_iter, initial_X)
