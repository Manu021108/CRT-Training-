#Problem-6: find the second largest number in a list 

a = [10,40,80,90,30]
#num= 0 1  2 3  4      

largest = float('-inf')   #90
second_largest = float('-inf') 

for num in a:
    
    if num>largest:#30> 90
        second_largest = largest #80
        largest = num #90
        
    elif num>second_largest and num != largest:
         second_largest = num
         
print(largest) #90
print(second_largest) #80            
