import numpy as np
from numpy import genfromtxt

def test_numpy():
    M1 = np.array([[3, 6, 9], [5, -10, 15], [-7, 14, 21]])
    M2 = np.array([[9, -18, 27], [11, 22, 33], [13, -26, 39]])
    M3 = M1 + M2  
    print(M1, M2, M3)

def show_all_datas(X, y, theta, cost):
    print("X: ", X)
    print("--------")
    print("y: ", y)
    print("--------")    
    print("theta: ", theta)
    print("--------")
    print("cost:", cost)

if __name__ == "__main__":
 
    ''' Parsing'''
    my_data = genfromtxt('data.csv', delimiter=',')
    my_data = np.delete(my_data, (0), axis=0)
    X, y = np.split(my_data, 2, axis=1)
    b = np.ones((y.size,1))
    X = np.hstack((b,X))
    print(X)
    ''' Variable initialisation'''

    theta = np.array([[0],[0]])
    alpha = 0.01
    m = y.size
    num_iter = 1000
    cost = 0

    # show_all_datas(X, y, theta, cost)

    ''' Cost function'''

    predictions = np.dot(X, theta)
    sqrt_error = sum(np.square(predictions - y))
    cost = (1/(2*m)) * sqrt_error

    ''' Gradient descent'''