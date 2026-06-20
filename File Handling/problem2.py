'''
A company wants to generate employee
salary reports 
write a program to:
1.Accept employee details 
2.store them in employee.txt
3.calculate total salary expenditure 
(total =0 +salary)
4.display employee report 
Sample INput:
Enter the emp name:Manish
Enter the salary:50000

output:
Employee Report 
Manish 50000
Total Expenditure:50000
'''
class EmployeeReport:
    def add_employee(self):
        try:
            name = input("Enter the name:")
            salary = float(input("Enter the salary:"))
            with open("employee.txt","a") as file:
                file.write(name + " " +str(salary)+"\n")
            print("Employee added") 
        except ValueError as e:
            print("Invalid input",e)      
    def generate_report(self):
        total = 0
        try:
            with open("employee.txt","r") as file:
                for line in file:
                    name,salary = line.split() 
                    print(name,salary)  
                    total +=float(salary) 
            print("Total Expenditure:",total)  
        except FileNotFoundError:
            print("EMployee File misssing") 
obj = EmployeeReport()
obj.add_employee()
obj.generate_report()                       