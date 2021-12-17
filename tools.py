import csv
import sys

def read_data(filename):
    try:
        with open(filename) as csvfile:
         reader = csv.DictReader(csvfile)
         array = [row for row in reader]
        return(array)
        
    except:
        sys.exit("Error: can't read input data file")

def create_thetafile(header, array_of_theta):
    with open('theta_file.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        writer.writerow(header)
        writer.writerow(array_of_theta)

# header = ['row1', 'row2']
# array_of_theta = ['0.123', '12.4']

# create_thetafile(header, array_of_theta)
# read_data("theta_file.csv")

#read_data("data.csv")