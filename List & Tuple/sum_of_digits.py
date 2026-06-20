n = int(input()) #3

a = list(map(int, input().split()))
#[123,45,50]
#    6  9  5
#num = 1 

for num in a:
    
    temp = num  #45
    digit_sum = 0
    
    while temp > 0:
        digit_sum = digit_sum + temp % 10
          #    5+4  = 5 + 4 % 10-> 4  =>9
        temp = temp//10
           #  = 4 // 10  = 0
    print(digit_sum)    
        
       