import csv
import sys

def read_data(filename):
    try:
        with open(filename) as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             print(row['km'], row['price'])
        return(row)
        
    except:
        sys.exit("Error: can't read input data file")

#read_data("data.csv")