#Decision making ability
#Control flow decides 
#1.how many times to execute what to execute 

#human analogy:

'''
if it rains --> take umbrella
if marks > 40 --> pass
if password correct --> login

'''

#Program also needs decision making ability 
#control flow: determines 
#which statement to execute and in what order 

'''
3-Types of control flow
1.Sequential :Top to bottom execution 
2.conditional: decision making 
3.Looping: Repetition 

'''
#if --> to check the condition 
#& executes if condition is true
#Syntax:
# if condition:
#     statements

#Example:
age = 21
if age > 20:
    print("Eligible")

'''
Execution flow 
        condition true?
               |
        Execute the block

'''

x = 10

if x>5:
    print("Hello")
    
#if-else :what if state becomes false 

# if condition:
#     statement
# else:
#     statements   
    
# Example:    Even/Odd

#take input 
num = int(input("Enter the number"))

#check the condition 
if num % 2 == 0:
    print("Even number")
else:
    print("Odd numbers")  
      
'''
Execution flow 
                         condition ?
                          /      \
                        True    False
                          |       |
                          Even   Odd   
'''

 # elif ladder   
#Multiple conditions: mutiple decisions

# if condition:
#     statement
# elif condition-2:
#     statement
# else:    
#     statement    

#Task: build a student grading system 

#dont do these mistakes
marks = 90

if marks >=50:
    print("C")
elif marks >=90:
    print("A")
else:
    print("Fail")    