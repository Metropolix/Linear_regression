import tools
import sys

Theta0 = 0
Theta1 = 0

def km_estimation():
    global Theta0
    try:
        val = int(input("Enter a km value: "))
    except:
        sys.exit("Error: you must enter a digit")

    km_estim = Theta0 + (Theta1 * val)
    print(km_estim)
    Theta0 += 1

if __name__ == "__main__":

    if (len(sys.argv) >= 2):
        filename = sys.argv[1]
    else:
        filename = "data.csv"
    data = tools.read_data(filename)
    theta_file = tools.read_data("theta_file.csv")
    try:
        Theta0 = float(theta_file[0]['row1'])
        Theta1 = float(theta_file[0]['row2']) # TODO: Securisez le int
    except:
        sys.exit("Error: Failed to Read theta file must be number")
    
    km_estimation()