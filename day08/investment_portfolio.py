stock1 = {
    "symbol" : "NKIA",
    "price" : 170
}

stock2 = {
    "symbol" : "SMSNG",
    "price" : 100
}

stock3 = {
    "symbol": "AAPL",
    "price" : 200
}

total = (stock1["price"] + stock2["price"] + stock3["price"])
print ("total=", total)

stocks= [(stock1["symbol"], stock1["price"]), (stock2["symbol"], stock2["price"]), (stock3["symbol"], stock3["price"])]
#print(stocks)

highest = stock1["symbol"], stock1["price"]
for x in stocks:
       if x[1]>highest[1]:
        highest=x
print("Most expensive symbol:", highest[0])
print ("highest price=", highest[1])

lowest = stock1["symbol"], stock1["price"]
for i in stocks:
    if i[1]<lowest[1]:
        lowest=i
print("Cheapest symbol:", lowest[0])
print("the lowest price=", lowest[1])