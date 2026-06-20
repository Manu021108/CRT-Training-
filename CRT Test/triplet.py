'''      0 1 2 3  4  5
nums = [-1,0,1,2,-1,-4]
         i L         R  
nums.sort()           
nums = [-4,-1,-1,0,1,2]  left = i+1 
         0  1  2 3 4 5
            i    R L      Left > Right --> stop 
                
         
result : -1,0,1
         -1 -1 2
Two pointers approach:

iteration:1
i = 0

nums[i] = -4
left = 2
right = 5

total = nums[i]+left+right
       -4+(-1)+2= -3
  sum<0     
 -3 < 0
 move left 
 
 left= 2
 
 total = -4+(-1)+2=-3
 sum<0
 left = 3 
 total = -4+0+2 = -2
 sum < 0
 left = 4
 total = -4+1+2 = -1
 sum < 0
 left = 5
 left == right stop 
 No triplets were found 
 
 iteration=2 
 i = 1 
 nums[i] = -1
 left = 2
 right = 5
 
 total= -1+(-1)+2 =0
 #triplet found 
 [-1,-1,2]
 
 Move both pointers 
 left = 3
 right = 4 
 
 total = -1+(0)+1 = 0
 Triplet found
 [-1,0,1]
 
 Move both pointers again 
 l = 4
 r = 3
 l>r stop 
 
 iteration=3
 i = 2
 nums[i] = -1
 check duplicate:
 nums[i] == nums[i-1]
 
 -1 == -1
 skip 
       
'''
# if sum < 0:
#     left +=1
# if sum > 0:
#     right -+1    

n = int(input())
nums = list(map(int,input().split()))

nums.sort()
for i in range(n-2):
    #skip the duplicate elements 
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    left = i+1
    right = n-1
    while left < right:
        total = nums[i]+nums[left]+nums[right]
        
        if total == 0:
            print(nums[i],nums[left],nums[right])
            left +=1
            right -=1
            #skip the duplicates 
            while left < right and nums[left] == nums[left-1]:
                left +=1
                
            while left<right and nums[right] ==nums[right+1]:
                right -=1
                
        elif total<0:
            left +=1
        else:
            right -=1              