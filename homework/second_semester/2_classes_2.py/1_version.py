import random

class Car:
    def __init__(self, name, speed:int):
        self.name = name
        self.speed = speed

class Races:
    def race(car_list, laps):
        result = []
        result = sorted(car_list, reverse=True, key=lambda x: x.speed)
        for i in range(laps):
            droped_out = result.pop(random.randint(0, len(result) - i - 1))
            print(droped_out.name, 'попал в аварию!')
            result.append(droped_out)
        return result

car1 = Car('Fast', 200)
car2 = Car('Slow', 100)
car3 = Car('Middle', 150)
car_list = [car1, car2, car3]

print(*[i.name for i in Races.race(car_list, 1)])