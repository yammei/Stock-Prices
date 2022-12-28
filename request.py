import yfinance as yf
import csv
import math
from datetime import datetime, timedelta

# INFO MENU OPTIONS: 
# open
# previousClose

class StockCreate():

  def stock_info(stock_symbol):

    company = yf.Ticker(stock_symbol)
    data = company.info[input("Please Input Info Option: ")]
    print(data)
    info = company.history(period = input("How Long: "))
    print(info)

  def stock_history(stock_symbol):
    company = yf.Ticker(stock_symbol)
    info = company.history(period = "30d", interval = "1h")
    data = []
    # print(info)
    # print(data["Open"])
    for item in info["Open"]:
      item_string = str(item).split(" ")
      item_string = item_string[0:]
      result = " ".join(item_string)
      result = round(float(result), 2)
      data.append(result)
    # for item in data:
    #   print(item)
    return data

  def create_data(company, data):
    file_pathway = "/Users/EvelynZhang/Project1/Stock_Data/" + str(company) + ".csv"
    with open(file_pathway, "w") as file:
      writer = csv.writer(file)
      for item in data:
        print(str(item))
        writer.writerow([item])
