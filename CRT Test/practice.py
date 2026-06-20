'''
Problem 1: Empty Chocolate Packets* 
(September Day 1 – Slot 1)

*Problem Statement:*  
A chocolate factory is packing chocolates into 
packets. 
The chocolate packets represent an array 
of N integer
values. Find the empty packets
(0) and push them to the end of the conveyor
belt (array).

*Example:*  
- Input: N=8, arr = [4,5,0,1,9,0,5,0]  
- Output: 4 5 1 9 5 0 0 0

*Logic:*  
- Keep all non-zero elements in order at the beginning
- Fill the remaining positions with 0s

*Constraints:*  
- Non-zero elements maintain their original order

*

## *Problem 2: Count Elements Greater Than Prior Elements* (Day 2 Slot 1 – Question 1)

*Problem Statement:*  
Given an integer array Arr of size N, 
find the count of elements whose value is 
greater than all of its prior elements. 
The 1st element is always considered in the
count.

*Example:*  for i in range(1,n):
- Input: Arr = {7,4,8,2,9} 
                0 1 2 3 4 
                      i
                count = 1
                max_so_far = 7
                i = 1 
                4>7  false (ignore)
                count = 1
                i = 2
                8>7 (Yes)
                count= 2
                max_so_far = 8
                2>8 False (ignore)
                count= 2
                max_so_far= 8 
                i = 4
                9>8 True
                count = 3
                max_so_far = 9              
- Output: 3  
- Explanation: 7 (first element),
8 (>7), and 9 (>8, >7, >4, >2)
meet the condition


*Constraints:*  
- 1<=N<=20  
- 1<=Arr[i]<=10000

*

'''
n = int(input())
arr = list(map(int,input().split()))
count = 1
max_so_far = arr[0]
for i in range(1,n):
    if arr[i]> max_so_far:
        count +=1
        max_so_far = arr[i]
print(count)        