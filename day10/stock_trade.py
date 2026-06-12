price = int(input("what price did you buy it?"))
sell = int(input("what price did you sell it?"))

def profit_or_loss (price, sell):
    return sell-price
if sell-price > 0:
    print ("your profit=", profit_or_loss(price, sell))
elif sell-price ==0:
    print ("you didn't get any profit=", profit_or_loss(price,sell) )
else:
    print("your loss =", profit_or_loss(price, sell))
