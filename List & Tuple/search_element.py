'''

Problem-10:

Check whether the given key exist  in the list:
'''
b = [10,20,30,40]
#  i =  0  1   2 3

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




       
       
       