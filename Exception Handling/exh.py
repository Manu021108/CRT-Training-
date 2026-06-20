# '''
# Error: An error is a problem
# in the program causing 
# abnormal termination 
# 1.Syntax Error
# 2.Run time errors --Exceptions 
#    ---> Occurs while executing the program 
   
#    Example: 
#    a = 10
#    b = 0 
#    c = a/b  --> ZeroDivisionError
   
#    3.Logical Errors:
#    Program runs but gives wrong output 
#    Example:
   
#    print(2*(3+5))
   
#    What is exception handling?
#    Exception handling is a mechanism to handle 
#    run time errors gracefully without stopping 
#    the program 
#    without exeception:
#    1.Program crashes 
#    2.Poor User experince 
#    3.Data loss possible 
   
#    With exception:
#    1.Program will execute normally 
#    2.Proper error message 
#    3.Safer application 
   
#    #Basic Exception:
#    syntax:
   
#    keywords:try,catch,finally,raise,else
   
#    try:
#       risky code 
#    except:
#       handling code     
# '''

# #lets write our first program
# # try:
# #     num = int(input("Enter a number:"))
# #     print(10/num)
# # except:
# #     print("Some error occured")    

# #Risky code will be inside try
# #if exception occurs ->except executes 

# #above is not a good practice 
# #Hides actual problem 
# #difficult to debug 

# try:
#     num = int(input("Enter a number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("cannot divide with 0")    
    
# except ValueError:
#     print("Input should not be a string")      
    
# '''
# Common python exceptions:
# 1.ZeroDivisionError ---> Divide with 0 
# 2.ValueError -->Invalid input
# 3.TypeError -->wrong datatype
# 4.IndexError --> Invalid Index
# 5.KeyError -->Invalid dictionary key
# 6.FileNotFoundError -->File Missing 
# 7.AttributeError -->Invalid Attribute 
# 8.NameError --> Variable is not defined 

# '''
# #Example:
# try:
#     lst = [10,20,30]
#     index = int(input("Enter the index:"))
#     print(lst[index])

# except IndexError:
#     print("Index out of range")
    
# except ValueError:
#     print("Please enter integer") 

# #Else: if no exception occurs
# '''
# try:
#    code
# except:
#    handling 
# else:
#    success block      
# '''
# try:
#     lst = [10,20,30]
#     index = int(input("Enter the index:"))
#     print(lst[index])

# except IndexError:
#     print("Index out of range")
    
# except ValueError:
#     print("Please enter integer") 
    
# else:
#     print("No exception occured")    
    
# #another example: 
# try:
#     num = int(input("ENter number:"))
#     result = 100/num 
# except ZeroDivisionError:
#     print("zero")
# else:
#     print(result)     
    
# #finally 
# '''
# finally block executes always
# used for:
# 1.closing files 
# 2.closing database connections
# 3.cleanup activities

# try:
#    code
# except:
#    handling 
# finally:
#    cleanup code 


# '''
# try:
#     file = open("data.txt")
    
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Execution completed") 
    
#ATM Machine
try:
    print("transaction is processing") 
except:
    print("Transaction failed")
finally:
    print("Thanks for using ATM")  
    
try:
    a = 10/0
except ZeroDivisionError as e:
    print("error:",e)  
    
#Nested try blocks 
try:
    print("outer try")
    try:
        num = int(input("Enter number:"))
        print(10/num)
    except ZeroDivisionError as e:
        print("Error:",e)      
except:
    print("Outer Exception")
    
#raise: used to manually 
# generate exceptions

age = int(input("Enter the age:"))
if age<18:
    raise ValueError("Age should be 18 or greater")
print("Eligible")

#why custom exceptions;

class MyException(Exception):
    pass
    
               
#Bank Application:

class InsufficientBalance(Exception):
    pass

balance = 5000
withdraw = int(input("Enter the amount"))   
if withdraw > balance :
    raise InsufficientBalance("Not enough balance")
print("Withdraw successful")  

#Task:write a custom exception

#Exceptions with oops concept 
#Exceptions are mostly used with methods 

#STudent Result System
class Student:
    def __init__(self,marks):
        self.marks = marks  
    def calculate_result(self):
        try:
            average = sum(self.marks)/len(self.marks)   
            print(average) 
        except ZeroDivisionError as e:
            print("Error:",e)   
s1 = Student([]) 
s1.calculate_result()   

#Login system:
class LoginSystem:
    def login(self,username,password):
        try:
            if username !="admin" :
                raise ValueError("Invalid username") 
            if password !="admin123":
                raise ValueError("Invalid Password")
            print("Login successful")
        except ValueError as e:
            print("Error:",e) 
            
#Generic Exceptions:

try:
    print(10/0)
    
except Exception as e:
    print(e)      
    
'''
Accept account balance 
nd withdrawl amount
Raise Exception iF:
1.withdrawl amount is -ve 
2.withdrawl amount exceeds balance
3.withdrawal amount exceeds daily 
limit of 25000
4.display remaining balanace 
if transaction successful 
'''
# Custom Exceptions
class InsufficientBalance(Exception):
    pass              
class WithdrawlLimit(Exception):
    pass   
class InvalidInput(Exception):
    pass  

class ATM:
    def __init__(self,balance):
        self.balance = balance  
        
    def withdraw(self,amount):
        try:
            if amount <= 0:
                raise InvalidInput("No negative") 
            if amount > 25000:
                raise WithdrawlLimit("No more then 25")
            if amount>balance:
                raise InsufficientBalance("Insuff")
            self.balance -=amount 
            print("Transaction is successful")
            print("Balance:",self.balance)        
                   
        except InsufficientBalance as e:
            print(e)
        except InvalidInput as e:
            print(e)
        except WithdrawlLimit as e:
            print(e)        
            
balance = int(input())
amount = int(input())  
obj = ATM(balance)  
obj.withdraw(amount)       