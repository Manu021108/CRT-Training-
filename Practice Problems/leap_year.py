# write a program to check whether a given year 
# is leap or not 
# Conditions 
# 1.divisible by 400
# or divisible by 4 
# and should not divisible by 100

year = int(input("Enter the year:"))

#Leap year condition:

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    #print the leap year 
    print("Leap year")
else:
    print("Not a leap year")    
