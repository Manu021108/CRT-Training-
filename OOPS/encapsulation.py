'''
What is encapsulation?
Binding data and methods together 
into a single unit 

And:
restricting direct access to data 

ENcapsulation protects the data from 
1.Unauthorized access 
2.accidental modifications

SImilarly In oops:
data is hidden inside the class 
accessed using methods 

Key-idea 
data+methods
    |
combined into a single unit 
    |
Controlled access


Features of ENcapsulation:
1.Security: 
2.data hiding 
3.Controlled access:
4.Better Maintenance 
5.Better organization
'''
#No encapsulation
# balance = 50000

# balance = -50000

#Encapsulation:
class Bank:
    def __init__(self):
        self.balance = 10000
        
    def deposit(self,amount):
        self.balance +=amount   
        
    def show_balance(self):
        print(self.balance) 
        
b1 = Bank()   
b1.deposit(5000)  
b1.show_balance()      #data and methods are bound together 

#data hiding 
#restricting access to direct variables

'''
Goal: Prevent the data modifications 
misues of data 

Access modifiers in python:
1.Public: 
2.Protected: _single_underscore
3.private: __double_underscore


'''
#1.Public: Members can be accessible everywhere
#default access type in python

class Student:
    def __init__(self):
        self.name = "Manish"
        
s1 = Student()
print(s1.name)
'''
Accessed anywhere
No restriction
Default behaviour 
'''


#protected:_ single_underscore 
#should not be accessed directly outside the class

class Student:
    
    def __init__(self):
        self._marks = 90
        
s1 = Student()
print(s1._marks)        
        
'''
Python protected members 
are not exactly protected 

_marks: Prtotected by convention

Please dont access it directly

where to use?
1.During inheritance 
2.for internal usage
'''
'''
Private: __ underscore
used for : strong data hiding 
'''
class Student:
    def __init__(self):
        self.__marks = 90
               
s1 = Student()
# print(s1.__marks)

#Name Mangling 

# __marks
# |
# _Student__marks
'''
Prevent:
accidental direct access 
accidental overriding 
'''
#Can i access private var inside the class
class Student:
    def __init__(self):
        self.__marks = 90
        
    def show(self):
        print(self.__marks) 
        
s1 = Student()
s1.show()   #accessed within the same class
        
#try to access using name mangling 
class Student:
    def __init__(self):
        self.__marks = 90
        
s1 = Student()
#Iam using name mangling to access 
print(s1._Student__marks)  

'''
self.__marks
    |
Python will convert 
     |
 self._Student__marks        
'''
'''
Access Modifiers   | Syntax | Accessible outside 
1.Public             Variable  Yes 
2.Protected         _variable  yes(convention only)
3.Private           __variable No directly

#Task:
create a class named "BankACcount"
#balance -->private
#deposit 
#withdraw amount 
#check for balance 
#print balance using name mangling
'''
class BankAccount:
    def __init__(self):
        #Private variable
        self.__balance = 10000 
        
    def deposit(self,amount):
        self.__balance += amount 
        
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount
        else:
            print("Insufficient funds")  
            
    def show_balance(self):
        print(self.__balance)  
        
b1 = BankAccount()
b1.deposit(1000)
b1.withdraw(2000)  
b1.show_balance()
print(b1._BankAccount__balance)      

'''
Getters and setters:
getters -- read the data 
setters --> modify/update the data

#why use?

student.marks = -90
No validation 

'''
#without getters and setters 
class Student:
    def __init__(self):
        self.marks = 90
s1 = Student() 
s1.marks = -50 # accepted 
print(s1.marks)       
            
#Using getters and setters
class Student:
    def __init__(self):
        self.__marks = 90
        
    #getter method 
    
    def get_marks(self):
        return self.__marks   
    #setter method 
   
    def set_marks(self,value):
        if value >= 0:
            self.__marks = value 
        else:
            print("Invalid marks") 
            
b1 = Student()
print(b1.get_marks()) 
b1.set_marks(95) 
print(b1.get_marks())    
b1.set_marks(-95)
print(b1.get_marks())  

#Task:Create a class BankAccount
#create getter for returning balanace 
#create  setter for updating balance 
#amount  >= 0                    

'''
obj.setmarks
obj.getmarks




'''
class Student:
    def __init__(self):
        self.__marks = 90
        
    #getters
    @property
    def marks(self):
        return self.__marks   
    
    #Setter 
    @marks.setter
    def marks(self,value):
        if value >= 0:
            self.__marks = value 
        else:
            print("Invalid marks")  
            
s1 = Student()
print(s1.marks)
s1.marks = 95
print(s1.marks) 
'''
Problem:1

STudent marks validator
Create a class Student:
Requirements:
Private var --> __marks
method set_marks(marks)
method get_marks()

rules:
Marks must be btw 0-100
otherwise print 

invalid marks 
Example: Input[85] --> 85
               205--> invalid marks 
'''
class Student:
    def __init__(self):
        self.__marks = 0
        
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if 0<=marks <= 100:
            self.__marks = marks 
            
        else:
            print("Invalid Marks")  
            
marks = int(input()) 
s = Student()
s.set_marks(marks)
if 0 <= marks <= 100:
    print(s.get_marks()) 
                           
                           
'''
EMployee salary manager 
Create a class named as Employee
Requirements:
1.Private var - __salary 
2.salary should not be < 15000
3.Method increase_salary(percent)

if invalid:
invalid salary 

input:20000
percent:10 
output: 22000

'''
class Employee:
    def __init__(self):
        self.__salary = 0
        
    def set_salary(self,salary):
        if salary >= 15000:
            self.__salary = salary 
        else:
            print("Invalid Salary") 
    def increase_salary(self,percent):
        self.__salary += (self.__salary*percent/100)
        
    def get_salary(self):
        return self.__salary
    
salary = int(input())
percent = int(input())

e = Employee()
e.set_salary(salary) 
if salary >= 15000:
    e.increase_salary(percent)
    print(e.get_salary()) 
    
'''
Password Manager:
Create a class PasswordManager:
Rules:
1.minimum 8 characters 
2.one uppercase
3.one lowercase
4.one digit 

if invalid 
Weak Password 
else:
Password Set successfully

Example: "Manish123"
output:Password set successfully
'''
class PasswordManager:
    def __init__(self):
        self.__password = "" 
        
    def set_password(self,password):
        upper = False
        lower = False
        digit = False
        if len(password) < 8:
            print("Weak Password") 
            return 
        for ch in password:
            if ch.isupper():
                upper = True 
            elif ch.islower():
                lower = True 
            elif ch.isdigit():
                digit = True 
                
        if  upper and lower and digit:
            self.__password =  password   
            print("Password Set successfully")  
        else:
            print("weak password")
                
    def get_password(self):
        return self.__password 
    
password = input()

p = PasswordManager()
p.set_password(password)

'''
Problem-4
E-Commerce shopping Cart
Create a class ShoppingCart
Features:
1.private var - __total 
2.add items 
3.remove the items 
4.apply discount

Rules:
1.Total should never become zero
2.discount only if total > 1000
Methods:
1.add_item(price)
2.remove_item(price)
3.apply_discount(percent)
4.get_total()
'''
class ShoppingCart:
    def __init__(self):
        self.__total = 0  
    def add_item(self,price):
        if price > 0:
            self.__total += price 
    def remove_item(self,price):
        if price <= self.__total:
            self.__total -=price 
    def apply_discount(self,percent):
        if self.__total > 1000:
            self.__total -=(self.__total*percent/100) 
            
    def get_total(self):
        return self.__total          

n = int(input())
cart = ShoppingCart()
for _ in range(n):
    price = float(input())
    cart.add_item(price)  
remove_price = float(input())
cart.remove_item(remove_price)  
discount = float(input())
cart.apply_discount(discount) 
print(cart.get_total())                                                            