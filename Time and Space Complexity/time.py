'''
Analogy:

You are given with 2 programs where it is generating 
the same output

how will you decide which one to use ?
1.Faster program 
2.Less memory 
3.Efficient 

#Algorithmic complexity == efficiency 

Two types:
1.Time Complexity: faster results in google

2.Space complexity: 

                       Mark-zukerberg -->CSS 20kb
                       /          \
                     A = 19kb      B = 18kb 1kb 
                       10LPA         30LPA

               DAU===> 200cr 
               70 lakhs --20Lakhs --50Lakhs 
    
Time complexity?

Time complexity measures how the running
time grows as the size of input   

3 - Techniques to measure time complexity 

 

'''
#Stop watch method:
import time 

start = time.time()

for i in range(1,101):
    print(i)
    
print(time.time()-start)    

'''
#Problems in above technique

1.different systems diff time 
2.Different compilers/diff interpreters 
3.background apps effect time 
4.Internet/cpu/GPU/ affect the performance 
'''
#Technique-2 Counting the num of operations 
    
#Not measures the time in seconds but counts operations 

def c_to_f(c):
    return c*9/5+32

# mul = 1
# div = 1
# add = 1  operations = 3

#Example-2

def mysum(x):
    total = 0  #--> 1 op 
    for i in range(x+1):  
        total = total+i  #2 op 
        
    return total 

   
        #x ---> input 
        
        # 1+2X  x=10 --->21 operations 
        
        
#Techniqiue- 3 Order of growth 

'''
Notations:
Asymptotic Notations 

1.Big Oh o():Calc the upper bound (Worst time complexity)
2.Omega Notaion : Best case complexity 
3.Theta : avg case complexity 

#EXample: Linear search 

arr = [1,2,3,4,5,6,7]

arr[0] == target  # best case 
arr[4] == target #avg case 
arr[last] == target #worst case complexity 

Big Oh: worst time growth
Focus:
1.Measuring the scalability 
2.Machine Independent 
3.focuses on growth 
4.Ignores the hardware 


def mysum(x):
    total = 0  #--> 1 op 
    for i in range(x+1):  
        total = total+i  #2 op 
        
    return total 

   
        #n ---> input 
        
        # 1+2n  x=10 --->21 operations
        
Big Oh (Rules)
1.additive constants (remove)
       #1+2n  --->2n

2.multiplicative constant (remove)
       #2n ---> n
       
       time complexity --> O(n)

a = 10
b = 20 
c = a+b 


for i in range(1,101):

O(n)
++++  n+n+n = 3n -->n O(n)

Nested loops:
for i in range(1,n+1):
   for j in range(i):
       print(i)
       
       n*n ==>n^2  --> O(n^2)       
Equation:  n^2+n+10    --> n^2+n --> O(n^2)  

for i in range(1,100)
   print(i)
for j in range(1,50):
    print(j)
    
    n+n --> 2n   --> O(n)     

#Practice:

1.n^2+10000n+3^1000  

O(n^2)  


2.log(n)+n+4 

O(n)

3.0.0001*n*log(n) + 300n

O(nlog(n))

4.2n^30 + 3^n

O(3^n)

#Complexity classes 

1.Constant Time --> O(1)

_> same time always 

arr =[10,20,20]
arr[i]
  
-->Input increase and time stays constant 

2.Linear time -->O(n)

for i in arr:
   print(i)
       
#Grows along with input 

3.Quadratic time --->O(n^2) 
  
Nested loops:
for i in range(1,n+1):
   for j in range(i):
       print(i) 
       
#Outer loop runs n times and 
inner loop runs n time with outerloops 

4.Logarithmic Time ---> O(log(n))

Best Example: 

Binary search: 

arr = [1,6,8,3,7,10]
arr = [1,3,6,7,8,10]

n/2


#Large input: smaller growth 
#Very efficient

5.Linearithmic ---> O(n log(n))

#Better then quadratic 
#used in industry 

6.Exponential: --->O(2^n)

Very slow,not much used 

Example: recursive fibonacii

Dangerous for large input  

while n>1:
   n = n//2
   
#loop dividing 2 --> O(log(n))

#space complexity: Measures memory used by the algorithm 

1.Input space 
2.Auxiliary space 

Example:

a = 10 
b = 20 

constant space ---> O(1)

Example-2:

arr =[0]*n

linear space---> O(n)
          

'''
