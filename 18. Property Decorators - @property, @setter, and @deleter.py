class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price
    
    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


item = Product(100)

print(item.price)  
item.price = 150      
print(item.price)     
del item.price         
print(item.price) # This will raise an AttributeError     