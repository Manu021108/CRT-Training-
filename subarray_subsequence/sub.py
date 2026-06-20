'''
s = "College"

[c]
[co]
[col]
[coll]
[colle]

arr = [1,4,5,6,8,9]

#sub array: It should have a continuity
dervired from continuous part 
[1]
[1,4] wrong 

[4,5,6] ---> yes 

subsequence:
#elements are skipped 
#any slected items 

[1,4] 
concept        subarray    subsequence 

continuity       yes          No
skiiping allowed No           Yes
order            yes          No
derived from    Continuous   seleted from any


EXample:
arr = [1,2,4,5,6,7,9,11]

subarray: [1,2,4] wrong
subarray: [4,5,6,7] right

subsequence:[1,2,4,5]


Problem:

arr = [2,1,5,1,3,2] #6
k = 3

1. 2 1 5 -->8
  j=0 1 2 ==>0+1+2
2. 1 5 1 -->7
   1 2 3
3. 5 1 3 -->9
   2 3 4
4. 1 3 2 -->6
   3 4 5

max_sum = 0  
#looping for each possible window
                #6-3+1 --> 4 #0 1 2 3
                            i = 3
for i in range(len(arr)-k+1)#4 
    current_sum = 0 
    
    #inner -->adding the elements
    for j in range(i,i+k):#3 4 5
                          j = 5
                   0,0+3 
    
        current_sum = current_sum+arr[j]#0
                    = 0+1+3+2 = 6
    print(current_sum) #6
           6   > 8
    if current_sum > max_sum:
        max_sum = current_sum #9
        
print(max_sum) #9
        
     

max_sum = 9


#Sliding window approach

arr = [2,1,5,1,3,2]
             w    
2+1+5 = 8
1+5+1 = 7
5+1+3 = 9
1+3+2 = 6   O(n^2)


arr = [2,1,5,1,3,2]
window = 1
2 1 5  = 8
outgoing = 2 
incoming = 1 

next_window = 8-2+1 = 7
            = previous_sum+(-outgoing)+incoming 

window = 2
1 5 1 = 7

window = 3

next_window = 7 - 1 + 3 = 9
5 1 3 = 9

window = 4
next_window = 9-5+2 =6
1 3 2

Brute Force   vs sliding window 
               2+1+5=8
2+1+5          windows_sum =previous_sum-
                outgoing+incoming 
1+5+1
5+1+3
1+3+2

arr = [2,1,5,1,3,2]
       0 1 2
k = 3

#first window:
window_sum = sum(arr[:k])#2+1+5 = 8

max_sum = window_sum
               3   6   #3 4 5
               i = 5
for i in range(k,len(arr)):
     outgoing = arr[i-k]
                    3-3 = 2 #5
     incoming = arr[i] #2
                    5
     
     window_sum = window_sum-outgoing+incoming
                = 9-5+2 #6
     max_sum = max(max_sum,window_sum)
             = max(9,6) #9
print(max_sum) #9    

#Problem:subarray

find the first continuous subarray 
whose sum equals to the target 

arr = [1,4,20,3,10,5]
       i   j

sub = [1,4,3]= 8

target = 33

output:[20,3,10]

constraint: continuous subarray
1.Elements should be adjacent 
2.elements should not be skipped 

Brute force 

index=0 
[1] = 1
[1,4] = 5
[1,4,20] = 25
[1,4,20,3] = 28          
[1,4,20,3,10] = 38
[1,4,20,3,10,5] = 43

No 33 found

index=1 
[4] = 4
[4,20] = 24
[4,20,3] = 27
[4,20,3,10] = 37
[4,20,3,10,5] = 42

index=2 
[20] = 20
[20,3] = 23
[20,3,10] = 33
[20,3,10,5] = 38

Found 

arr = [1,4,20,3,10,5]
       0 1 2  3 4  5
target = 33

found = False 
                  6       i =2
for i in range(len(arr)): #0 1 2 3 4 5 
     current_sum = 0 
                    2,6
     for j in range(i,len(arr)): #2 3 4 5
                                 J= 4
         current_sum = current_sum + arr[j]
                     = 0+20+3+10=33
         #check for target 
         
         if current_sum == target:
             print(arr[i:j+1])
                       2:5  #20 3 10
             found = True
             
             break
             
    if found:
       break         
       
 
 

Problem Title: Circular Frequency-Based Array Transformation
You are given an integer array A of size N and an integer K.
Perform the following operations:
Count the frequency of each element.
Identify all elements whose frequency is greater than 1.
Rotate these repeated elements to the right by
K positions while maintaining their relative 
occurrence positions.
Reverse every maximal contiguous segment
consisting only of unique elements (frequency = 1).
Finally, move all zeros generated during 
transformations to the end while preserving the relative
order of non-zero elements.
Return the transformed array.
Input Format

N
A1 A2 A3 ... AN
K
Constraints

1 ≤ N ≤ 10^5
-10^9 ≤ Ai ≤ 10^9
0 ≤ K ≤ 10^9



#Sliding window approach for above problem 
       0 1 2  3 4  5
arr = [1,4,20,3,10,5]    R = Expand the window 
            L            L = shrinking the window
                 R increased until sum is greater   
                 if sum > then shrink the L
R = 0
window   sum
[1] =     1      sum <target
[1,4]=   5       sum < target
[1,4,20]= 25     sum <target
[1,4,20,3]= 28     sum <target
[1,4,20,3,10]= 38     sum > target
[4,20,3,10]= 37     sum > target
[20,3,10]= 33     sum == target

'''
arr =[1,4,20,3,10]
target = 33
left = 0
current_sum = 0
for right in range(len(arr)):
       current_sum = current_sum+arr[right]
       
       while current_sum > target:
              
              current_sum = current_sum - arr[left]
              left = left + 1
              
       if current_sum == target:
              print(arr[left:right+1])  
              break     
       
'''
Problem:3
find the length of longest
continous subarray 
that contains no repeating elements  

Example:
input:[1,2,3,1,2,3,4]
output:4

Example:substring
input:["abcabcbb"]
output:3  -->abc

keep adding the 
elements until duplicate found
Brute Force 
i = 0
[1] = unique
[1,2] = unique
[1,2,3] = unique
[1,2,3,1] = duplicate

length = 3

i = 1
[2] = unique
[2,3]=unique
[2,3,1]= unique
[2,3,1,2] = duplicate

len = 3

i = 2
[3] = unique
[3,1] = unique
[3,1,2] = unique
[3,1,2,3] = duplicate

len = 3

i = 3
[1] = unique
[1,2] = unique
[1,2,3] = unique
[1,2,3,4] = unique

len = 4  best answer 

arr = [1,2,3,1,2,3,4]
       0 1 2 3 4 5 6
max_length = 0
                #7       i = 3
for i in range(len(arr)):#0 1 2 3 4 5 6
    
    seen = set()#1,2,3,4,      j= 6
    for j in range(i,len(arr)):#3 4 5 6
        if arr[j] in seen:
            break
        seen.add(arr[j])
        
        max_length = max(max_length,j-i+1)
                   = max(3,4) #4
print(max_length)   
#4

#using sliding window         
L =0
R = L
arr = [1,2,3,1,2,3,4]
             L
                   R
[1] = unique
[1,2] = unique
[1,2,3] = unique
[1,2,3,1] = duplicate r== duplicate(shrink)
[2,3,1] = unique r=r+1
[3,1,2] = shrinked(unique)
[1,2,3] = shrink(left)-unique
[1,2,3,4] = unique

print(len(subarray))

'''       
arr = [1,2,3,1,2,3,4]   

left = 0
max_length = 0
seen = set()

for right in range(len(arr)):
       
       #remove the duplicates 
       while arr[right] in seen:
              seen.remove(arr[left]) 
              left = left+1
              
       seen.add(arr[right])   
       
       #update the maximum length
       max_length = max(max_length,right-left+1) 
print(max_length)                

'''
#find the longest substring 
without repeating any character
Example: 
input:"abcabcbb"
output:3  -->abc


'''
