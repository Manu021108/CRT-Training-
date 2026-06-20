'''
Iterators:
Gives one element at a time 
on demand 

Python referes iterators:
memory efficiency 
controlled access 

Iterable:is an object can be looped 
1.list
2.tuple
3.set
4.dict 
5.string 

Examples:
nums = [10,20,30,40]
                  P

for x in nums:
   print(x)
   
#syntax:

iterable_object = [1,2,3,4]
it = iter(iterable_object)   
print(it)

iterable--->iterator




'''
iterable_object = [1,2,3,4]
it = iter(iterable_object)   
print(it)
print(next(it))
#element printed then pause
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
'''
list
 |
 iter()
 |
 Iterator
 

 
 nums = [1,2,3,4]
        P
for x in nums:
    print(x)
    
it = iter(nums)
while True:
   try:
      x = next(it) 
      print(x)
   except StopIteration:
      break      
        
        
How loop in python works internally
iterators ---will be used internally 
iter(),next()        

'''
nums = [1,2,3,4]
it = iter(nums)
while True:
   try:
      x = next(it) 
      print(x)
   except StopIteration:
      break
  
'''
nums = [2,3,4]

it = iter(nums)

print(next(it)) #2
print(next(it)) #3
print(next(it)) #4
print(next(it)) #StopIteration

name = "Python"

it = iter(name)
print(next(it)) #P #string object 


t = (1,2,3)
it = iter(t)
print(it) #string object #(1,2,3)
#tuple iterator object 

d = {"a":10,"b":20}

it = iter(d)
print(next(it))



    '''
d = {"a":10,"b":20}

it = iter(d)
print(next(it))

#Iterator No:

nums = [i for i in range(100000)]

#huge memory 

#iterator approach 
nums = iter(range(100000))

#only the current element 
# will be processed 

#Creating a custom iterator 
#count 

class Count:
    #constructor 
    def __init__(self,limit):
        self.num = 1
        self.limit = limit
        
    def __iter__(self):
       return self   
    def __next__(self):
       if self.num > self.limit:
           raise StopIteration 
       x = self.num
       self.num +=1
       return x 
#object creation 
c = Count(5)

for i in c:
    print(i)

'''
#Create a custom iterator 
# for even numbers
'''
class EvenNumbers:
    #constructor method 
    def __init__(self,limit):
        self.num = 2
        #max limit
        self.limit = limit
    #This method makes the object iterable
    #it returns the iterator object itself 
    def __iter__(self):
        return self
    
    #next value during iteration
    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        
        x = self.num
        self.num += 2
        return x
    
e = EvenNumbers(10)

for i in e:
    print(i)