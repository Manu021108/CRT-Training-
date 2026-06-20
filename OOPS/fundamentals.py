'''
OOPS: Object oriented programming (Paradigm)

programs are organized using objects 
objects contains: 
1.data (variables)
2.behaviour(functions/methods)

OOP not only focuses on functions 
but also real world entities 

car -> Object 
student -> object 

Each Object here:
will have properties and actions 
             |             |
             Variables Methods

Earlier the programming was written without oops 

1.difficult to manage the large level projects 
2.code duplication 
3.less security 
4.difficult maintenance 

OOPs solve the above problems:
1.classes 
2.Objects 
3.encapsulation 
4.Inheritance 
5.abstraction
6.Polymorphism 
'''

#Procedural programming
name = "Ramya"
marks = 30 
def display():
    print(name,marks)
    
display()    
    
#OOP approach:

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 
        
    def display(self):
        print(self.name,self.marks)
 
#object        
s1 = Student("Manish",90)  
s1.display()       
        
#data+functions --->
'''
advantages:
1.code reuasability 
2.Better organization - modular and structure
3.Security -> encapsulation 
4.Easy maintenance: update , debug 
5.real world modelling 
6.Scalability : large applications

       Full stack:front+backend+db
       MERN stack--:
       M: Mongodb --> db
       E:Express -->framework
       React:frontend 
       Node:Run time environment 
       
       frontend:HTML,CSS,JS,React Js 
       backend:Python,Node+Express
       Database:Mysql,PostgreSql,oracle,mongodb
       python-Flask,django,fastapi,streamlit,gradio




'''
'''
class: Blueprint of an object 
collection of var,methods ??

Blueprint:
can be used to build many houses 

'''   
class ClassName:
    pass

'''
class: keyword creates class 
classname : identifiers
pass:empty block

'''
#Object:Instance of a class 
           #or
#actual memory representation of class

class Student:
    pass

#Create an object 
obj = Student()
print(obj)

'''
obj --> instance name (object)
Student--> class name 

'''
class Car:
    brand="Audi"
    #Method
    #self:Refers to current object
    def start(self):
        print("Car started")
        
#create the objects 
#both objects has different memory locations 
c1 = Car()
c2 = Car()
c1.start()
c2.start()
c1.brand #class --> obj searches
#for brand inside the class

#Task:Create a class named as employee
#create two var company name and name_emp
#create two methods to access name and comp_name 
#create two objects and access var and methods

class Employee:
    name ="Kavya"
    company_name = "Google"
    
    #create two methods
    def display(self):
        print("Hello",self.name)
    def start(self):
        print("Hello",self.company_name)  
        
e1 = Employee() #
e2 = Employee() 

print(e1)  
print(e1)         


'''
Constructor:  __init__()
special method
automatically called when object is created 

used : initializing the object data 


'''
class Student:
    
    def __init__(self):  #constructor 
        print("Constructor is called")
        
s1 = Student()    

'''
Student()
|
Object created
|
__init__ automatically called

If No constructor 
manually assign the value 

If yes 
automatic initialization


'''
# If No constructor 
# manually assign the value   

class Student:
    pass 

s1 = Student()
s1.name = "Manish"
s1.branch = "CSE"

#Example with constructor 
class Student:
    
    def __init__(self):
        self.name = "Manish"
        self.age = 21
        
obj1 = Student() 

print(obj1.name)  
print(obj1.age)  

'''
self--> current object (obj1)
self -->obj1

#Constructor with parameters 
'''
class Student:
    #Constructor
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
obj2 = Student("Manish",28)        
print(obj2.name)
print(obj2.age)

'''
self -->obj2
name :"Manish"
age:28

obj2_______
name = "Manish"
age = 28

Step by step
1.object memory allocated 
2.__init__ is called automatically
3.Self points to object 
4.Variables initialized 
5.Object returned 

'''
'''
#default Constructor 

class Test:
    def __init__(self):
        print("Default Constructor")
        
t = Test()   

Parametrized constructor

class Test:
   def __init__(self,x):
       self.x = 100
       
t = test()            
constructor           |    Normal method
Automatically called     Manually call it
Name fixed: __init__     Any name 
Used for initialization  used for operations
Executes during object   Executes when called 
creation

'''
class Student:
    def __init__(self):
        print("constructor")
    #Normal method
    def display(self):
        print("Normal method")    
c1 = Student()
c1.display()

'''
Instance Variables:

variables that belong to an object 
separate copy created for every object 

They store:
  object-specific data 
  
  Student | Name | Marks 
  S1       Manish  98
  S2       Rajesh  99

Each object stores its own data 

'''
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name = name 
        self.marks = marks
        
s1 =Student("Manish",98)   
s2 = Student("Rajesh",99) 

print(s1.marks) 
print(s2.marks)  

'''
s1 object 
---------
name = "Manish"
marks = 98

s2 object 
---------
name = "Rajesh"
marks = 99

Objects do not sahre instance variables 

'''
#Instance methods 
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name = name 
        self.marks = marks 
        
    #instance method 
    def display(self):
        print(self.name) 
        print(self.marks)   
        
s1 = Student("Rajesh",98)  

s1.display()  
'''
s1.display()

Student.display(self)
|
self --->s1 




'''
'''
#Dynamic object properties 
adding the variables dynamically 
after creating object 

class Student:
    pass 
    
s1 = Student() 

s1.name = "Manish"
'''
class Student:
    pass    
s1 = Student() 
s1.name = "Manish"
s1.age = 28
print(s1.name)
    
'''
Class variables:
shared among all the objects 
'''
class Student:
    #class Variable
    college_name = "CITY" 
    def __init__(self,Branch):
        #Instance variable
        self.Branch = Branch  # X Local variable
        #wont creates object data 
        
    #Normal Method 
    def display(self):
        print(self.college_name)
        
s1 = Student("Cse") 
s2 = Student("CSD")
print(s2.college_name)
print(s1.college_name)  

'''
Self: refers to current object 
             Or
reference variable pointing to current object     
''' 

class Student:
    def display(self):
        print("hello") 
        
s1 = Student()
s1.display() 
'''
s1.display()
    |
    Student.display(s1)
    |
    self-s1(self points to s1)
'''
class Student:
    
    def show(self):
        print(self)
        
s1 = Student()   
s2 = Student() 
print(s1) 
print(s2)       
s2.show()
        
'''
       student class 
       -------------
       College = CITY  #stored in class memory
       -------------
         |     |
         s1   s2

class Employee:
    company = "Google"
    def display(self):
       print(self.company)
       
e = Employee()     
Two ways access:
print(e.company)

#No object use 
print(Employee.company)
'''
'''
#class methods:
work with class variables 
Operate on class level data 

@classmethod - decorator
'''
#Basic example for class method 

class Student:
    college = "CITY"
    
    @classmethod
    def show_college(cls):
        print(cls.college)
            
Student.show_college()           

        
'''
@classmethod:
decorator which tells python:
This method belongs to class not object 

self --> current object 
cls --> current class 

'''
#TasK; Create a clas named as employee
#create one class var
#use @classmethod to apply
# on method company_name 
#print the comnpany name 
#using multiple objects 
        
class Employee:
    company = "Microsoft"
    @classmethod
    def change_company(cls,new_name):
        cls.company = new_name
        
Employee.change_company("Google") 
print(Employee.company)       
          
#objects 
# e1 = Employee()
# e1.show_company()  
# e2 = Employee()
# e2.show_company()      
'''
diff btw instance method and class method 

instance method         | class method
works on the object      Works on class data 
data 
uses self                cls - current class
need object              directly using class 
Access the instance var  Access class variables



'''
class Student:
    college = "CITY"
    
    #instance method:refers object
    def instance_method(self):
        print("Instance method")
        
    #class method : refers class
    @classmethod
    def class_method(cls):
        print("Class Method")
        
'''
Static Method:
does not uses : object,class 

They Are:
utility/helper methods

Not uses:
self,cls -->

Example: 
add()
multiply()

@staticmethod--> decorator 
'''
#Static Method Example:
class Calculator:
    @staticmethod  #helper method 
    def add(a,b):
        return a+b  
    
print(Calculator.add(10,20))  

#independent method 
#logically belongs to class but
# no data required from class   

class Message:
    @staticmethod
    def greet():
        print("hello students") 
print(Message.greet())
'''
instance method 
|
works with object 

class method
|
works with class 

static method:
|
works independent of object or classs

'''


#Task:Create a class named as Student
#create constructor 
#class variable
#instance varibles 
#instance method 
#class method 
#static method 

'''

https://assessments.prepinstaprime.com
/CITY/dashboard/startTest/CITY00026

Passcode:594558


'''
