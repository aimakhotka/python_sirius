class Washing:
    def __init__(self, water):
        self.water = water

    def wash(self, item):
        print(f"I'm washing {item} with {self.water}l of water")

class Driving:
    def drive(a, b):
        print(f"I'm going from {a} to {b}")

class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color
    def about(brand, price, year, color):
        print(f"Machine's brand: {brand} \nMachine's price: {price} \nMachine's year: {year} \nMachine's color: {color}")


class Driving_Machine(Driving, Machine):
    pass

class Washing_Machine(Washing, Machine):
    pass

car1 = Driving_Machine
print(car1.drive('Moscow', 'Sochi'), car1.about('ferrari', '10000$', '1991', 'yellow'))

woman = Washing_Machine('10')
print(woman.wash('plates'), woman.about('0$', '30', 'white'))