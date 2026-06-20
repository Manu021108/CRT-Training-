n = int(input())

a = list(map(int, input().split()))

total = 0

for i in a:
    total +=i
    
average = total/n

print(average)    
    