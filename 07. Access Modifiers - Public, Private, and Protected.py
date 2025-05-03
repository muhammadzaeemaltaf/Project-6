class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public Variable
        self._salary = salary # Protected Variable
        self.__ssn = ssn # Private variable 

        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable
print("Public Name: ", emp.name)

# Accessing protected variable (possible, but not recommended)
print("Protected Salary:", emp._salary)

# Access private variable using name mangling
print("Private SSN (via name mangling):", emp._Employee__ssn)