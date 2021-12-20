import tools 

def hypothesis (theta_0,theta_1,X):
    return theta_1*X + theta_0

def cost_function(data,theta_0,theta_1):
    m = len(data)
    summation = 0.0
    for i in range (m):
        summation += ((theta_1 * float(data[i]['km']) + theta_0) - float(data[i]['price']))**2
    return summation /(2*m)

def gradient_descent_v2(data, array_of_theta):
    t0_deriv = 0
    t1_deriv = 0
    m = len(data)
    theta_1 = array_of_theta[1]
    theta_0 = array_of_theta[0]
    learning_rate = 0.00000001

    # print(float(data[0]['km']))
    
   # print("theta0 = %s , theta1 = %s", theta_0, theta_1)
    for i in range (m):
        t0_deriv += hypothesis(theta_0, theta_1, float(data[i]['km'])) - float(data[i]['price'])
        t1_deriv += (hypothesis(theta_0, theta_1, float(data[i]['km'])) - float(data[i]['price'])) * float(data[i]['km'])
        # print("t0_deriv, t1_deriv:", float(data[i]['km']), float(data[i]['price']))
        print(t0_deriv)

    theta_0 -= (1/m) * learning_rate * t0_deriv 
    theta_1 -= (1/m) * learning_rate * t1_deriv
    
    
    array_of_theta = [theta_0, theta_1]
    # print(t0_deriv, t1_deriv)
    # print(array_of_theta, m,)
    return array_of_theta

def gradient_descent(data, array_of_theta):
    learning_rate = 0.000001
    tmp_deriv_0 = 0
    tmp_deriv_1 = 0

    for counter, car in enumerate(data):
            estimate_price = array_of_theta[0] + (array_of_theta[1] * float(car['km']))
            tmp_deriv_0 += estimate_price - float(car['price'])
            tmp_deriv_1 += (estimate_price - float(car['price'])) * float(car['km'])
            #i print(estimate_price, car['km'])
            print(tmp_deriv_0, tmp_deriv_1)
            print("AAAAAAAAA")
    array_of_theta[0] -= learning_rate * (1/(counter+1)) * tmp_deriv_0
    array_of_theta[1] -= learning_rate * (1/(counter+1)) * tmp_deriv_1
                # print(tmp_deriv_0, tmp_deriv_1)

 #   print( array_of_theta[0], array_of_theta[1])
    return (array_of_theta)

def linear_regression(data, theta0, theta1):
    number_of_iterations = 100

    array_of_theta = [theta0, theta1]
    for i in range(number_of_iterations):
        array_of_theta = gradient_descent_v2(data, array_of_theta)
        print(cost_function(data, array_of_theta[0], array_of_theta[1]))
  #  print(array_of_theta[0], array_of_theta[1])



if __name__ == "__main__":

    data = tools.read_data("data.csv")
    print(data[1])
    theta_file = tools.read_data("theta_file.csv")
   # thesta0 = float(theta_file[0]['row1'])
  #  theta1 = float(theta_file[0]['row2'])
  # print(theta_file[0])
    theta0 = 1
    theta1 = 90000000
    linear_regression(data, theta0, theta1)