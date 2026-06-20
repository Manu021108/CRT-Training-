'''Problem-8: 
Find the largest odd number: 

Example:

input: [1,2,4,6,9]
output: 9

Logic Flow: 
              Traverse list 
                   |
               check for the odd condition
                   |
               Track the max value        

'''
a = [1,2,4,6,9]
#      0 1 2 3 4
# i = 4
largest_odd = -1

for i in a:

    if i%2 != 0:
        if i > largest_odd:
            largest_odd = i #9

print(largest_odd)