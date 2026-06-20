'''
Prefix Sum:one of the most important technique
used to solve sub array problems 
1.Fast range sum queries 
2.Optimization
3.sliding window's alternative
4.sub array problems 
5.competitive programming 

It reduces the repeated calculations and 
improves the time complexity 

what is prefix sum?
stores the cumulative sum of the elements 
from the beginning of the array to every index 

arr = [a0,a1,a2,a3....]

then:
prefix[i] = arr[0]+arr[1]+arr[2]+...arr[i]

problem:

arr = [2,4,1,7,3]
       0 1 2 3 4
         L   R+1

find the sum from index 1 to 3
4+1+7 = 12

solve in brute force --use pointers 
arr = [2,4,1,7,3]
L = 1
R = 3
total = 0

for i in range(L,R+1): --->O(n)
    total += arr[i]
    
print(total)

i = 1 total = 4 -->O(n)
i = 2 total = 5 -->O(n)
i = 3 total = 12 
    
sum(1,3)
sum(0,3)
sum(2,3) complexity increases 

Prefix sum --> 

arr = [2,4,1,7,3]
       0 1 2 3 4
       
Calculate the prefix:

prefix[i] = prefix[i-1]+arr[i]

index   arr[i]   prefix[i]  
0         2         2
1         4         2+4=6
2         1         6+1=7
3         7         7+7 = 14
4         3         14+3 = 17

prefix[i] = [2,6,7,14,17]

prefix[0] = 2  sum from 0 to 0
prefix[1] = 6  sum from 0 to 1
prefix[2] = 7  sum from 0 to 2
prefix[3] = 14  sum from 0 to 3
....

prefix sum formula:
sum = prefix[R]-prefix[L-1]
special case:
if L == 0
sum = prefix[R]

find sum from 1 to 3

R = 3
L = 1

sum = prefix[3]-prefix[0]
sum = 14-2= 12

4+1+7 = 12 






'''
arr = [2,4,1,7,3]
 #     0 1 2 3 4

n = len(arr) #5

#create a prefix array
prefix = [0]*n  # [0,0,0,0,0]

prefix[0] = arr[0] #[2,6,7,14,17]

#Build the prefix sum 
                   #i = 4
for i in range(1,n): #1,2,3,4
    prefix[i] = prefix[i-1]+arr[i]
         #4   =        7+7 = 14+3=17
print(prefix)      
L = 1
R = 3
#range sum 
if L == 0:
    answer = prefix[R]    
else:
    answer = prefix[R] - prefix[L-1] 
          # = 14-2= 12  
    
print(answer)  #12  

'''
Find the multiple range queries 
1-4  sum 
2-5
0-3
all queries in a single program 


'''
arr = [2,4,1,7,3,9]
 #     0 1 2 3 4 5

n = len(arr) #5

#create a prefix array
prefix = [0]*n  # [0,0,0,0,0]

prefix[0] = arr[0] #[2,6,7,14,17]

#Build the prefix sum 
                   #i = 4
for i in range(1,n): #1,2,3,4
    prefix[i] = prefix[i-1]+arr[i]
         #4   =        7+7 = 14+3=17
print(prefix)      
queries = [(1,4),(2,5),(0,3)]

for L,R in queries:
#range sum 
    if L == 0:
        answer = prefix[R]    
    else:
        answer = prefix[R] - prefix[L-1] 
          # = 14-2= 12  
    
    print(answer)  #
    
'''
Problem-3
Find the equilibrium index using prefix sum 

arr = [1,3,5,2,2]
       0 1 2 3 4

Left sum = 1+3= 4   prefix[i-1]
Right sum = 2+2 = 4  totalSum - prefix[i]

left sum == right sum 

print equilibrium index
index = 2
    
    
    
'''
arr = [1,3,5,2,2]
    #  0 1 2 3 4
n = len(arr) #5
prefix = [0]*n #[0,0,0,0,0]
prefix[0] = arr[0] #[1,4,9,11,13]
for i in range(1,n):
    prefix[i] = prefix[i-1]+arr[i]
    #      4           11+2 = 13
    
total_sum = prefix[-1] #13   

#find the equilibrium index 
                #i = 2
for i in range(n):#0,1,2,3,4
    
    #left sum 
    if i == 0:
        left_sum = 0
    else:
        left_sum = prefix[i-1] #4  
        
    #right sum     13-9=4
    right_sum = total_sum - prefix[i]  
    
    #check for 
    #     4 == 4
    if left_sum == right_sum:
        print("Equilibrium index",i)  #2