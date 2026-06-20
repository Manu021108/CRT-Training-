'''
key:values -->Mutable
 |
 Immutable

student_marks={
    "John":85,
    "alice":98,
    "bob":78
}



'''
student_marks={
    "john":85,
    "alice":98,
    "bob":78
}

print(student_marks.items())
'''
dict_items(
    [('John', 85),
    ('alice', 98),
    ('bob', 78)])
    
    collection of tuples inside the list 
Now each item is a tuple
t = (key,value)
      0    1
      
Dict themselves cannot be 
sorted 

# list = [1,2,3,4]
# sort(list)
students = list(student_marks.items())
      
'''
students = list(student_marks.items())
students.sort()
print(students)

students = list(student_marks.items())
def sort_by_marks(item):
    #tuple - John,85
     #        0    1
    return item[1]
students.sort(key=sort_by_marks,reverse=True)
print(students)

'''
#Problem perspective 
count ={
    "john":2,
    "alice":2,
    "bob":1
}
print(count.items())




'''
count ={
    "john":2,
    "alice":2,
    "bob":1
}
print(count.items())
'''
dict_items(
    [
    ('john', 2), 
    ('alice', 2), 
    ('bob', 1)
    ]
    )




'''
employees = list(count.items())
employees.sort()
print(employees)

def sort_by_work(item):
    return item[1]
employees.sort(key= sort_by_work,reverse=True)
print(employees)











