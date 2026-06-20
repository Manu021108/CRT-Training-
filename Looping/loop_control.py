'''
Loop control: 

Break: It stops the execution of the loop immediately 
(Terminates the loop immediately)

Continue: Skips the current iteration 

Pass:do's nothing


'''

#Example: Break 

i = 1

while i<=10:
    if i == 5:
        break  #Terminates at 5 
    print(i)
    i += 1
    
#Continue: Skips the current iteration and moves forward 

for i in range(1,11):
    if i == 5:
        continue  
    print(i)  
    
    
#Pass: do's nothing (Provides the placeholder for code )   

for i in range(1,11):
    pass


#Summary:

'''
diff btw for and while 

for : used when num of iterations are known 
Best for iterating over the sequences 

while: unknown num of iterations 
Best for condition controlled loops
best for condition based repetition 
It executes until the condition is true 

Q2: what makes the loop infinite ?
When condition never mets false becomes an infinite loop

Q3: can we use else with while ?

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop is finished ")    

Note: Else wont work if there is a break statement
'''
