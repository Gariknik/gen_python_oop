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
class User:
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False

class PremiumUser(User):
    def skip_ads(self):
        return True

#5
"""

Классы Validator и NumberValidator
Реализуйте класс Validator, описывающий объект, проверяющий значение на корректность. При создании экземпляра класс должен принимать один аргумент:

obj — произвольный объект
Класс Validator должен иметь один метод экземпляра:

is_valid() — пустой метод, всегда возвращающий значение None
Также реализуйте класс NumberValidator, наследника класса Validator, описывающий объект, проверяющий значение на принадлежность типу int или float. Процесс создания экземпляра класса NumberValidator должен совпадать с процессом создания экземпляра класса Validator.

Класс NumberValidator должен иметь один метод экземпляра:

is_valid() — метод, возвращающий True, если значение переданное в инициализатор принадлежит типу int или float, или False в противном случае
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(NumberValidator, Validator))
Sample Output 1:

True
Sample Input 2:

validator1 = Validator('beegeek')
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())
Sample Output 2:

None
None
None
Sample Input 3:

validator1 = NumberValidator('beegeek')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())
Sample Output 3:

False
True
True

"""

class Validator:
    def __init__(self, obj):
        self.obj = obj
    
    def is_valid(self):
        pass

class NumberValidator(Validator):
    def is_valid(self):
        return type(self.obj) in (int, float)
    

#6
"""

Класс Counter и подклассы
1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен принимать один аргумент:

start — начальное значение счетчика, по умолчанию равняется 0
Экземпляр класса Counter должен иметь один атрибут:

value — текущее значение счетчика
Класс Counter должен иметь два метода экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод должен увеличить значение счетчика на единицу
dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число не передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным
2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать, но нельзя уменьшать. Процесс создания экземпляра класса NonDecCounter должен совпадать с процессом создания экземпляра класса Counter.

Экземпляр класса NonDecCounter должен иметь один атрибут:

value — текущее значение счетчика
Класс NonDecCounter должен иметь один метод экземпляра:

dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counter
3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение которого можно увеличивать лишь до определенного числа. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

start — начальное значение счетчика, по умолчанию равняется 0
limit — максимально возможное значение счетчика, по умолчанию равняется 10
Экземпляр класса LimitedCounter должен иметь один атрибут:

value — текущее значение счетчика
Класс LimitedCounter должен иметь один метод экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения счетчика метод не должен превышать установленный лимит
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))
Sample Output 1:

True
True
Sample Input 2:

counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)
Sample Output 2:

0
6
2
0
Sample Input 3:

counter = NonDecCounter(10)

print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)
Sample Output 3:

10
21
21
21
Sample Input 4:

counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
Sample Output 4:

0
5
2
10

"""
class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = start

    def inc(self, num=None):
        if num is None:
            self.value += 1
        else:
            self.value += num

    def dec(self, num=None):
        if num is None and self.value > 0:
            self.value -= 1
        elif num and self.value - num >= 0:
            self.value -= num
        else:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, num=None):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.start = start
        self.limit = limit
        self.value = start

    def inc(self, num=None):
        if num is None and self.value + 1 < self.limit:
            self.value += 1
        elif self.value + num < self.limit:
            self.value += num
        else:
            self.value = self.limit


"""

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class NonDecCounter(Counter):
    def dec(self, n=1):
        return None


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, n=1):
        self.value = min(self.value + n, self.limit)


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


    user = User('Arthur')
    premium_user = PremiumUser('Arthur')

    print(user.skip_ads())
    print(premium_user.skip_ads())


    validator1 = NumberValidator('beegeek')
    validator2 = NumberValidator(1)
    validator3 = NumberValidator(1.1)

    print(validator1.is_valid())
    print(validator2.is_valid())
    print(validator3.is_valid())


    print(issubclass(NonDecCounter, Counter))
    print(issubclass(LimitedCounter, Counter))

    counter = Counter()

    print(counter.value)
    counter.inc()
    counter.inc(5)
    print(counter.value)
    counter.dec()
    counter.dec(3)
    print(counter.value)
    counter.dec(10)
    print(counter.value)