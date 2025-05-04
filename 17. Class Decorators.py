def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Add the greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Zaeem")
print(p.name)        
print(p.greet())     