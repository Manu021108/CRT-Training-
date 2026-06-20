#Take the username 
username = input("Enter the username:")

#First Condition
if username == "admin":
    password = input("Enter the password:")
    
    #Nested condition 
    if password == "1234":
        print("Login Successful")
    else:
        print("wrong password")   
        
else:
    print("Invalid username")         