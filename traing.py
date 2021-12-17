import tools 

def linear_regression(data, theta0, theta1):
    i = 0
    j = 0
    learning_rate = 0.01
    estimate_price_gap = 0

    for counter, car in enumerate(data):
        print(counter)
        estimate_price = theta0 + (theta1 * float(car['km']))
        estimate_price_gap += estimate_price - float(car['price'])
  
    tmp_theta0 = learning_rate * (1/(counter+1)) * estimate_price_gap
    tmp_theta1 = learning_rate * (1/(counter+1)) * estimate_price_gap * float(car['km'])

if __name__ == "__main__":

    data = tools.read_data("data.csv")
    print(data[1])
    theta_file = tools.read_data("theta_file.csv")
    theata0 = float(theta_file[0]['row1'])
    theta1 = float(theta_file[0]['row2'])
    print(theta_file[0])
    linear_regression(data, theata0, theta1)