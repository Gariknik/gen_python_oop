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


#4
"""

Классы User и PremiumUser
Реализуйте класс User, описывающий пользователя некоторого интернет-ресурса. При создании экземпляра класс должен принимать один аргумент:

name — имя пользователя
Класс User должен иметь один метод экземпляра:

skip_ads() — метод, всегда возвращающий False 
Также реализуйте класс PremiumUser, наследника класса User, описывающий пользователя некоторого интернет-ресурса с премиум подпиской. Процесс создания экземпляра класса PremiumUser должен совпадать с процессом создания экземпляра класса User.

Класс PremiumUser должен иметь один метод экземпляра:

skip_ads() — метод, всегда возвращающий True 
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(PremiumUser, User))
Sample Output 1:

True
Sample Input 2:

user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())
Sample Output 2:

False
True


"""


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