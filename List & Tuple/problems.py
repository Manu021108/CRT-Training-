'''
Problem-1: Sum of the elements

Given a list of integers, find the sum 

a = [1,2,3,4,5]
  i= 0 1 2 3 4
total = 0

for i in a:
   total +=i
   
print(total)  

time complexity: O(n) 


Problem-2: find the maximum element 

b = [10,50,90,40]

                first assume max = b[0]
                          |
                  traverse over the list 
                          |
                  compare max with remaining elements 
                          |
                 update the max 
                          |
                      print(max)                             
'''
b = [10,50,90,40]
#i     0  1  2  3
maximum = b[0] #90

for i in b:
    if i > maximum:
        maximum = i 
        
print(maximum) 

'''
Problem-3: count the even numbers in a list 

input:[1,2,3,4,5,6]
output:3

a = [1,2,3,4,5,6]
i =  0 1 2 3 4 5
i =  5
count = 3

for i in a:
   if i%2 == 0:
      count +=1
             = 0+1+1+1 - 3
      
print(count)  #3    

Problem-4: Reverse your list 
input: [1,2,3,4]\
output: [4,3,2,1]

a = [1,2,3,4]

print(a[::-1])

Problem-5:Remove the duplicates from list
input: [5,6,1,7,7,8]
output:[5,6,1,7,8]

a = [5,6,1,7,7,8]
#      0 1 2 3 4 5
# i = 5 
result = []

for i in a:
   if i not in result:
       result.append(i)
       
print(result)   


Problem-6: find the second largest number in a list 

a = [10,40,80,90,30]

largest = float('-inf')  
second_largest = float('-inf') 

for num in a:
    
    if num>largest:
        second_largest = largest #-inf
        largest = num
        
    elif num>second_largest and num != largest:
         second_largest = num
         
print(largest)
print(second_largest)             





Problem-8: 
Find the largest odd number: 

Example:

input: [1,2,4,6,9]
output: 9

Logic Flow: 
              Traverse list 
                   |
               check for the odd condition
                   |
               Track the max value        


a = [1,2,4,6,9]
     0 1 2 3 4
i = 4
largest_odd = -1

for i in a:

    if i%2 != 0:
        if i > largest_odd:
            largest_odd = i #9

print(largest_odd)

Problem-9:

Create a list of squares:

input = [1,2,3,4]
output = [1,4,9.16] (New list)

#LOgic flow: 
                create a empty list
                        |
                   Traverse original list 
                        |
                   Append the squares of each number 
                   
                #    append(i*i)          

a = [1,2,3,4]

squared_list = []

for i in a:
    squared_list.append(i*i)
    
print(square_list)    


Problem-10:

Check whether the given key exist  in the list:

b = [10,20,30,40]
 i =  0  1   2 3

key = 30 

found = False 

for i in b:
    if i == key:
       found = True
       break
       
if found:
   print("Element is found")
else: 
   print("Element is Not found")      

Problem:11
find the common elements in both the lists

a = [1,2,3,4,5]
b = [3,4,5,6,7]

common elements: 3,4,5

                Traverse the list 
                       |
                check if element is exist in b
a = [1,2,3,4,5]
b = [3,4,5,6,7]           
for i in a:
   if i in b:
      print(i)  
      
Problem:11
swap the first and last elements in a list 

a = [1,2,3,4,5]
output:[5,2,3,4,1]

a[0],a[-1] = a[-1],a[0]

#Tuples:

Problem 12:
Find the maximum in a tuple

t = (10,20,30,40)

maximum = t[0]

for i in t:
    if i>maximum:
       maximum = i
       
print(maximum)       

output: 40

Problem-13:

convert tuple into the list 

t = (1,2,3)

a = list(t)

print(a)


                    
'''
'''
Problem - 14:
Find the avg of the numbers in a list 
Note: Take the input from the user in a list 

n = int(input())
a = list(map(int, input().split()))
                  "10 20 30" ---> '10','20','30'- 10,20,30

map--> maps the int to input 


n = int(input())

a = list(map(int, input().split()))

total = 0

for i in a:
    total +=i
    
average = total/n

print(average)    
   
Problem-14:

Find all the odd numbers in a list 
Note: take the list as input from user     
    
n = int(input())

a = list(map(int, input().split()))

for i in a:
    if i%2 != 0:
       print(i, end="")

Problem:15
Find the sum of the digits of each element in a list 

Example:
input:[10,20,30,44]
       1+0=1,2+0=2
output:[1,2,3,8]



Problem:15
find the smallest even number in a list 

Traverse list --> check for even cond-->
Track the smallest 

n = int(input())

a = list(map(int, input().split()))

input:[1,2,3,4]
      0  1  2 3

minimum = 99999

for i in a:

    if i%2 == 0:
        if i < minimum:
            minimum = i #2
            
print(minimum)  #2           

#Problem:17

Find the number of elements greater then avg 

input:[1,2,3,4,5]
avg=3
output:2

n = int(input())

a = list(map(int, input().split()))

total = 0
for i in a:
   total +=i
   
average = total/n

count = 0
for i in a:
   if i>average:
      count +=1
      
print(count )         


ALternate:

total = sum(a)

average = total/n
count = 0
for i in a:
   if i>average:
      count +=1
      
print(count ) 

#Problem:19
Find the difference between largest and smallest number in a list


#Problem-20:
count the numbers ending with 5 

Example: 
input:[25,33,44,65]
output:2

Problem:21
Replace the negative numbers with zeros

Example: 
input:[1,-2,8,5,-7]
output[1,0,8,5,0] 

Problem:22

Product of all the elements in a list

Problem:23
Print the elements greater
than previous element 

input:2 5 3 8 6
      0 1 2 3 4
      
  i=1 arr[i]> arr[i-1]  

5>2 --->yes
3>5 --->no
8>3  --->yes
6>8 --->no

output: 5 8


'''
'''
Problem:24
count the multiples of 3
input[3,5,9,12,14]
output:3

n = int(input())

a = list(map(int, input().split()))

count = 0
for i in a:
   if i%3 == 0:
      count +=1
print(count)      

Problem:25
Find the absolute diff between
first and last element in a list

input: [10,25,-30,-40] 
output: 10-(-40)

|10+(-40)| ==>30

abs()

n = int(input())

a = list(map(int, input().split()))

difference = abs(abs(a[0])-abs(a[-1]))

print(difference)

#Problem:26

Print the unique elements:

Elements which appears only once 
input:[1,2,2,3,4,4]
output:[1,3]

for i in a:
   if a.count(i) == 1:
      print(i,end="")
      
#Problem:27
Move all the negative numbers to the left
given a list of integers,move all the negative numbers 
to the beginning of the list 
Note: maintain the order

Example:

input:[1,-2,3,-4,5]
output:[-2,-4,1,3,5]      

'''
n = int(input())

a = list(map(int, input().split()))

negative = []
positive = []

for i in a:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i) 
        
result = negative+positive

print(*result)    #unpacking of list

'''
find the frequency of the element
Example:
input:[1,2,2,3,3,3]
output:[1,2,3]

'''
n = int(input())

a = list(map(int, input().split()))
#[1,2,2,3,3,3]
#  0 1 2 3 4 5
i= 5

freq = {
    1:1,
    2:2,
    3:3
}

#traverse the list

for i in a:
    if i in freq:
        freq[i] = freq[i]+1
                # = freq[2]+1
    else:
        freq[i] = 1  
        
for key in freq:
    print(freq[key])          

'''
#Rotate list by k positions 
given a list and k integer,rotate the 
list to the left by k positions
Example:
input:[1,2,3,4,5]
k = 2
output:[4,5,1,2,3]

n =int(input())
a = [1,2,3,4,5]

k = k%n -->7%5 = 2

a[-k:] ==>[4,5]
a[:-k] ==>[1,2,3]

result = a[-k:]+a[:-k]
       = [4,5]+[1,2,3]
       =[4,5,1,2,3]
       
#alternate method

for i in range(k+1):
   first = a.pop(0) #first element removed

   a.append(first) #first element added at end
   
print(*a)         

#Problem: Reverse a list 
Note:two pointers approach 

Example: 
input:[1,2,3,4,5]
output:[5,4,3,2,1]

arr = [1,2,3,4,5]
           L R
       5 2 3 4 1
       5 4 3 2 1
       
left = 0
right = len(arr)-1

while left<right:
    arr[left],arr[right] = arr[right],arr[left]
    
    left +=1
    right -=1
    
print(*arr)    
      
Problem:33

Check an array is palindrome
using two pointers

left = 0
right = len(arr)-1
palindrome = True

while left<right:
     
     if arr[left] != arr[right]
         palindrome = False 
         break
         
     left +=1
     right -=1
     
if palindrome:
   print(palindrome)
else:
   print("NOt a palindrome")            
            
 
Problem:34
Move zeroes to the end of the list 
input:[1,0,4,-2,0]
output:[1,4,-2,0,0]

arr = [1,0,4,-2,0]
           L
             R
       1,4,0,-2,0 
       
       1,4,-2,0,0   
       L = 0 and R = 0
       
left = 0
for right in range(len(arr)):
     if arr[right] != 0:
         #swap elements 
         arr[left],arr[right] = arr[right],arr[left]
         
         left +=1
         
print(arr)    

Problem:35
Sort the binary array:
Example:
input:[1,0,0,1,1,0,1]
output:[0,0,0,1,1,1,1]

manishsahu@technofutureindia.com



         
'''
