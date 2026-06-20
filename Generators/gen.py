'''
Youtube: doesn't loads the whole video 
loads by:
small chunks 
when neeeded 

simply generators work in the same format 

Problem with list:
list =[1,2,3,4,5]

entire list is stored in memory 

nums = [i for i in range(100000)]

Python consumes :
high memory 
slower

Generator:
produces values one at a time 
only when it is needed 
saves memory 

Yield keyword:
yield pauses the function 
and remembers the state 

return: ends the function
yield: pauses the function 


'''
#Example:
def numbers():
    yield 1
    yield 2
    yield 3
x = numbers()
print(x)

#access the numbers 
print(next(x))
print(next(x))
'''
numbers()  #call
|
generator created 

1.first next()
yield 1 --> 1
function paused 

2.second next()
resume from previous position
yield 2 ---> 2
function pause 

3.third next()
resume from previous position
yield 3 --> 3
pause again

Generators:
remembers the variables 
remember line position 
continue from the same place 

#Diff between return and yeild 
return                   Yeild 
Ends the function          pauses the function
returns sigle value  will return mutiple values 
by one
No state memory          remebers the state 
'''
def test():
    return 1
    return 2 

print(test())

#with yield
def numbers():
    yield 1
    yield 2 

for i in numbers():
    print(i)
    
#For loop uses iter(),next() internally  

#create a generator for even numbers 

def even_numbers(limit):
    
    num = 2
    while num <= limit:
        yield num
        num +=2
        
        
x = even_numbers(10) 
for i in x:
    print(i)
'''
num = 2  --> yeild 2  ->2
pause

resume
num = 4 --> yeild 4  ->4
pause

resume 
num = 6 --> yeild 6 ->6
pause 

#Memory Efficiency 

nums = [i for i in range(10000)]

Generator 
nums = (i for i in range(1000000))
only the current value 

#Lazy evaluation

Values are generated when neede 
generators are lazy 

#Write a program for fibonacci using 
generators 

 



'''
def fibonacci(limit):
    
    #first two numbers 
    a = 0 
    b = 1
    
    #loop until the limit 
    while a<= limit:
        #generate the current value 
        yield a 
        #update the values 
        a, b = a+b   
        
x = fibonacci(20)

for i in x:
    print(i)              