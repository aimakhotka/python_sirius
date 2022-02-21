
import random

class Car:
    def __init__(self, name, speed:int):
        self.name = name
        self.speed = speed

class Races:
    def race(car_list, laps):
        droped_car = []
        result = sorted(car_list, reverse=True, key=lambda x: x.speed)
        lenght = len(car_list)
        if laps > lenght:
            laps = lenght
        for i in range(laps):
            droped_out = result.pop(random.randint(0, len(result)))
            print(droped_out.name, 'попал в аварию!')
            droped_car.append(droped_out)
        result += droped_car[::-1]
        return result

car1 = Car('Fast', 200)
car2 = Car('Slow', 100)
car3 = Car('Middle', 150)
car_list = [car1, car2, car3]

print(*[i.name for i in Races.race(car_list, 5)])