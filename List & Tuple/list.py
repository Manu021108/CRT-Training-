'''
What is a list?

list: collection of ordered elements 

                                   Mutability
                                   /       \
                                Mutable  Immutable
                                   |        |
                            can modify   cant modify 
                            
List is mutable:
Allow's duplicate---> yes list allows duplicate  
#dynamic in size.  

#Syntax: 

list_name = [elements]

#Stores heterogenous elements 
                         

'''
numbers = [10,20,30,40,10.4,]

print(type(numbers))


data = [10,10.4,"Python",True]

print(data)

#accessing the elements 

a = [10,20,30,40]
    # 0 1  2  3
    
print(a[0])
print(a[2])

#check the mutability 

a[0] = 60

print(a)

#negative indexing 

a = [10,20,30,40]
   # -4  -3 -2 -1

print(a[-1])
print(a[-2])
    
#Slicing :

# list[start:end:step]    

print(a[0:3])
print(a[:3])
print([a[::2]])

#List methods 

#append: 

b = [10,20]

b.append(30)

#extend: adds multiple elements 

b.extend([40,50,60])

print(b)

# insert ->adds the element at specific index

b.insert(2,20) 
print(b)

#remove -->removes the element 

b.remove(20)
print(b)

#pop -->removes the elements with index

b.pop(0)

#clear() --->deletes all elements

# b.clear()

#index() : returns the position

print(b.index(20))


#count():counts the occurances of the element 

print(b.count(20))

#reverse():

b.reverse()

#copy():creates the copy 

c = b.copy()
print(c)

#Sorting in list:

a = [5,0,2,4,3,1]

#sort() --->sorts in ascending order
a.sort()

print(a)

#Descending order:

a.sort(reverse=True)

print(a)

#sort vs sorted:creates a new list 

b = sorted(a)

print(b)

'''
Task: create a list with 5 bestfrnds 
1.add a new frnd just introduced 
2.Remove the 2 frnds just had a fight 
3.add 3 close frnds at a single time
4.sort the frnds in alphabetical order 
5.delete the frnd at index 5
6.copy the frnds list in a new list 
7.then perform clear on previous list 

'''

#Nested list ?

a = [[1,2,3],[4,5,6]]
    #    0        1

print(a[0][0])
print(a[1][1])

#Iterating over the list 

a = [10,20,30,40]

for i in a:
    print(i)

#Range()

for i in range(len(a)):
    print(a[i])
    
    
#List comprehension: 

# [expression for variable in iterable]   

#Example:

squares = [x*x for x in range(1,6)] 

print(squares)

'''
Tuple: Collection of ordered elements 
#Immutable: 
#Tuple: more faster then list 
#Allow duplicates 

t = (1,2,3)

feature  list  tuple

Mutable     yes   NO
duplicates  yes   yes 
ordered     yes   yes 
performance slow  fast 
synatx       []     ()

#Indexing:

t = (1,2,3,4)
     0 1 2 3
     
t[0]     



'''
t = (1,2,3,3.12)
print(t)

print(t[0])

#check the mutability 

# t[0] = 9

#Tuple pack and unpack 

#packing 

t = (10,20,30)

#unpacking 

a,b,c = t

print(a)
print(b)
print(c)

#tuple methods 

t.count(10)

t.index(20)

'''
why use tuple?  --> fixed data 
list: dynamic data 

can tuple consist of a list ?

what is the diff between append and extend?

append: indvidual element 
extend: multiple elements 

#diff btw list and tuple

#sort vs sorted 



'''
t = ([1,2,3],10,3.14)

t[0].append(20)


a = [1,2,3]

a.append([4,5,6])

print(a)

