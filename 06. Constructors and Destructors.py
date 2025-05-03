class Logger:
    def __init__(self):
        print(f"Constructor call because instance created from class")

    def __del__(self):
        print(f"Destructor call because instance deleted")


log1 = Logger()  # Constructor will be called here when the object is created

# Optional because Python uses GC (Garbage Collector) and cleans it up itself
del log1  # Explicitly deleting the object to trigger the destructor
