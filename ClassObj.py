# oops

# 1. Class and Object
# 2. Polymorphism
# 3. Inheritence
# 4. Encapsulation
# 5. Abstraction


class Car:

    def __init__(self, r1, r2):
        self.r1 = r1  # member variable
        self.r2 = r2

    def sayHello(self):  # Data variables
        return "Hello Car"

    def sayCarName(self, carName):
        return carName

    def sayCarVariant(self, carVariant):
        return carVariant


class Truck:

    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def sayHello(self):
        return "Hello from Truck"

    def sayTruckName(self, truckName):
        return truckName

    def sayTruckVariant(self, truckVariant):
        return truckVariant


class Honda(Truck, Car):

    def __init__(self):
        print("Honda Car")


h1 = Honda()

print(h1.sayHello())
