class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return '{} {} {}'.format(self.make, self.model, self.year)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        Vehicle.__init__(self, make, model, year)
        self.num_doors = num_doors

    def honk(self):
        print("Honk! Honk! From Car")

    def get_info(self):
        return '{} {} {} {}'.format(self.make, self.model, self.year, self.num_doors)

class Motorcycle(Vehicle):

    def __init__(self, make, model, year, type):
        Vehicle.__init__(self, make, model, year)
        self.type = type

    def honk(self):
        print("Honk! Honk! From Motorcycle")

    def get_info(self):
        return '{} {} {} {}'.format(self.make, self.model, self.year, self.type)

class Truck(Vehicle):

    def __init__(self, make, model, year, capacity):
        Vehicle.__init__(self, make, model, year)
        self.capacity = capacity

    def honk(self):
        print("Honk! Honk! From Truck")

    def get_info(self):
        return '{} {} {} {}'.format(self.make, self.model, self.year, self.capacity)

    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        else:
            return False

class PickupTruck (Car, Truck):

    def __init__(self, make, model, year, capacity, num_doors, has_cover):
        Car.__init__(self, make, model, year, num_doors)
        Truck.__init__(self, make, model, year, capacity)
        self.has_cover = has_cover

    def get_info(self):
        return '{} {} {} {} {} {}'.format(self.make, self.model, self.year, self.capacity, self.num_doors, self.has_cover)




vehicle1 = Car('Honda','Accord', 2023, 4)
vehicle2 = Motorcycle('Honda', 'Fury', 2022, 'cruiser')
vehicle3 = Truck('Toyota', 'Tundra', 2021, 100)
vehicle4 = PickupTruck('Toyota', 'Tacoma', 2020, 70, 4, True)

vehicle1.honk()
vehicle2.honk()
vehicle3.honk()
vehicle4.honk()
print()
print(vehicle1.get_info())
print(vehicle2.get_info())
print(vehicle3.get_info())
print(vehicle4.get_info())
print()
print("Is the Truck capcity at {} smaller than the Pickup Truck capacity at {}".format(vehicle3.capacity, vehicle4.capacity))
print(vehicle3 < vehicle4)