#1
"""
Иерархия классов 🛸
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих транспортные средства:



Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(LandVehicle, Vehicle))
print(issubclass(WaterVehicle, Vehicle))
print(issubclass(AirVehicle, Vehicle))
Sample Output 1:

True
True
True
Sample Input 2:

print(issubclass(Car, LandVehicle))
print(issubclass(Motocycle, LandVehicle))
print(issubclass(Bicycle, LandVehicle))
Sample Output 2:

True
True
True

"""

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass

class Motocycle(LandVehicle):
    pass

class Bicycle(LandVehicle):
    pass


class Propeller(AirVehicle):
    pass

class Jet(AirVehicle):
    pass


if __name__ == '__main__':
    print(issubclass(Car, LandVehicle))
    print(issubclass(Motocycle, LandVehicle))
    print(issubclass(Bicycle, LandVehicle))