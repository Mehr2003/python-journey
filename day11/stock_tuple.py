stocks = (("AAPL", 2500), ("SMSNG", 3000), ("MZRTI", 7000))
print(stocks)

most_expensive = None
highest_price = -1

for symbol, price in stocks:
    if price > highest_price:
        highest_price = price
        most_expensive = symbol
print("most expensive:", most_expensive)
print("price:", highest_price)