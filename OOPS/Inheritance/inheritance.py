'''
What is inheritance?
a mechanism where one class acquires the 
properties and methods of another class
                or 
one class reuses the features of 
another class 

SImple understanding.

a child class can 

use variables 
use methods 
of parent class without 
rewriting the code  

Example:
vehicles:
car,bike,bus

All vehicles have
start(),stop()
No need to repeated code 

write code once 
|
use num of times 

Advantages or why?
1.Code Reusability
2.Reducing the code duplication
3.Better Organization
4.Easy Maintenance

Terms:
parent: Base or super class 
child:  sub class/derrived   

          Parent
             |
           Child 
           
'''
#syntax:
class Parent:
    pass 

class Child(Parent):
    pass

#Basic EXample:
class Animal:
    def eat(self):
        print("ANimal is eating")
        
#child class 
class Dog(Animal):
    pass 

#have to create object
# for child class
d1 = Dog()
d1.eat()
'''
Dog class does not contains eat()
              |
  Python seaches in animal class 
              |
     Method is found and executed                     
'''
#No Inheritance 

class Dog:
    def eat(self):
        print("eating")
        
class Cat:
    def eat(self):
        print("eating")        

#with inheritance 
class Animal:
    def eat(self):
        print("Eating")  
    
class Dog(Animal):
    pass
class Cat(Animal):
    pass 
c1 = Cat()
c1.eat()

#accessing the parent variables 
class Person:
    def __init__(self):
        self.name = "Glory"
class Student(Person):
    pass
       
s1 = Student()
print(s1.name)           
'''
Types of Inheritance in python
1.Single Inheritance 
2.Mutiple Inheritance 
3.Multilevel inheritance
4.Hierarichal inheritance 
5.Hybrid Inheritance

1.Single Inheritance:
One child class inherits from one parent 

          Parent
             |
           Child
             
'''
#Example:
class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("Barking")   
        
d1 = Dog()
d1.eat()
d1.bark()    

'''
2.Multiple Inheritance:

one child class inherits
from multiple parents 

             Parent 1    Parent2
                 \       /
                   Child
'''
#Example:
class Father:
    def money(self):
        print("Father's Money") 
        
class Mother:
    def gold(self):
        print("Mother's Gold") 
        
class Child(Father,Mother):
    pass   

c1 = Child()
c1.gold()
c1.money()   

'''
#Multilevel Inheritance 
Inheritance chain of mutiple levels 

             GrandParent
                  |
               Parent
                  |
                Child   
'''
class Grandparent:
    def house(self):
        print("Grand Parents House")
        
class Parent(Grandparent):
    def car(self):
        print("Parents car")
        
class Child(Parent):
    def bike(self):
        print("Child's Bike")  
        
c1 = Child()
c1.house()
c1.car()
c1.bike()  

'''
Hierarichal Inheritance:

Multiple child classes
inherit from one parent

           Parent
           /     \
         Child1  Child2      
'''                   
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
class Cat(Animal):
    def meow(self):
        print("Meow")
                                     
c1 = Cat()
c1.eat() 

'''
#5.Hybrid Inheritance:
two or more inheritance types:
1.hierarichal and multiple
                   
                   A
                  /  \
                 B    C
                 \   /
                   D
                      
'''
class A:
    def show_a(self):
        print("class A")
class B(A):
    def show_b(self):
        print("Class B")
class C(A):
    def show_c(self):
        print("Class C")
        
class D(B,C):
    def show_d(self):
        print("Class D") 
        
d1 = D()
d1.show_a() 
d1.show_b()
d1.show_c()
d1.show_d() 

#Check the inheritance 
class Animal:
    pass 
class Dog(Animal):
    pass
c1 = Dog()

print(isinstance(c1,Animal))
print(issubclass(Dog,Animal))
                                  
class Parent:
    def __init__(self):
        print("Constructor called")
class Child(Parent):
    pass                  

c1 = Child()
'''
1.Methods
2.Variables
3.constructor

'''
'''
Problem:1 
create a parent class Animal
with method sound()

that should print 
Animal Makes sound 

Create a child class Dog()
that inherits the Animal

create object of Dog and call
inherited sound()

Problem-2:
Student and college
create a parent class College
class var -->college name 
create a child class student with:
instance var-->student_name

display:
1.college_name 
2.Student_name

'''
class College:
    college_name = "CITY"
    
class Student(College):
    
    def __init__(self,student_name):
        self.student_name = student_name
        
    def display(self):
       print(self.college_name)
       print(self.student_name) 
       
stu = Student("Rajesh")

stu.display()          
'''
Problem-3
Create:
Vehicle class with method start()
car class inheriting Vehicle
Sportscar class inheriting the Car
add Method:
speed()
inside the sports Car:
call:
start()
speed() using sportscar object

'''
class Vehicle:
    def start(self):
        print("Vehicle Started")
        
class Car(Vehicle):
    pass
class Sportscar(Car):
    def speed(self):
        print("speed")
        
sp = Sportscar()
sp.start() 
sp.speed()               

'''
Eployee skill system 
create:
class Programmer with method coding()
class Designer with method designing()

create a child class Employee inheriting
both classes 
call both methods using EMployee objects 

'''
class Programmer:
    def coding(self):
        print("Writes code")
        
class Designer:
    def designing(self):
        print("designing")
        
class Employee(Programmer,Designer):
    pass

e1 = Employee()
e1.coding()
e1.designing()
'''
Employee Bonus Mgmt
A company wants to calc
yearly bonuses for 
different types of employees 

create a base class Employee:
with:
name , salary 
create method:
calculate bonus()

then create two child classes 
developer
Bonus = 20% of salary 
manager 
Bonus = 35% of salary 
write a program to:
1.Take employee details as input
2.create objects based on employee type
3.Display:
employee name 
role
Bonus amount 

input format:
role,name,salary

output format:
Name:<name>
Role:<role>
Bonus:<bonus>

Sample:
3
Developer Rahu1 50000
Manager   Sneha 80000
Developer Arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00

'''
class Employee:
    def __init__(self,name,salary):
        self.name= name  
        self.salary = salary
    def calculate_bonus(self):
        return 0         
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20    
    
class Manager(Employee):
      def calculate_bonus(self):
        return self.salary * 0.35  
    
n = int(input())
employees = []
for _ in range(n):
    role,name,salary = input().split() 
    salary = int(salary) 
    if role == "Developer":
        emp = Developer(name,salary)
    elif role == "Manager":
        emp = Manager(name,salary) 
    employees.append((role,emp))
    
for role,emp in employees:
    print(f"Name:{emp.name}")  
    print(f"Role:{role}") 
    print(f"Bonus:{emp.calculate_bonus()}") 
    print()          
'''
Online course Access System
An online learning platform provides 
different levels of course access
create a parent class Course: with
-> Student_name 
create a method:
access_level():
Then create two child classes 
->FreeCourse
Access Level = "Limited Access"
->Premium Course 
Acess Level = "Full ACcess"
write a program:
1.Accept student details 
2.Create objects using inheritance 
3.Print Student access information

input:course_type,student_name

sample:
4
Free Amit
Premium Neha
Free Rohan
Premium Rakesh

output:
Student:Amit
Course_type:Free
Access:Limited Access 
'''
class Course:
    def __init__(self,student_name):
        self.student_name = student_name
        
    def access_level(self):
        return "No Access"
class FreeCourse(Course):
    def access_level(self):
        return "Limited Access"    
class PremiumCourse(Course):
    def access_level(self):
        return "Full Access" 
    
n = int(input)  
students = []
for _ in range(n):
    course_type,name = input().split()
    
    if course_type == "Free":
        student = FreeCourse(name)
    elif course_type == "Premium":
        student = PremiumCourse(name)    
       
    students.append((course_type,name))   
for course_type,student in students:
    print(f"Student:{student.student_name}")
    print(f"Course_Type:{course_type}")
    print(f"Access:{student.access_level}")
    print()
    