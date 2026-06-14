#symbol = ["AAPL", "SMSNG", "MZRTI"]
#prices = [3000, 2500, 7600]

symbol_and_price = (("AAPL", 3000), ("SMSNG", 2500), ("MZRTI", 7600))

most_expensive = None
highest_price = -1

for symbol, price in symbol_and_price:
    if price > highest_price:
        highest_price = price
        most_expensive = symbol
print("most expensive symbol:", most_expensive)
print("price:", highest_price)