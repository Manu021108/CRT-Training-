n = int(input()) #5


arr = list(map(int, input().split()))
                   #10 20 30 40 -->'10','20','30','40'
                   #[2 5 3 8 6]
                #    0 1 2 3 4
               # i = 4
                   
#traverse over the list
#iteration starts from 1(second element)

for i in range(1,n):  
         #6 > 8
    if arr[i] > arr[i-1]:
        print(arr[i],end=" ")  #5 8           
       