def hypothesis(X, theta):
    predictions = theta[0] * 1 + theta[1] * X
    return predictions

def get_sqrt_error(X, y, theta):
    sum = 0
    for xi in X:
        predictions = hypothesis(xi[1], theta)
        for yi in y:
            sum += (predictions - yi) ** 2
    return sum

def gradient_descent(step, X, y, theta):
    ''' Try to estimate theta's '''

    sum_0 = 0
    sum_1 = 0
    for xi in X:
        predictions = hypothesis(xi[1], theta)
        for yi in y:
            sum_0 += (predictions - yi) * xi[0]
            sum_1 += (predictions - yi) * xi[0]

    theta[0] = theta[0] - step * (1/m * sum_0)
    theta[1] = theta[1] - step * (1/m * sum_1)

    return (theta)

def cost_function(m, X, y, theta):
    ''' Calcul cost'''
    sqrt_error = get_sqrt_error(X, y, theta)
    cost = 1/(2*m) * sqrt_error
    return (cost)

''' Variables initialisation'''
X = [[1, 2],[1,3],[1,4],[1,5]]
y = [3,4,5,6]
theta = [0, 0]
m = len(y)
number_of_iteration = 1000
step = 0.01

''' Gradient descent loop'''
for i in range(number_of_iteration):
    theta = gradient_descent(step, X, y, theta)
    cost = cost_function(m, X, y, theta)
    # print(theta)
    print(cost)

