# 2. Write a program to perform single inheritance create main class company(name,city,mobile no)sub class employee(emp_name,designation,salary).

class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_details(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")

class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        super().__init__(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_details(self):
        self.display_company_details()
        print(f"Employee Name: {self.emp_name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary}")

employee = Employee("Microsoft", "Washington", "6355494350", "Het Agravat", "Software Engineer", 100000)

employee.display_employee_details()
