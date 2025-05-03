class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()

emp = Employee("Zaeem", 101)
dept = Department("HR", emp)
dept.show_department()