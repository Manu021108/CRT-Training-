'''
Check whether a character is alphabet or not 

Logic flow :

read the character-->
ASCII --> chr(ch)--> int -- string
ord(ch) --> string -- int 
            
A-Z ==>65 - 90
a-z ==>97 - 122

ch = input()
asci = ord(ch)

if(65 <= asci <=90) or (97<=asci <=122):
     print(alphabet)



'''
ch = input("Enter the alphabet")
asci = ord(ch)

if(65 <= asci <=90) or (97<=asci <=122):
     print("alphabet")
else:
    print("Not an alphabet")     
    
    
'''
Find the length of the string 
without using len()
Logic:
        1.Initialize a count = 0
                 |
        2.Traverse the string 
                 |
        3.Increament the counter for each char   
                 |
         4.Print(counter)      
         
string = input("Enter the string") #HELLO

count = 0 2

#traverse over the string 

for ch in string:
    count = count + 1
          =  5
print("Length:",count)                      

Length: 5

'''
string = input("Enter the string") #HELLO

count = 0 

#traverse over the string 

for ch in string:
    count = count + 1
        
print("Length:",count)                      

# Length: 5

'''
Toggle each character:

Logic Flow:
           1.Traverse Each Character
                      |
             2.If upperCase -> convert to lower
                      |
              3.else lowercase --> uppercase                 
Example:
PyThon ---> pYtHON


string = input("enter the string:") #PyThon
                                     012345
result = ""

for ch in string:
    if ch.isupper():
       result += ch.lower()
               = ""+"p"
               = "pY+"t"->"pYt"
    else:
        result = result+ch.upper()           
               = "p"+"Y"
               = "pYt"+"H"-> "pYtH"+"O"- "pYtHO"+"N"-"pYtHON"
    print(result)
'''

'''
Remove the vowels from the string 

Example: input: Hello 
output: Hll

Logic: 
           1.Traverse over the string 
                      |
              2.Ignore the vowels 
                      |
                3.Add remaining characters              


'''

string = input("Enter the string")
#string = "H E L L O"
    #ch =  0 1 2 3 4
    #ch = 4
result = ""

for ch in string:
    if ch.lower() not in ['a','e','i','o','u']:
        result = result+ch
            #  = "hll"
print(result)

'''

Problem:5
Remove all characters except alphabets 

Example: 
input: "he123@lo"
output:"hello"

Logic Flow:
           1.Traverse over the string 
                     |
            2.Keep only the alphabets       

Input = h e 1 2 3 @ l o
   i  = 0 1 2 3 4 5 6 7
   i=7
result =""

string = input()

for ch in string:
    if ch.isalpha():
       result = result+ch
              = helo
print(result)       
       
        
        
        
'''

        
