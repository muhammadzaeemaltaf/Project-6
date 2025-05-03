class Student:
    def __init__(self, name, className):
        self.name = name
        self.className = className
    
    def display(self):
        print(f"{self.name} is student of class {self.className}")

person = Student("Zaeem", "10th")
person.display()