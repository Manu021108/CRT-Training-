'''
Kadane's algorithm:Max sub arrays problems 

arr = [2,-1,3,-2,4]

find the contigious sub array with max sum

subarray: [-1,3,-2] right 
          [2,3] invalid
i = 0       
subarrays     sum       
[2]           2
[2,-1]        1
[2,-1,3]      4
[2,-1,3,-2]   2
[2,-1,3,-2,4] 6

i = 1
[-1]       1
[-1,3]     2
[-1,3,-2]  0
.....

Kadane's algorithm Main idea 

At every element we decide:

TWo choices:
1.continue previous subarray 
           (or)
2.Start a new subarray 

current_sum = -5 
next_element = 10 

-5+10 = 5 #discarding the previous (-ve)
next == 10 
     
arr = [2,-1,3,-2,4]  

current_sum = 2
max_sum = 2 

index:1
    -1
    choice-1: extend the array
     2+(-1)= 1
    
    choice-2: start a new array  
    -1   

current_sum = 1
max_sum = 2

index-2: 3
   choice-1: extend the array
     2+(-1)= 1+3=4
    
    choice-2: start a new array  
    3  
    
current_sum = 4
max_sum = max(2,4) =4 

index-3:-2
choice-1: extend the array
     2+(-1)= 1+3=4+(-2) = 2
    
    choice-2: start a new array  
    -2
current_sum = 2
max_sum = max(4,2) = 4   

index-4:4

choice-1: extend the array
     2+(-1)= 1+3=4-2=2+4=6
    
    choice-2: start a new array  
    4   
current_sum = 6 
max_sum = max(4,6) = 6

current_sum = max(arr[i],current_sum+arr[i])
max_sum = max(max_sum,current_sum)
  

'''
arr = [2,-1,3,-2,4] 
    #  0  1 2  3  4 

current_sum = arr[0] #2
max_sum = arr[0] #2
                      #i = 4
for i in range(1,len(arr)): #1,2,3,4
    #Either continue with old subarr
    #or start a new sub arr
   #             =    4,2+4 = 4,6
    current_sum = max(arr[i],current_sum+arr[i])
    max_sum = max(max_sum,current_sum)
   #                4            6 = 6
    
print(max_sum)    #6

'''
Problem: Maximum Winning Streak

A cricket player gains or loses
points in each match.

Positive → won points
Negative → lost points

The coach wants to find the longest continuous 
winning streak with maximum performance.

But instead of returning the sum,
return the:

Maximum score
Starting index
Ending index
Example

Input:

scores = [-2, 4, -1, 5, -3, 2]

Output:

Maximum Score = 8
Start Index = 1
End Index = 3

Subarray:

[4, -1, 5]

scores = [-2, 4, -1, 5, -3, 2]

Choice - continue subarray
index-1
  -2+4 => 2
choice-2 start a new subarray
    4 --> starting 

scores[i] > current_sum+scores[i]
new sub array is starting 
temp_start = i 


current_sum = scores[0] #-2
max_sum = scores[0] #-2
current_sum = max(scores[i],current_sum+scores[i])
                    4,-2+4= 4
                    4
     max_sum = max(max_sum,current_sum)               
                     -2       4   = 4
'''
arr = [-2, 4, -1, 5, -3, 2]
    #   0  1   2  3   4  5

current_sum = arr[0] #-2
max_sum = arr[0] #-2

start = 0
end = 0
temp_start = 0
                        #i = 5
for i in range(1,len(arr)):#1,2,3,4,5
    
    #Either starting a new sub array or extending
    if arr[i] > current_sum+arr[i]:
        # 2 > 5+2=7
        current_sum = arr[i]
        #           = 4
        #new possible starting index
        temp_start = i #1
        
    else:
        current_sum = current_sum+arr[i]
            #       =  4+(-1) =3+5 = 8+(-3)=5+2= 7
        
    #update the maximum
    #       7>8
    if current_sum > max_sum:
        max_sum = current_sum   #8
        
        #save the index values 
        start = temp_start #1
        end = i  #3
print(max_sum) #8
print(start) #1
print(end)# 3
print(arr[start:end+1]) 
       #    1 : 4

'''
Problem-5
Maximum Product subarray 

input:[2,3,-2,4]
output:6    2*3
print(index)


'''
       