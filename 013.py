# Write a program to create class name Employee and display employee name,Date of join ,designation,salary with the help of object.

class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary
    
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary}")

employee = Employee("Het Agravat", "2024-08-06", "CEO", 100000)

employee.display_details()
