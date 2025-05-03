class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person's name is {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # Using super() to call the Parent class constructor
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches {self.subject}")

# Create an object of Teacher class
teacher1 = Teacher("Ali", "Mathematics")