class A:
    def show(self):
        print("This is from class A")

class B(A):
    def show(self):
        print("This is from class B")


class C(A):
    def show(self):
        print("This is from class C")

class D(B, C):
    pass

d = D()
d.show()  # This will call the show method from class B due to MRO (Method Resolution Order)



