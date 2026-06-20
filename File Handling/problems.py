'''
Student Record Management:
A college wants to maintain student 
records permanently 
write a python program to 
1.accept student_name and marks 
2.store records in a file
named students.txt
3.display all records 
4.handle file exceptions properly
'''
class StudentManager:
    def add_student(self):
        try:
            name = input("Name:")
            marks = input("Marks:")
            with open("students.txt","a") as file:
                file.write(name + " "+ marks)
            print("Records added")
            
        except Exception as e:
            print(e) 
    def display_records(self): 
        try:
            with open("students.txt","r") as file:
                content = file.read()
                print("Students Records:")
                print(content)   
        except FileNotFoundError as e:
            print(e)               
obj = StudentManager()
obj.add_student()
obj.display_records()