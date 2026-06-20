'''
sms ---> click on this link
to get 100 rs 

if sms has "click on link":
    print("Spam") 
    
win money 200000 by playing games    

100 percent placements get the opportunity 

nested if or elif to check if suspicious msgs are available 
spam msg 


message = input():

if "win money" in message:
    print("Spam message") 

'''

#Taking the message from the user 
message = input("Enter the message: ")

#Conversion of message to lower 
message = message.lower()


#Spam -- detetction 

if "win money" in message:
    print("Spam message detected")
elif "free offer" in message:
    print("Spam message detected")
elif "click this" in message:
    print("Spam message detected")
else:
    print("No spam")    
        

'''
a = 10
b = 10 
a is b   ---?True/False

is ---> Identity (Memory )

a in b ? --? False 

in ---> checks for the value


a = [1,2,3]
b = [1,2,3]
c = a 
is ---> Identity(Memory location)

a is b  ? False 
a in b ? False

a ---> [1,2,3]  False 

1 in b ? True 

Identity : is , is not 
membership operators: in and not in 

'''
