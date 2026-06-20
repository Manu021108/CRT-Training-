'''
Problem Statement: 

Simulate the ATM system:
1.Correct pin is required 
2.withdraw only if sufficient balanace is available 
initial balance = 5000
                      Pin check 
                          |
                       Balance check 
                          |
                      withdraw the amount 
                      
                      Balance = 5000
                      pin = input()
                         amount = input()
                         if balance > amount :
                             balanace = balance - amount 
                             display the updated balance 
                         else:
                             insufficient funds 
                    else:
                        print(Invalid pin)                    

'''
balance = 5000

#Taking the pin input 
pin = int(input("Enter the pin"))

#checking the pin 

if pin == 1234:
    #withdrawl amount input 
    amount = int(input("Enter the withdrawl amount:"))
    #check the amount availability 
    if amount <= balance:
        #Deduct the amount from balance 
        balance = balance - amount 
        
        #Display the updated amount 
        print("Withdrawl is successful")
        print("Remaining balanace :",balance)
    else:
        print("Less amount")
        
else:
    print("Invalid pin")        
           
