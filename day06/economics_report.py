#grade1 = int(input("grade1:"))
#grade2 = int(input("grade2:"))
#grade3 = int(input("grade3:"))
#grade4 = int(input("grade4:"))
#grade5 = int(input("grade5:"))

grades = [18, 15, 20, 17, 19]
print (grades)


average = sum(grades)/len(grades)
print("your average=", average)
highest = grades[0]
lowest = grades[0]

for x in grades:
    if x > highest:
        highest = x
print("highest=", highest)

for i in grades:
    if i < lowest:
        lowest = i
print("lowest=", lowest)
        

    

#if i in grades:
 #   while grades[0] > grades[1]:
  #      print ("highest =", grades[0])
   # else:
    #    print("highest=", grades[1])
        

    






    


