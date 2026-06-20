'''
Strings: one of the most important topic 

Strings are the sequence of characters:
Enclosed -->'' , "", ''''''

                            Mutability 
                            /       \
                        Mutable    Immutable
                          |             |
                          Change     cant change 
                          
Strings are immutable                           

EXample:

name = "Aanish Kumar"
name[0] = "M"  --> error

#Memory space 

str = "S T R I N G"
       0 1 2 3 4 5
 
#accessing the elements 
str[0]


'''


# name = "M A N I S H"
# print(name)

# # print(name[0])s h"
#         # 0 1 2 

# print(name[0:2])
# print(len(name))

# str = "College"
#     #  0123

# print(len(str))

# #Slicing:

# str[start,end,step]


# print(str[0:3])

'''
str = "C O L L E G E"
       0 1 2 3 4 5 6
      -7-6-5-4-3-2-1

str[-1:-4]
str[6:3]

str[-1]   --> last character 

str[-2] --> second last character 

str[10]  --> index error

#ommiting start 
str[:3]  --> col
str[3:]  -> lege

#C O L L E G E
 0 1 2 3 4 5 6
 C     L     E
 C    
 
#Step Slicing:
str[0:6:2] --->CLE
str[0:6:1] --->colleg


#Reverse your name 
name = "Manish"

name[::-1] 

'''

name = "Manish"

# [::-1] --> starts from -1 and goes upto end 

print(name[::-1]) 

'''
#string traversal:
            i=2
name = "C h a l a p a t h i"
        0 1 2 3 4 5 6 7 8 9
        

for i in range(len(name)):  10
                            i = 0,9
   print(name[i])
   
output:
C 
H 
A
L
A
P
A
T
H
I 


'''

for ch in range(len(name)):
    print(ch,name[ch])
    
print(name.upper())
print(name.lower())

#Title() --> First letters capital 
#str = "python programming"

print(name.title())

#capitalize()
#only first letter will get capital

print(name.capitalize())

College_name = " Chalapathi "
#strip -- Removes the extra spaces 
print(College_name.strip())

#Replace: 

text = "I love programming"
print(text)

replaced_text = text.replace("love","Hate")
print(replaced_text)

fruit = "banana"
#Find the frequency of "a"
print(fruit.count("a"))

#startswith --> check's if starting with "letter"
print(name.startswith("M"))

#endswith -->

text = "python"
print(text.endswith("on"))

#split()
text = "Python C Java"

separated = text.split()
print(type(separated))

#Use join --> list --> string 
#python-C-Java 

new = "-".join(separated)
print(new)


#Searching inside the strings 

#find() -->
print(new.find("Jython"))

#using membership operator
print("Python" in new)

#index()

text = "Python"

# print(text.index("Z"))

#which is safe find() or index?

#find() is safe to use 

#String formatting 

name = "Vijay"
age = 20 
#F - strings
print(f"My name is {name} and age is {age}")

#old college
print("Name:",name, "and age is:",age)

#format()

print("Welcome {}".format(name))

#Escaping Characters or sequence 

print("hello \n world")
print("Hello \t world")

#R- strings (Regex-regular expressions)
path = r"c://downloads/photos/pic.jpeg"

'''
r --> tells to your interpreter that there are no escaping 
characters in path 

'''

#swapcase() ---? 
text = "PyThon"

print(text.swapcase())

#casefold() --> stronger lower conversion 

print(text.casefold())

#center--?

print(text.center(40))

#Task: create a string with your frnds names 

# name = Manish Vijay Ajay

#split the names to a list 
#join the string "_"
# #Traverse over the string and find the index 
# of the person name starting with "A"
#Print the person name 
#count the len of the name & check "a" occurances 
#Print the frnd name with 30 spaces in center 

#Task:  Reverse your name or a string without using slicing 


#slicing:

name = "Manish"

print(name[::-1])

# dont use slicing 
'''
                   logic
                     |
    Read the characters from the end of the string 
                     |
                start adding each char (from end ) to a new var 
                     |
                     Print the var  
                     
Example: 
          INPUT:  H E L L O  (TRAVERSE)                    
        OUTPUT:   O L L E H          
                     
             S = HELLO 
                 01234
                    4  
                 start = 4 
                 end = -1 
                 step = -1 
             reverse =""
             for i in range(len(S)-1,-1,-1): 4,-1 = 5
                  reverse = reverse+S[i]
                  
                  print("Step:",i"character:"S[i],"Reverse:",reverse)
 
'''



# https://assessments.prepinstaprime.com/CITY
# /dashboard/startTest/CITY00021