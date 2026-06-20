'''
What is polymorphism?
poly--> Many
morphism -> forms 
same method/operators will behave differently

Example:

print(5+3) #8
print("Hello"+"world") #Helloworld

       same operator
           |
        BUt diff behaviours    
Types of polymorphism:
1.Compile time 
2.Run time polymorphism 

#compile time -- method overloading 
#NO method overloading in python 

Method Overloading:

same method names 
       +
 diff parameters  
 #defualt arguments
 #  *args ---var len arguments      

#Java --> add(int,int) 
#       -> add(int,int,int)

Python approach:
class Calculator:
    def add(self,a,b,c=0):
        print(a+b+c)
        
c1 = Calculator()  
c1.add(10,20)
c1.add(10,20,30)      

#Run Time Polymorphism:
-->method overriding
'''
class Bird:
    def fly(self):
        print("Bird Flying")
class Eagle(Bird):
    def fly(self):
        print("Eagle is flying")        
        
e1 = Eagle()
#method is choosen during run time
e1.fly()   

#Duck typing in python 
#python focuses on
# behaviour not object type     

class Duck:
    def sound(self):
        print("Quack")
class Dog:
    def sound(self):
        print("Bark")   
        
def make_sound(obj):
    obj.sound()
    
d1=Duck()
d2=Dog()        

make_sound(d1) 
make_sound(d2)        