'''
               Logic for password verifier 
                       
                       Store the original password
                                 |
                          Ask the user for input 
                                 |
                Compare the entered password with original pass 
                                 |
                       if Wrong:
                            Show error message 
                            ask again
                                 |
                       if correct:
                            stop loop
                            login successful     
'''

correct_password = "1234"

user_password = ""

#Loop unitil the password is correct 
while user_password != correct_password:
    #take the input 
    user_password = input("Enter the password:")  #1234
    
    if user_password != correct_password:
        print("Invalid password, Try again")
    
#Loop ends and prints successful         
print(" Login Successfull")      