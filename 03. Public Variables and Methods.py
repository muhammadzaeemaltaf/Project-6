class Treasure:
    # Public variable
    hiddenPlace = "Under the tree"
    
    # Public method
    def tell(self):
        print(f"I hide treasure {self.hiddenPlace}")

# Access Public method
man = Treasure()
man.tell()


# Accessing the public variable
print("Position:", Treasure.hiddenPlace)