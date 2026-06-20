'''
nested loop: loop inside the loop 

first loop: outer loop ---> row
second loop : inner loop  ---> column


Example:

i = 1 4
while i<=3: 
    
    j = 1
    while j<=2:
        print(i,j)      Iteration = 1 (1,1) (1,2)
                        Iteration = 2 (2,1) (2,2)
        j = j + 1                   3 (3,1) (3,2)
    i = i + 1   


For loop: 

for outer in range():
    for inner in range():
         #code 

for every row:
    for every student in that row:
        #greet the student 
        
        
How nested loop works using for :

for i in range(1,4): i = 

    for j in range(1,3): j=2
    
        print(i,j)  Print(1,1)(1,2)
                    print(2,1)(2,2)
                    print(3,1)(3,2)
                    
outer loop runs once 
    Inner loop runs completely 
outer loop runs twice
     Inner loop runs completely 
    
Why nested loops are used ?
1.Pattern problems 
2.Matrix operations 
3.Tables
4.Games 
5.Grid systems 
6.Comparing the elements 

Task: Square- star patterns

****
****
****
**** 


'''

#Square- star patterns

#Outer loop
for row in range(4): #row = 1 
    
    #inner loop
    for col in range(4):  #col = 2
        
        print("*", end="") # * * * *
                           # * * * *
                           # * * * *
                           # * * * *
    print()    
'''
Example-2: right triangle pattern 

*
* *
* * *
* * * *
* * * * *

row == outer loop (1,6)
col == inner loop (row)

#Outer loop 

for row in range(1,6): row = 5

    #inner loop 
    range(4) ==>0,1,2,3
    for col in range(row):  col = 0,1,2,3,4
        print("*" , end="")    #  *
                                  * *
                                  * * *
                                  * * * *
                                  * * * * *
                                  
                                  
                                  
        
        
    print()    

Example-3:Number pattern

1 row =1 
1 2 Row+1
1 2 3
1 2 3 4
1 2 3 4 5

Row1 = 1
Row2 = 2
Row3 = 3

for row in range(1,6): row = 5

    for col in range(1, row+1): col = 1,6
    
        print(col, end="")   1
                             1 2
                             1 2 3
                             1 2 3 4
                             1 2 3 4 5
        
    print()    

Example-4: reverse triangle

* * * * *
* * * *
* * * 
* * 
*
row = 1 elements = 5 
2 --> 4
3 --> 3 
4 --> 2
5 --> 1

for row in range(5,0,-1): row = 5 

    for col in range(row): inner loop= 5 times 
    
        print("*", end = "")  * * * * *
                              * * * *
                              * * * 
                              * * 
                              *
                              
        
        
    print()    

#Example-5

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Row 1 = Prints one 1's
Row 2 = Prints two 2's 
Row 3 = prints three 3's


Logic: 
n = int(input())
outer loop:  rows = range(1,n+1)
inner loop:  col  = range(row)
                   print(rows)
                   
n = int(input("Enter the rows")) 5

for row in range(1,n+1):  row = 5
    
    for col in range(row) 0,1,2,3,4
        
        print(row, end="")    
        
    print()                     

Output:

1
2 2 
3 3 3
4 4 4 4
5 5 5 5 5


EXample-6:Reverse number pattern

n = 5
5 4 3 2 1
5 4 3 2
5 4 3 
5 4
5

Observation:

Number always starts from N 
Ending number decreases in every row

Logic:
n = int(input())
row = range(n) 
range(start,stop,step)
col = range(n,row,-1)   #5 4 3 2 1 0

n = 5 
row = range(5) #0 1 2 3 4  
col = range(5,0,-1)
print(col)


range(start,stop, step)

start--> start index
stop --> stop index
step --> increament/decreament 

n = int(input())  5

#rows ---
for row in range(n): 5 row=4
    
    for col in range(n, row, -1):
                    5    4    -1
         print(col, end="")
                            #5 4 3 2 1
                             5 4 3 2
                             5 4 3 
                             5 4 
                             5                         
    print()                  

#Example-7

A
B C
D E F
G H I J

Alphabet  ASCII

A ----> 65
B ----> 66
C ----> 67

chr() ---converts ASCII to Alphabets

ch = 65
print(chr(ch))

LOgic: 

ch = 65
n = int(input())5
row = range(1,n+1): 
      range(1,6)   row = 1,2,3,4,5
                   row = 1
col = range(row)
             1
     print(chr(ch)) 
     
     
     ch = ch + 1 ---> 66  (B)
     
     print()
     
     
n = int(input()) 5
ch = 65  -->A

for row in range(1,n+1): (1,6) = 1,2,3,4,5
                            row = 4

     for col in range(row): range(3) --> 0,1,2,3
         print(chr(ch),end="") #A
         
         ch = ch+1   65+1 - 66+1-C B
         ch = 67+1+1 
         
    print()     
       
Output:

A 
B C
D E F
H I J K

Example- 8: odd number triangle

1 
1 3 
1 3 5
1 3 5 7

observe: only odd numbers 

odd = 2*n-1 

Logic:

n = int(input()) 5

for i in range(1,n+1): 1,6  i = 4   i = 1,2,3,4,5
    for j in range(1,i+1) , j = 1,5 = 1,2,3,4
        odd = 2*j - 1 = 7
        
        print(odd,end="")
    print()    
     
    output:
    1 
    1 3
    1 3 5
    1 3 5 7
    
    Example-9
    
        *
       * *
      *   *
     *     *
    * * * * *
    
    
    Row | Spaces | stars
    1       4        1
    2       3        2
    3       2        3
    
    spaces = n-i  5-1 = 4
    stars = i 
    
    n = int(input()) 5
                            i=5
    for i in range(1,n+1): 1,6 i=1,2,3,4,5
        
        #leading spaces 
        for j in range(n-i): j=0
            print(" ", end="")
            
        for k in range(i): k = 0,1,2,3,4
            print("*",end=" ")
            
        print()    
    
    Output:
        * 
       * * 
      * * *          
     * * * * 
    * * * * *   

  






    
    
'''