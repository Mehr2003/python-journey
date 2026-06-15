stocks = (("AAPL", 3500), ("MZRTI", 7600), ("SMSNG", 2400))
#(stock1, stock2, stock3) = stocks
#prices = stock1[1], stock2[1], stock3[1]
#symbols = stock1[0], stock2[0], stock3[0]



def find_highest_stock(stocks):
    most_expensive = None
    highest_price = -1

    for symbol, price in stocks:
        if price > highest_price:
            highest_price = price
            most_expensive = symbol
    return  most_expensive, highest_price
result = find_highest_stock(stocks)
find_highest_stock(stocks)
print("most expensive symbol:", result[0])
print("price:", result[1])