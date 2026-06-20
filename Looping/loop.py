'''
What is a loop?
A loop is used to repeat the block of code
Instead of writing the logics again and again 
we will repeat the code.

print("Hello")
print("Hello")
print("Hello")
print("Hello")


'''
# #Looping ---2 types 
#    /       \
# For      while
  
'''
for --> used when num of iterations are known 
while ---> num of itertions are unknown
1.executes until the condition is true  

Benefits:
1.Reduces the code duplication & complexities 
2.Save time
3.Make our programs very efficient 
4.Helps in the automation 

                   Execution flow of loops 
                   
                          Start
                            |
                          condition check 
                            |
                         True --->Execute the block 
                            |
                            Repeat
                            |
                            False ---> stop   
'''
#For loop: it iterates on the sequences 
#list,tuple,range,strings 

'''
C- Programming 

for(i = 0; i<n; i++){
    i = 0 initialization 
    i<n --> condition 
    i++ --> increament 
}

python :
list --> collection of ordered elements 
List ---> [,,,,]
list is mutable 

'''

frnds = ["Rajesh","suresh","ramesh"]

#syntax:

# for var in sequence:
#     statements  
for i in frnds:
    print(i)

'''
frnds = ["Rajesh","suresh","ramesh"]
            0       i= 1         2
Rajesh
suresh
Ramesh

'''


# for frnd in frnds{
#     print("Hello")
# }
#     print(frnd)
    
#2nd way ?

#range(start,end-1,step)  
# range(1,11)  

for i in range(5):
    print(i)

for i in range(1,16):
    print(i)
    
#Task:Mutiplication table -5
num = 5

for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Task: sum of numbers (1,6) 1+2+3+4+5 ->15 
total = 0

for i in range(1,11):
    total +=i
print(total)    

#Task: s = "Manish" now count char in your name using for 

word = "Elephant"
char_count = {}

for i in word:
    if i in char_count:
        char_count[i] +=1
    else:
        char_count[i] = 1
print(char_count)            
 
#use for loop and print only
# even numbers upto 20 
#dont write even num logic 

for i in range(2,21,2):
    print(i)
    
#Reverse of the sequence  
# 1 , 11---> 11,1,-1   

for i in range(11,1,-1):
    print(i)
    
#while ---> 

#syntax:

# while condition:
#     statements    

#Example:

i = 1 #when i =6 exits the loop

while i<=5:
    print(i)  #1 2 3 4 5
    i +=1 #6
   
#Infinite loop    
while True:
    print("run forever")    
    
#sum of numbers --using while  
#do sum until the input is 0

'''
num = int(input()) 5
total = 0

while num != 0:
    total = total + num 
      0   =  0    +  5 --> 5
      5   =  5    +  10 ---> 15
      15  =  15   +  6  ---> 21
    num = int(input())  0
    
print(total)   
# 21
    
EXample - 2:

Print the even numbers from 2-20?

                   Execution flow(Logic)
                        
                        
                        Starts from 2
                              |
                        check if num <= 20  
                              |
                            print(num)
                              |
                    increament the number by 2    
                              |
                            Repeat
                              |
                          Stop after 20     

'''
num = 2 , 8

while num <= 20:
    print(num)  # 2 4 6 8 10 12 14 16 18 20
    
    num = num + 2 
    #  6  = 6   + 2 - 8 
    #  8  = 8   + 2 - 10