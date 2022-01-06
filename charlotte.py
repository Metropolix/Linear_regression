def    gradient_descent(X, y, theta):
    ''' Try to estimate theta's '''

    predictions = theta[0] * 1 + theta[1] * x;

    sqrt_error = sum((predictions - y) .^2);

    cost = 1/(2*m) * sqrt_error; % Zero :D


    theta[0] = theta[0] - a * (1/m * sum((predictions - y) * x[0])
    theta[1] = theta[1] - a * (1/m * sum((predictions - y) * x[1])
    return (theta)


''' Variables initialisation'''
X = [2,3,4,5];
y = [3,4,5,6]; 
theta = [0; 0];
m = length(y);
number_of_iteration = 5;

''' Gradient descent loop'''
for i in range(number_of_iteration):

	theta = gradient_descent(X, y, theta)
	cost = 1/(2*m) * sqrt_error; % Zero :D



