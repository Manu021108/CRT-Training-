'''
What is function?
Function is a block of reusable code.Performs 
specific task 

why functions?
1.AVoid repetition 
2.Improves readabilty
3.Easy Debug 
4.Modular programming 

#function definition 

def function_name(Parameters):
    """Doc strings"""
    statements 
    return value 
    
    def --> keyword 
    function_name -->identifiers
    parameters -->Input 
    return -->Output

#Function calling:Executing the code 

function_name()

Funtions are        two types     
                    /              \
            Built IN func  User defined functions
            
BuiltIn functions: which are already defined 
Example:  print()
input()
sum()
mean()
max()            
UserDefined Functions:we will create our logic 
as per our requirement 

'''
#Create a function 
def hello():
    print("Hello world")
    
#call the funct
hello()

#Parameters:variable passed during
# the function definition  

def add(a,b): #a,b are parameters 
    print(a+b)  

#arguments = values passed during function call 
#calling the function 
add(2,3)  #2,3 -- arguments 

'''
Types of arguments:
1.Positional arguments:
arguments passed in order 

Example: 
def multiply(a,b):
    return a*b
    
#call the function 
multiply(2,3)

#Task:Create a function to calculate
simple interest  using positional args 

3.Keyword arguments 

def sub(a,b):
    return a-b 
    
sub(b=5,a=10)




'''
#Keyword arguments
def sub(a,b):
    print(a-b) 
    
sub(b=5,a=10) #No order 

#Task:call the simple interest funct
# using keyword arguments

'''
3.Default arguments :used when value is not provided 

Example: 

def student(name = "Manish"):
    print(f"Student name is {name}")



'''
def student(name,branch="CSE"):
    print(f"Student name is {name} and branch is {branch}")
    
student("Rajesh")    

#output:

#Task: create a function to calc
# squares by defualt parameters 
def square(a,b=2):
    print(a**b)
square(10) 

'''
#Variable length arguments 

def total(*args):
    print(args)
    
#Call the function 
total(10,20,30,40)    


'''
def total(*args):
    print(args)
    print(sum(args))
    
#Call the function 
total(10,20,30,40)  

#Task: Create a function to find sum of any number 
#of values

'''
#kwargs -->keyword arguments 

def student_details(**kwargs):
     print(kwargs)
     
student_details(name="Rajesh",branch="CSE",roll="09")     





'''
def student_details(**kwargs):
     print(kwargs)
     
student_details(name="Rajesh",branch="CSE",roll="09") 

#create a function to print employee details
#using kwargs
#Task: write args and kwargs together 

def together(*args,**kwargs):
    print(args,kwargs)
    
'''
return statement: send the value 
back to the caller 

def add(a,b):
   return a+b
   
result = add(10,20)
print(result)

Print             |  return 
display the output   sends the value
cannot reuse         can reuse

Mutiple return values:

def calculate(a,b):
    return a+b,a-b,a/b

format: tuple

s,sub,div = calculate(20,30)




'''
def calculate(a,b):
    return a+b,a-b,a/b

# format: tuple

s,sub,div = calculate(20,30)
print(s,sub,div)

#Task:Create a function that returns 
#1.Min,2.Max,3.avg of the numbers 

'''
#function doc strings

doc strings describes:
1.what function does
2.parameters 
3.return value 

def add(a,b):
    """This function adds two numbers 
    and returns result"""
    return a+b



'''
def add(a,b):
    """This function adds two numbers 
    and returns result"""
    return a+b

print(add.__doc__)
print(help(add))

#TAsk:write a docstring for
# the simple interest program 

'''
Variable scopes:

#1.Local scope:
Variables declared inside the function 

def test():
   x = 100
   print(x)

#Gloabal scope: outside the function

x = 100
def show():
   print(x)



'''
def test():
   x = 100  #local var
   print(x)
   
test()   

x = 200   #global variable 
def show():
   print(x)
   
show() 

#accessing the local var outside the function
x = 0

def update():
    global x
    x = x+5
    
update() 
print(x)   #5

#Task: Try without using global and tell me error

'''
TasK:
create a function bank_transaction()
which accepts:
1.account holder (string)
2.balance 
3.transaction_type(deposit/withdraw)
4.amount 

use:
default arguments
return statement 
global balance
print updated balance 
'''
balance = 1000
def bank_transaction(account_holder,transaction_type,amount=0):
    global balance #to modify balance 
    if transaction_type == "deposit":
        balance += amount
        print(f"{account_holder} deposited{amount}")
    elif transaction_type == "withdraw":
        if amount <= balance:
            balance -= amount
            print(f"{account_holder} withdraw {amount}")
        else:
            print(f"Insufficient balance for {account_holder}")
    else:
        print("Invalid transaction type")
        
    print(f"Updated Balance {balance}")  
    return balance  

bank_transaction("Manish","deposit",500)
  
'''
Lambda Function: is a small and anonymous function
#function without name 
#defined using lambda 
can pass any number of arguments 
can have only one expression
returns the value automatically (no return keyword)

Normal Function:

def add(a,b):
   return a+b
   
add(10,20)   
   
#write using lambda 

add = lambda a,b:a+b  

#calling the function
add(10,20) 

#Task:Write a normal funct to square of num
convert the normal fun to lambda 



'''
print((lambda x:x*x)(5))

#Max number in 2 
#c - programming 
#ternary :  ? :
#python: a if a>b else b
max_num = lambda a,b:a if a>b else b

'''
arr = list(map(int, input().split()))

#map():applies the function each
# element of iterable

map(function,iterable)

Example:
def square(x):
    return x*x
    
nums = [1,2,3,4]  
result = list(map(square,nums))
print(result)  


'''
def square(x):
    return x*x
    
nums = [1,2,3,4]  
result = list(map(square,nums))
print(result)  

#write with lambda 
nums = [1,2,3,4]  
result = list(map(lambda x:x*x,nums))
print(result)  

#Task:Given a list of numbers
#Convert each number into cubes 
# using map() and lambda

'''
what is filter?
selects the elements based upon the condition

syntax:
filter(function,iterable)

Ēxample:
def is_even(x):
   return x%2==0

list = [1,2,3,4,5]
result = filter(is_even,list)
print(result)

#Task: Given with a list with frnds names 
#filter the names letter starting with A
#use filter with lambda

n
'''
names = ["Anu","Amit","Rajesh"]
result = list(filter(lambda x:x.startswith("A"),names))
print(result)

'''
what is reduce()?
Repeatedly applies function
Reduces the iterable to single value 
Synatax:

reduce(function,iterable)


'''
# functools  ---> module

from functools import reduce

nums = [1,2,3,4,5]
result = reduce(lambda a,b:a+b,nums)
print(result)


# https://assessments.prepinstaprime.com
# /CITY/dashboard/startTest/CITY00024

#passcode:99448