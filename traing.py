import tools 

def gradient_descent(data, array_of_theta):
    i = 0
    j = 0
    learning_rate = 0.01
    tmp_deriv_0 = 0
    tmp_deriv_1 = 0

    for counter, car in enumerate(data):
            print(counter)
            estimate_price = array_of_theta[0] + (array_of_theta[1] * float(car['km']))
            tmp_deriv_0 += estimate_price - float(car['price'])
            tmp_deriv_1 += (estimate_price - float(car['price'])) * float(car['km'])

    array_of_theta[0] -= learning_rate * (1/(counter+1)) * tmp_deriv_0
    array_of_theta[1] -= learning_rate * (1/(counter+1)) * tmp_deriv_1
    print( array_of_theta[0], array_of_theta[1])
    return (array_of_theta)

def linear_regression(data, theta0, theta1):
    number_of_iterations = 10

    array_of_theta = [theta0, theta1]
    for i in range(number_of_iterations):
        array_of_theta = gradient_descent(data, array_of_theta)
        print(array_of_theta[0], array_of_theta[1])
    estimate_price = array_of_theta[0] + (array_of_theta[1] * float(data[1]['km']))
    print( estimate_price, data[1]['price'])
    print(array_of_theta[0], array_of_theta[1])



if __name__ == "__main__":

    data = tools.read_data("data.csv")
    print(data[1])
    theta_file = tools.read_data("theta_file.csv")
    theata0 = float(theta_file[0]['row1'])
    theta1 = float(theta_file[0]['row2'])
    print(theta_file[0])
    linear_regression(data, theata0, theta1)