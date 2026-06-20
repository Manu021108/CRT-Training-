#Largest of 4 numbers : 
#1.logical operators and conditionals 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the Third number:"))
d = int(input("Enter the fourth number:"))

if a >= b and a >= c and a >= d:
    print("a is larger")
elif b >= c and b>=a and b>=d:
    print("b is greater")
elif c >= a and c>= b and c >= d:
    print("c is greater")  
else:
    print("d is greater")          

#Task: Write the pseudocode for above program 

'''
START
Input a,b,c,d
IF a is greatest
   Display a 
ELSE IF b is greatest
   Display b   
ELSE IF c is greatest
   Display c
ELSE
   Display d
END          

'''

#Truthly or falsy statements 
if 0:
    print("hello")

#It will not execute 

#Short circuit evaluation 

if True or 10/0:
    print("safe")
    
#No -error and prints safe 

if True:
   print("hello")    
    
    
    