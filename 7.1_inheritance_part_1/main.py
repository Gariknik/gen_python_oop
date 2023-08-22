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



#2
"""

Иерархия классов 🔶
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры:

"""
class Shape:
    pass

class Polygon(Shape):
    pass

class Circle(Shape):
    pass

class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass

class Parallelogram(Quadrilateral):
    pass

class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass

class Rectangle(Quadrilateral):
    pass

class Square(Rectangle):
    pass

#3
"""
Иерархия классов 🐍
С помощью наследования и приведенной ниже схемы постройте иерархию классов, описывающих животных:



Класс Animal должен иметь два метода экземпляра:

sleep() — пустой метод
eat()— пустой метод
Класс Fish должен иметь один метод экземпляра:

swim()— пустой метод
Класс Bird должен иметь один метод экземпляра:

lay_eggs()— пустой метод
Класс FlyingBird должен иметь один метод экземпляра:

fly()— пустой метод
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

print(issubclass(Fish, Animal))
print(issubclass(Bird, Animal))
print(issubclass(FlyingBird, Animal))
print(issubclass(FlyingBird, Bird))
Sample Output:

True
True
True
True


"""
class Animal:
    def __init__(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

class Fish(Animal):
    def swim(self):
        pass

class Bird(Animal):
    def lay_eggs(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass


if __name__ == '__main__':
    print(issubclass(Car, LandVehicle))
    print(issubclass(Motocycle, LandVehicle))
    print(issubclass(Bicycle, LandVehicle))


    print(issubclass(Triangle, Polygon))
    print(issubclass(IsoscelesTriangle, Triangle))
    print(issubclass(EquilateralTriangle, Triangle))


    print(issubclass(Fish, Animal))
    print(issubclass(Bird, Animal))
    print(issubclass(FlyingBird, Animal))
    print(issubclass(FlyingBird, Bird))