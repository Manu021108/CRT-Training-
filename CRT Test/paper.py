'''
Problem: Pair Frequency Match
Given an array of N integers and a target value K, 
find the number of unique pairs (i, j) such that:
i < j
arr[i] + arr[j] = K
A pair is considered unique based on values, not indices.
Input Format
First line contains integer N.
Second line contains N space-separated integers.
Third line contains integer K.
Output Format
Print the count of unique pairs whose sum equals K.

'''

#Two sum problem 

arr = [1,5,7,-1,5,1]

target = 6

# 1+5 = 6  pair(1,5)
# 7+(-1) = 6 pair(-1,7)
# 5+1  = 6 pair(5,1)

# count(pairs) 2

#solve the problem with two pointers 

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

arr.sort()
left = 0
right = n-1
pairs = set()

while left < right:
    current_sum = arr[left]+arr[right]
    
    if current_sum == k:
        pairs.add((arr[left],arr[right]))
        
        left +=1
        right -=1
    elif current_sum < k:
        left +=1
        
    else:
        right -=1 
print(len(pairs))                   

