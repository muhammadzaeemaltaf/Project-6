class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  
    def start_car(self):
        self.engine.start()  


my_engine = Engine()          # Create an Engine object
my_car = Car(my_engine)       # Pass Engine into Car (composition)

my_car.start_car()            # Starts the engine via the Car class
