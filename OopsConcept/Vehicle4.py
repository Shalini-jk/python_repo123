 # Determine if School_bus is also an instance of the Vehicle class

class Vehicle4:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle4):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle4))