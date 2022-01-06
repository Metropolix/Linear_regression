def hypothesis(X, theta):
    predictions = theta[0] * 1 + theta[1] * X
    return predictions

def cost_function(m, X, y, theta):
    ''' Calcul cost'''
    predictions = hypothesis(X, theta)
    sqrt_error = sum((predictions - y) .^2)
    cost = 1/(2*m) * sqrt_error
    return (cost)

def    gradient_descent(step, X, y, theta):
    ''' Try to estimate theta's '''

    sum_0 = 0
    sum_1 = 0
    for xi in range(X):
        predictions = hypothesis(xi, theta)
        for yi in range(y):
            sum_0 += (predictions - yi) * xi
            sum_1 += (predictions - y) * xi

    theta[0] = theta[0] - step * (1/m * sum((predictions - y) * x[0]))
    theta[1] = theta[1] - step * (1/m * sum((predictions - y) * x[1]))
    return (theta)


''' Variables initialisation'''
X = [[1, 2],[1,3],[1,4],[1,5]]
y = [3,4,5,6]; 
theta = [0; 0]
m = length(y)
number_of_iteration = 5
step = 0.01

''' Gradient descent loop'''
for i in range(number_of_iteration):

	theta = gradient_descent(X, y, theta)
    cost = cost_function(X, y, theta)
    print(cost)



