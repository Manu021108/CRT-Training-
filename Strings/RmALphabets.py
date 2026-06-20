'''Problem:5
Remove all characters except alphabets 

Example: 
input: "he123@lo"
output:"hello"

Logic Flow:
           1.Traverse over the string 
                     |
            2.Keep only the alphabets   
            '''    

# Input = h e 1 2 3 @ l o
#    i  = 0 1 2 3 4 5 6 7
#    i=7
result =""

string = input("Enter the string: ")

for ch in string:
    if ch.isalpha():
       result = result+ch
            #   = helo
print(result)       
       
       
'''
Problem-6

Remove spaces without using strip 

Example: 
input : Hell o 
output: Hello


string = input()

result = ""

for ch in string:
    if ch !=" ":
       result = result+ch
print(result)       

'''
string = input()

result = ""

for ch in string:
    if ch !=" ":
       result = result+ch
print(result)    
        
'''
Problem:7 

remove the brackets from algebraic expressions

Example: 
input: (a+b)*{c+d}
output: a+b*c+d

expression = input()

result = ""

for ch in expression:
   if ch not in "{}[]()":
       result +=ch
print(result)  

Problem:8

Sum of numbers in a string:

INput: hel123o
output: 6     

logic: traverse string-->
identify digits-->do sum and print

'''
string = input("Enter the string:")

total = 0

for ch in string:
    if ch.isdigit():
        total += int(ch)
        
print(total)        



        
