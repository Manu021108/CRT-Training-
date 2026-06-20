#Problem statement:

#Take 3 sides from user and check 
#whether triangle is 
# 1.Isosceles --> two sides are equal
# 2.Equilateral --> all sides are equal
# 3.Scalene  -->3 diff sides 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the Third number:"))

#If all sides are equal 
if a == b and b == c:
    print("Equilateral triangle")
#Two sides should be equal     
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("scalene")        