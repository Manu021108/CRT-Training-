'''


def function_name(parameters):
    """Docstring"""
    statements 
    return statement 
    
    def --> keyword
    function_name -->identifier
    parameters-->input
    return -->output
    
def hello():
    print("Hello")
    
#calling function 
hello()

#sum of two numbers 
def add(a,b):  #parameters 
    return a+b
    
#call 
add(2,3) #arguments 

#Types of arguments 
1.Positional arguments 
#sum of two numbers 
def add(a,b):  #parameters 
    return a+b
    
#call 
add(2,3) #arguments 

2.Keyword arguments 

#sum of two numbers 
def add(a,b):  #parameters 
    return a+b
    
#call 
add(b=2,a=3) #arguments

3.default parameters/arguments 

def greet(name="Manish"):
     print(f"Hello {name}")


 
4.var len arguments 
def total(*a):
    print(a)




5.keyword var len arguments 

#lambda functions:anonymous 
-->name less function
add = lambda a,b:a+b
add()

#Map
#filter
#reduce 
    
    



'''
def greet(age,name="Manish"):
     print(f"Hello {name}")
     
print(greet("Ramesh"))

#var-len arguments 
def total(*a):
    print(a)

total(1,2,3,4,5,6)

#keyword var len arguements 
def total(**b):
    print(b)
    
total(a=10,b=20,c=30)

'''
Recursion is a programming technique where 
a function calls itself to solve smaller versions of the 
same problem 

function -> calls itself --> again -->again

1.Base case 
condition where the recursion stops 

2.Recursive case:
function calls itself with a smaller input

'''
def hello(n):
    if n==0:  #Base condition 
        return
    print("Hello")
    #recursive call
    hello(n-1)
    
hello(5)    
    
# hello(5)->Hello
# hello(4)->hello
# hello(3)->hello
# hello(2)->Hello 
# hello(1)->Hello 
# hello(0)-> stops the excecution

'''
Call Stack: LIFO(Last in first out)
stores function calls in memory 

Every function call:

gets added to stack 
removed after the completion 

def fun1():
   print("Fun1")
   func2()
   
def func2():
    print("func2)
    
fun1()  

main
  fun1
  func2



'''




'''
    fact(5)=fact(n-1)*n
           =fact(4)*5
      fact(4)= fact(3)*fact(4)*n
    
    
    
    '''


def count(n):
    if n==0:
        return
    print("Before:",n)
    count(n-1)
    print("after:",n)
count(5)
# added in stack and removed from stack if work is done
'''  0     count(0)  #pop #base condition
    1 |    count(1)|#pop  After:1
    2 |   count(2) |#pop  After:2
    3 |   count(3) |#Pop  After:3
    4 |  count(4)  |#Pop  After:4
    5|  count(5)  | #pop  After:5
     
     Before:5 #Top btm flow(Going down phase)
     Before:4
     Before:3
     Before:2
     Before:1
     After:1  #returning phase 
     After:2
     After:3
     After:4
     After:5
     
     Code Before recursive call:
     -->executes while going down 
     Code after recursive call
     -->Executes while returning 
     
     '''
'''
5! = 5 X 4 X 3 X 2 X 1
   = (n-1)!*(n-2).........n
   
   fact(n) = fact(n-1)*n
   
def factorial(n):
   if n == 0 or n == 1:
       return 1
   return n*factorial(n-1)
   
Call stack 
|   |
|   |
|  fact(1) |Pop 1
|  fact(2) |Pop    1*2
|  fact(3) |pop     1*2*3
|  fact(4) |Pop       1*2*3*4
|  fact(5) |Pop         1*2*3*4*5 =120

#Task:Sum of N numbers 

def sum_n(n):
    if n==1:
       return 1
    return n+sum_n(n-1)
    
sum(5) = 5+sum(4)
sum(4) = 4+sum(3)
sum(3) = 3+sum(2)
sum(2) = 2+sum(1)
sum(1) = 1+sum(0) #Base codition

#Fibonacci:
fib(5) = fib(4)+fib(3)
fib(4) = fib(3)+fib(2)
fib(3) = fib(2)+fib(1)
fib(2) = fib(1)+fib(0)

def fib(n):
    if n <=1:
       return n 
    return fib(n-1)+fib(n-2)  

#Problem:3
# Reverse a string  

rev of string = reverse of rest + first element 

call   s       s[1:]   s[0]   it returns
1     "hello"   "ello"  "h"   reverse("ello")+"h"
2     "ello"   "llo"    "e"   reverse("llo")+"e"
3     "llo"    "lo"     "l"   reverse("lo")+"l"
4     "lo"     "o"      "l"   reverse("o")+"l"
5      "o"     ""       "o"   reverse("")+"o"
#unwinding -- returning phase
6.returs ""
5.returns ""+"o" = "o"
4.returns "o"+"1" = "ol"
3.returns "ol"+"l" = "oll"
2.returns "oll"+"e" = "olle"
1.returns "olle"+"h" = "olleh"


def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]+s[0])
      
Problem:4
Given with n=1234 
Perform the sum of all the digits 
1234 = 1+2+3+4=10  

Last Digit:
1234 % 10 --> 4

Remove last digit 
1234//10 --> 123

1234 
|
4+digit_sum(123)  
then:
123
|
3+digit_sum(12)
 then:
12
|
2+digit(1)
|
1+digit_sum(0) #base case 

#Unwinding phase:

1+digit_sum(0)   1
2+digit_sum(1)   2+1 =3
3+digit_sum(2)   3+2+1 = 6
4+digit_sum(3)   4+3+2+1 = 10

Time comp: 
if number of digits has d 
t.c = O(d)

Space : Each call uses stack 
Becomes total number of digits :d
S.C = O(d)




'''
def digit_sum(n):
    if n == 0:
        return 0
    return (n%10)+digit_sum(n//10)

print(digit_sum(1234))

'''
Problem:5 
Check palindrome string using recursion

Input:"Madam"
Output: True

First check first and last char
and then remaining characters 
s[0] == s[-1] AND s[1:-1]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[1]:
        return False
    return is_palindrome(s[1:-1])
    
s = "Madam"
call = 1
s[0] == s[1] 
True          1:-1
is_palindrome("ada") 

call-2

s = "ada"

a == a
True
is_palindrome("d")

call-3

is_palindrome("d")

True

#stack unwinding starts 

is_palindrome("d") = true 
is_palindrome("ada") = true 
is_palindrome("madam") = true 

final output : True 

Problem-6

print the numbers from N to 1 
N = 5
5 4 3 2 1 
 
    


'''
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:])+s[0]

reverse_string("Hello")

'''
Problem:5
Find the largest element in an array 
using recursion

Input:[3,9,2,15,7]
output: 15

main idea:
compare current element
with max of remaining array 

arr =[3,9,2,15,7]
      0 1 2  3 4

call  n   arr[n-1]   what it does              returns
1     5   arr[4]=7   max(7,find_max(arr,4))     wait 
2     4   arr[3]=15  max(15,find_max(arr,3))    wait 
3     3   arr[2]=2   max(2,find_max(arr,2))     wait 
4     2   arr[1]=9   max(9,find_max(arr,9))     wait
5     1   arr[0]=3   3

unwinding:
5. returns 5 
4.max(9,3) = 9
3.max(2,9) = 9
2.max(15,9) = 15
1.max(7,15) = 15

final output: 15

'''
def find_max(arr,n):
    if n == 1:
        return arr[0]
    return max(arr[n-1],find_max(arr,n-1))

'''
Problem-6
-Check array is sorted or not using recursion
input:[1,2,3,4,5]
output: True 

Another Example:
input:[1,5,3,4]
output:5>3 False (Array is not sorted)


'''
arr = [1,5,3,4]
def is_sorted(arr, n):
    if n == 1:
        return True
    return arr[n-1] >= arr[n-2] and is_sorted(arr, n-1)
print(is_sorted(arr, len(arr)))


def is_sorted(arr, index=0):
    if index == len(arr)-1:
        return True
    if arr[index] > arr[index+1]:
        return False
    return is_sorted(arr,index+1)

'''
arr =[1,2,3,4,5]
call-1
is_sorted(arr,0)

1>2
 False 
 
 is_sorted(arr,1)
 
 2>3
 False 
is_sorted(arr,2)

3>4
False

is_sorted(arr,2)

4>5
False 

Final Output:
True




'''
