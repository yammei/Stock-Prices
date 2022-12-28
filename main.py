#This project is to teach the program - given historical stock data - how to predict the movement of current stocks.
#Oversight: in a volatile world, the program cannot predict unexpected events that may greatly skew future predictions.

from request import *

def main():
    result = retrieve_stocks(input("Name: "))
    for item in result:
        print(item)

if __name__ == "__main__":
    main()