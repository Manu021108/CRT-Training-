'''
Problem-7 Check if the list is sorted (dont use sort())

         



'''
a = [1,2,3,4,5]

flag = True

for i in range(len(a)-1):
    if a[i] > a[i+1]:
       flag = False
       break
         
print(flag)