# '''
# Module:
# a module is simply a python
# file containing code 

# why?
# 1.large file 
# 2.hard to maintain
# 3.difficult to reuse 

# modules:
# reusability 
# organinzation
# Readability 
# COllaboration 
# '''
# from . import calculator

# print(calculator.add(1,2))
# print(calculator.sub(10,5))

# #Task: create a module named as greeting
# from . import greeting
# greet1 = greeting.greet()
# print(greet1)

# #Task:
# # from Looping import new
# # print(new.hello())

# #built in modules:
# import math
# print(math.sqrt(33))
# print(math.factorial(5))

# #from import 
# from math import sqrt,pow
# sqrt(3)
# pow(2,2)

# import math
# import random
#     #(or)
# import math,random

# #all the attributes from math
# from math import *

# # from Looping import new
# # new.hello()

# #colection of modules is called package 

# import datetime as dt 
# print(dt.datetime.now())

# '''
# Module    meaning 
# 1.math   Mathematics 
# 2.random Random values 
# 3.datetime Date & Time
# 4.os       Operating system 
# 5.sys     Python runtime

# '''
# # help("modules")
# '''
# #Package:
# is a folder containing multiple modules

# School/  --> package 
#    student.py
#    teacher.py
#    management.py
   
# main.py --> from school import student    

# __init__.py
# Purpose:
# special file used to identify package
# 1.marks directory as package 
# 2.Runs initialization code 
# 3.controls the import 



# '''


# # builtin methods 
# import math 
# #round upward
# print(math.ceil(5.2))

# #floor()-->
# print(math.floor(5.2))

# #constants 
# print(math.pi)
# print(math.e)


# #Task:Area of a circle
# import math 
# r = 7
# area = math.pi*r*r
# print(area)

# #Random builtin mathods 
# #used for random values 

# import random 

# #randint()
# print(random.randint(1,100))

# #choice()
# fruits = ["Apple","Banana","Pineapple"]
# print(random.choice(fruits))

# #random()--> 0.0 - 1.0
# print(random.random())

# #shuffle()
# cards = [1,2,3,4]
# random.shuffle(cards)
# print(cards)

# #Task: Build the dice simulator
# import math 
# print(random.randint(1,6))

# #date?
# import datetime
# print(datetime.date.today())

# #custom date 
# d = datetime.date(2026,6,18)
# print(d)

# #Build the age calculator
# import datetime
# birth_year = 2006
# current_year = datetime.date.today().year
# print(current_year-birth_year)

# '''

# '''
# #Importing from package 
# # from school.student import show_student
# # show_student()

import os

print(os.getcwd())

# mkdir --make directory
# print(os.mkdir("PythonClass"))

# #change the name (rename)
# os.rename("PythonClass","2027Batch")

#listdir()
print(os.listdir())

# #remove directory
# os.rmdir("2027Batch")

#Task:Display all the files in a dir

import os 
files = os.listdir()
for file in files:
    print(file)

#Module - sys 
#provides the information about 
#python interpreter

import sys
print(sys.version)

print(sys.exit())
print(sys.path())