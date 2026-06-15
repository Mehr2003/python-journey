stocks = (("SMSNG", 4500), ("MZRTI", 8900), ("AAPL", 5200), ("CHVRLT", 9000))

def most_exp(stocks):
    most_expensive_symbol = None
    highest_price = -1
    for symbol, price in stocks:
        if price > highest_price:
            highest_price = price
            most_expensive_symbol = symbol
    return most_expensive_symbol, highest_price
result = most_exp(stocks)
print("most expensive symbol:", result[0])
print("price:", result[1])