'''
Files helps store data permanently

File Handling:
is a process of 
1.Creating files 
2.reading the files 
3.writing files 
4.updating files 
using python

why file handling?
data disappears after the program ends

with files:
1.store data perm
2.data sharing possible
3.reports/logs can be generated 

Types of files ???
Text Files:
1. .txt
2. .csv 
3. .py
4. .json
2.Binary Files:
1.Images
2.videos
3.pdf's

#Opening the files 
SYntax:

file = open("Filename","mode")

'''
#r- will tell to python that 
# line doesnt have any escaping characters
file = open(r"C:\Users\manis\OneDrive\Desktop\CRT-PROGRAM CITY\File Handling\data.txt","r")
print(file)

'''
File Modes

Mode       Meaning 
r          Read
w          write
a          append
x          create
r+         read+write
w+         write+read
a+         append+read
rb         read binary
wb         write binary 
'''
try:
    file = open(r"C:\Users\manis\OneDrive\Desktop\CRT-PROGRAM CITY\File Handling\data.txt","r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError as e:
    print("No file found",e)  

#write mode - w 
file = open(r"C:\Users\manis\OneDrive\Desktop\CRT-PROGRAM CITY\File Handling\data.txt","w")
file.write("Hello students")
file.close()

#Creates file if not exist 
#deletes the old and add new content  

#append - mode: adds the data at end 
file = open(r"C:\Users\manis\OneDrive\Desktop\CRT-PROGRAM CITY\File Handling\data.txt","a")
file.write("\nHow are you?")
file.close()

#create mode- x (Creating a new file only)
# file = open("newfile.txt","x")
#Gives FileExistsError if already available

#Read()
file = open("newfile.txt","r")
print(file.read())
file.close()
#readline()
file = open("newfile.txt","r")
print(file.readline())
file.close()
#3.readlines()-reads multiple lines 
file = open("newfile.txt","r")
lines = file.readlines()
print(lines)
file.close()

#readlines --> converts to list

#write() --> writes the data to file 
file = open("newfile.txt","w")
file.write("Manish\n")
file.write("Rahu\n")
file.close()

#writelines():writes list data
names = [
    "Rahul\n",
    "Anjali\n",
    "Rajesh"
]
file = open("newfiles.txt","w")
file.writelines(names)
file.close()

#Pointer methods:
# returns the current cursor position
#tell()
file = open("newfiles.txt",'r')
print(file.tell())
file.read(5)
print(file.tell())
file.close()

#seek(): Moves the cursor position
file = open("newfiles.txt","r")
file.seek(3)
print(file.read())
file.close()

#with open()

with open("newfiles.txt","r") as file:
    print(file.read())
#automatic closing 

#student record system 
name = input("Enter student name:")
marks = input("Enter marks")
with open("newfile.txt","a") as file:
    file.write(name +" "+ marks + "\n")
print("Record Saved")    

#list --employee details 
employees = [
    "Rahul 50000",
    "Anjali 60000",
    "Manish 10000"
]
with open("newfile.txt","w") as file:
    for emp in employees:
        file.write(emp + "\n")
print("Report Generated")   

'''
CSV -->Comma Separated Values 
used:excel,reports,databases

Example:
name,age,branch
manish,21,ds
rahul,22,cse
'''
import csv 
with open(
    "students.csv","w",newline=""
    )as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Rahul",23,"CSE"])
    writer.writerow(["Sravani",24,"CSE"])
    
#Read CSV 
with open("students.csv","r") as file:
    reader = csv.reader(file) 
    for row in reader:
        print(row)  
     
#binary file handling 
file = open(r"C:\Users\manis\OneDrive\Desktop\CRT-PROGRAM CITY\cat.jpeg","rb")
data = file.read()
print(data)
file.close()

'''
Task1:count words in a file
with open("data.txt","r") as file:
     content = file.read()
     words = len(content.split())
     print(words)
     
Task:2 Count the lines in a file
lines = len(file.readlines()) 
print(lines)  

Task:3 search a word in a file 
word = input("Enter the word")
with open("data.txt","r") as file:
     content = file.read() 
     if word in content:
        print("word Found")
     else:
        print(No word)   
Task 4:Copy one file to another    
     
     
     with open("first.txt:","r)as file
        
'''
with open("first.txt","r")as file1:
    content=file1.read()
with open("second.txt","w")as file2:
    file2.write(content)
print("file copied successfully") 


'''
Task:Count characters in a file
with open("new.txt","r") as file:
    count=file.read()
    character = len(count)
    print(character)




'''
       