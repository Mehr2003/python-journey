income = int(input("How much money did you make?"))
cost = int(input("How much did you spend?"))
profit = income - cost
print ("profit=", profit)

if profit>0:
    print("You saved money!")
elif profit==0:
    print("You broke even!")
else:
    print("You spent more than you earned!")


