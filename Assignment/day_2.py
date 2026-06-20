

'''
list --> [10,200]
input --> user (string)
split() --> 10200 ---> "10","200"
int --> 10, 200
claps = list(map(int, input().split()))
'''

#Water bottle tracker --> 
# 1.No of hours 
# 2.Water intake 

#read the number of hours 
n = int(input())

#Read the glasses consumed 
glasses = list(map(int, input().split()))

#store total water intake 
total = 0

#count of hours 
hours = 0

#loop through each glass of water 
for glass in glasses:
    #add water intake 
    total = total + glass 
    
    #Increase the hours count 
    
    hours = hours+1
    
    if total > 8:
        break
print(hours)
print(total)    