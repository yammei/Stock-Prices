from request import StockCreate as sc
import random
import csv

class MainFunction:

    def predict(ticker_list):

        with open(ticker_list, 'r') as file:

            i = 1
            reader = csv.reader(file)
            for row in reader:
                # print(str(row)[2:len(row)-3])
                ticker = str(row)[2:len(row)-3]
                print(ticker + " in progress.")
                sc.create_data(ticker, sc.stock_history(ticker))
                print(str(i) + " completed.")
                i += 1

        prediction = random.uniform(0, 150)
        prediction = round(prediction, 2)
        print(prediction)

    predict("TICKERS.CSV")
