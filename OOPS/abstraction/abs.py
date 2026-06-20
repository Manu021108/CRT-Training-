'''
what is abstraction?
hiding iternal implementation details
showing the essential
features to the user 
                  or 
         what operation is done?
         But Not:
         how operation is working internally         
-->complexity is hidden from the user 

why use abstraction?
1.Reduces the complexity 
2.Improves the security 
3.Better Maintenance
4.Cleaner code 
5.Standardization

#Abstraction in python 
Python supports abs using :
abstract classes 
abstract methods

# ABC Module
ABC -- Abstract Base Class
    
Abstract class 
blueprint of a class 
cannot create objects directly     

#defines  basic  common structure  

abstract can have :
1.abs methods 
2.normal method   

#Abs Method 
Methods declared but:
   implementation not provided 
   
Child class Must Implement it   
Example:
vehicle

->start()
    
'''
#ABC -->Abstract Base Class

from abc import ABC,abstractmethod

#abstract class 
class Vehicle(ABC):
    #Abstract method
    @abstractmethod
    def start(self):
        pass
    
# v = Vehicle()

from abc import ABC,abstractmethod

#abstract class 
class Vehicle(ABC):
    #Abstract method
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle): 
    def start(self):
        print("Car Started")    
        
c1 = Car()
c1.start() 

#Example:2
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 
class Dog(Animal):
    def sound(self):
        print("dog barks")  
d1 = Dog() 
d1.sound()    

#multiple abstract methods 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass 
class Rectangle(Shape):
    def area(self):
        print("Area Formula")
    
    def perimeter(self):
        print("Perimeter formula")  
        
r1 = Rectangle()

r1.area()
r1.perimeter()   

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 
    #Normal method 
    def sleep(self):
        print("sleeping")  
        
class Dog(Animal):
    def sound(self):
        print("Bark")
        
d2 = Dog()
d2.sound() 
d2.sleep() 

#Payment system:
# pay()
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
                    
class Phonepe(PaymentGateway):
    def pay(self):
        print("Paid using phonepe")  
class Paytm(PaymentGateway):
    def pay(self):
        print("Paid using paytm") 
        
pp = Phonepe()
pt = Paytm()
pp.pay()
pt.pay()
'''
#Task:create an abstract class PayGateway
with two abs methods 
1.pay
2.refund 
but amount --: param 
create child class implementations 
1.CreditcardPay
2.UPI Pay 



'''
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass 
#child 1 
class CreditCardPay(PaymentGateway):
    def pay(self,amount):
        print(f"Pay {amount} using credit card")
        
    def refund(self,amount):
        print(f"refunded {amount} using credit pay")        
        
class UpiPay(PaymentGateway):
    def pay(self,amount):
        print(f"Pay {amount} using UPI")
        
    def refund(self,amount):
        print(f"refunded {amount} using UPI")     
        
c1 = CreditCardPay()
c2 = UpiPay()

c1.pay(5000)   
c2.refund(6000)

'''
Create an abstract class Employee 
with abs methods:
calculate_salary()
create:
FulltimeEmployee
PartTimeEmployee
Rules:fulltimesalry = 50000
parttimesalary = hours*500

'''
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass 
#child1 
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
    
class PartTimeEmployee(Employee):
    def __init__(self,hour):
        self.hour = hour
        
    def calculate_salary(self):
        return self.hour*500 
         
c1 = FullTimeEmployee()
c2 = PartTimeEmployee(40)
print(c1.calculate_salary())  
print(c2.calculate_salary())      

'''
Food delivery System:
Create an abstract class Restaurant 
with methods:
prepare_food()
delivery_time()
create child classes:
1.PizzaShop
2.BurgerShop
display:
food preparation message 
delivery time

'''
'''
Ride Booking application 
class - > Ride
method:
calculate_fare(distance)
child:
1.BikeRide
2.CarRide
3.AutoRide 
Rules:
Bike --> distance*10
Car -->distance * 20
Auto -->d *15
'''
class Ride(ABC):
    @abstractmethod
    def calculate_fare(self,distance):
        pass
    
class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance*10
       
class CarRide(Ride):
    def calculate_fare(self, distance):
        return distance*20
    
class AutoRide(Ride):
    def calculate_fare(self, distance):
        return distance*15
           
'''
Magic Methods/Dunder Methods 
Dunder --> Double Underscores 
__ double underscores 
Example:   __init__
           __add__
wh? 
operator overloading 
+
_
/ 

print(10+10) #20
print("Helo"+"world") #HelloWorld

'''
# +
class Number:
    def __init__(self,value):
        self.value = value
        
    def __add__(self,other):
        return self.value + other.value 
    
n1 = Number(10)
n2 = Number(20)
print(n1+n2)    
    
#Make your objects work 
# like built in types  

#strings:
class Student:
    pass 

s1 = Student()
print(s1)

#__str__
class Student:
    def __str__(self):
        return "Student Object"
    
s1 = Student()
print(s1)    

#len() method
class Team:
    def __len__(self):
        return 5
t1 = Team() 
print(len(t1))   

# == __eq__

class Students:
    def __init__(self,marks):
        self.marks = marks
        
    def __eq__(self, value):
        return self.marks == value.marks    
      
s1 = Students(90)
s2 = Students(90)
print(s1 == s2)

# repr --> official object representation 
#debugging 
#development

class Student:
    def __repr__(self):
       return "Hello"
   
s1 = Student()
print(repr(s1)) 
'''
https://assessments.prepinstaprime.com/
CITY/dashboard/startTest/CITY00029

passcode: 913432
'''
           