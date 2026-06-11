stocks={
    "stock1":{
        "symbol" : "SMSNG",
        "price" : 600,
        "sector" : "samsung"
    },
    "stock2":{
        "symbol" : "AAPL",
        "price" : 1000,
        "sector" : "apple"
    },
     "stock3":{
        "symbol" : "NKI",
        "price" : 760,
        "sector" : "nokia"
    },
     "stock4":{
        "symbol" : "CHVRLT",
        "price" : 3400,
        "sector" : "chevorlett"
    },
     "stock5":{
        "symbol" : "MZRT",
        "price" : 2500,
        "sector" : "maserati"
    }
}
#print(stocks)

highest_stock = stocks["stock1"]["symbol"]
highest_price = stocks["stock1"]["price"]

for key, stock in stocks.items():
    if stock["price"] > highest_price:
        highest_price = stock["price"]
        highest_stock = stock["symbol"]

print("most expensive symbol:", highest_stock)

lowest_stock = stocks["stock1"]["symbol"]
lowest_price = stocks["stock1"]["price"]

for key, stock in stocks.items():
    if stock["price"] < lowest_price:
        lowest_price = stock["price"]
        lowest_stock = stock["symbol"]
print("cheapest symbol:", lowest_stock)