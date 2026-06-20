'''
what is dict?
list --> collection of ordered elements
mutable--> can be modified
tuple --> collection of ordered elements 
Immutable --> cant be modified 

dict: collection of key-value pairs 

     key: values 
     08:"Manish"
     dict : {}
     
#Mutable:can be modified 
#'keys' are immutable and values are mutable
Not allows duplicates of-- keys 
Values can be duplicates 
No fixed indexing 
searching is very efficient: O(1)
dict uses hashing technique to search hence O(1)

why we use dict?
1.Labels 
2.Properties 
3.Mapping the relationships 

list = ["Manish","08",26]    
#creation of dictionary
student = {
    "Name":"Manish",
    "RollNo":08,
    "Age":26   
} 






'''
#creation of dictionary
student = {
    "Name":"Manish",
    "RollNo":8,
    "Age":26 ,
} 
print(student)

#2nd method -->dict()
student1 = dict(name = "Ramya",
               age = 21,Branch = "CSE")

print(student1)

#3rd Method: empty dict 

data = {}

print(data)

# list =[10,20,30,40]
#         # 0 1  2 3
# list[0]

print(student["Name"])
print(student["Age"])
'''
feature        List    dict
ordered        yes      no
access(indexing) yes    keys no
arr[0]          yes    student["Keys"]

'''

employee = {}

employee["Name"] = "Lokesh"
employee["age"] = 21

print(employee)

#update the value
employee["age"] = 24

print(employee)

#delete the value 
employee.pop("age")

print(employee)

#2nd method dele

del student["RollNo"]
print(student)

#dictionary methods 

#Keys() --> returns the keys 
print(student.keys())

#Values() -->return all the values
print(student.values())

#items() --> returns all the items in dict
print(student.items())

# print(student["Branch"])
#when I use this --> keyerror

#access the elements 
print(student.get("Branch"))
#None

#update() --> add mutiple elements 
student.update({"Branch":"CSE","College":"CITY"})

print(student)

#popitem:Removes the last inserted pair 
student.popitem()
print(student)

#looping on dictionary
for i in student:
    print(i)
    
#iterating on values 
for value in student.values():
    print(value)   
    
for key,value in student.items():
    print(key,value) 
    
#Nested dictionaries: dict inside dict
students = {
    "s1":{
        "Name":"Rajesh",
        "Branch":"AI"
    },
    "s2":{
        "Name":"Ravi",
        "Branch":"AIML"
    }
}        
print(students["s1"]["Name"])

#can i store list inside the dict ?

student = {
    "Name":"Harish",
    "Marks":[90,80,60,95]
}

print(student)

#you can store multiple dict in list

students =[
    {"Name":"Rajesh","Branch":"CSE"},
       #0
    {"Name":"Praful","Branch":"CSD"}
    #1
]
students[0]["Name"]

#Dict comprehension 

#{key:value for variable in iterable}

squares  = {x:x*x for x in range(1,11)}
print(squares)

#keys: Rules 
'''
int
string
tuple
list --- no
dictionary -->

student ={
    1:"Manish",
    "Roll":08,
    (1,2):"tuple"
    [1,2,3]:"List" #Mutable 
    {"Name":"Manish}:"Hello" #Cant use 
    
    
}


'''
'''



'''
