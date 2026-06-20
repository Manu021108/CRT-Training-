'''
Decorators:
adds the extra functionality 
without changing the original function 

Gift Wrapper:

wrapper adds: 
extra layer ,beauty 

decorator = wrapper around the function

#why decorators are needed?
logging:
authentication,
timing
validation 

if no decorators 
1.repeated code 
2.messy programs 


'''
def greet():
    print("hello students")
    
#In python --functions are 
# treated like variables

def greet():
    print("hello students") 
    
x = greet    
x()

#nested functions 

def outer():
    def inner():
        print("Inner side")
        
    inner()
outer() 

#returning the function 
def outer():
    def inner():
        print("Inner side")
        
    return inner
x = outer
x()
'''
outer() called 
|
returns the inner 
|
stored in x
|x()-->executes inner 

'''
#simple decorator 
def decorator_function(original_function):
    
    def wrapper():
        print("Before function call")
        original_function()
        print("After function call")
        
    return wrapper    
    
#Original function:
def greet():
    print("Hello students") 
    
#apply manually 
decorated = decorator_function(greet)   
decorated() 

'''
greet()
|
decorator_function()
|
wrapper created 
|
extra functionality is added 

shortcut syntax:
special symbol : @

'''

@decorator_function
def greet():
    print("Hello students") 
    
#Example:2
def smart_divide(func):
    def wrapper():
        print("Checking before div")
        func()
        print("Division is completed ")
        
    return wrapper

@smart_divide
def divide():
    print(10/2)
    
divide()    

#Example:3
# @decorator_function
# def greet(name):
#     print("hello",name)

# greet()  #Fail 

def decorator_function(original_function):
    
    def wrapper(name):
        print("Before function call")
        original_function(name)
        print("After function call")
        
    return wrapper

@decorator_function
def greet(name):
    print("hello",name)

greet("Manish")

#Timer decorator

import time 

def timer(func):
    def wrapper():
        start = time.time()
        func() 
        end = time.time()
        print("Execution time",end-start)
    return wrapper
@timer
def test():
    for i in range(10000):
        pass
    
test()

#Example:2

def login_required(func):
    def wrapper():
        print("Checking the user login")
        func()
        
    return wrapper   

@login_required
def dashboard():
    print("welcome to dashboard")
    
dashboard() 
