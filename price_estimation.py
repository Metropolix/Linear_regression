import tools
import sys

if __name__ == "__main__":
    
    if (sys.argv[0]):
        filename = sys.argv[0]
    else:
        filename = "data.csv"
    data = read_data(filename)

    print(sys.argv[0])