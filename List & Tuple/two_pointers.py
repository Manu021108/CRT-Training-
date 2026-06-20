'''
Two pointers:

one pointer is start
one pointer is end

Operations:
swapping 
Moves towards the center 

arr = [1,2,3,5,7,10,11,15]
             L R
     L<R

Example:
sum of any two digits should be equal
to target,print(pair)
target = 15
arr = [1,2,3,5,7,10,11,15]
       i j

outer range(n)
inner range(i+1,n)
1+2 --> 3
1+3 --> 4
1+5 --> 6
1+7
1+10
1+11
1+15-->16

arr = [1,2,3,5,7,10,11,15]
       0 1 2 3 4 5  6   7 
       i j
       arr[i]+arr[j]
target = 15
n = len(arr)
for i in range(n):
    
    for j in range(i+1,n):
        current_sum = arr[i]+arr[j]
        
        if current_sum == target:
           print("Pair found:",arr[i],arr[j])

arr = [1,2,3,5,7,10,11,15]
       0 1 2 3 4 5  6  7
             L   R
                   =  1+15 = 16 > target
                       R--
                       14 < target 
                       L++
                       
                       1+11 = 12 <target 
                       2+11 = 13 < target
                       3+11 = 14 < target
                       5+11 = 16 > target
                       5+10 = 15 == target
                       a[l],a[r]
       current_sum = arr[L]+arr[R]

              target = 15 


'''
