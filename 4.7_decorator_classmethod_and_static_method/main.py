# 1
"""

Класс Circle
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь один атрибут:

radius — радиус круга
Класс Circle должен иметь один метод класса:

from_diameter() — метод, принимающий в качестве аргумента диаметр круга и возвращающий экземпляр класса Circle, созданный на основе переданного диаметра
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

circle = Circle(5)

print(circle.radius)
Sample Output 1:

5
Sample Input 2:

circle = Circle.from_diameter(10)

print(circle.radius)
Sample Output 2:

5.0

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

# 2
"""

Класс Rectangle
Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:

length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь один метод класса:

square() — метод, принимающий в качестве аргумента число side и возвращающий экземпляр класса Rectangle c длиной и шириной, равными side
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
Sample Output 1:

4
5
Sample Input 2:

rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)
Sample Output 2:

5
5

"""
class Rectangle:
    def __init__(self, l: int|float, w: int|float):
        self.length = l
        self.width = w

    @classmethod
    def square(cls, side: int|float):
        return cls(side, side)



#3
"""

Класс QuadraticPolynomial
Квадратный трехчлен — это многочлен вида 
�
�
2
+
�
�
+
�
ax 
2
 +bx+c, где 
�
≠
0
a

=0. Например:
�
2
+
1
�
2
−
5
�
+
6
x 
2
 +1
x 
2
 −5x+6
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — коэффициент 
�
a квадратного трехчлена
b — коэффициент 
�
b квадратного трехчлена
c — коэффициент 
�
c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

a — коэффициент 
�
a квадратного трехчлена
b — коэффициент 
�
b квадратного трехчлена
c — коэффициент 
�
c квадратного трехчлена
Класс QuadraticPolynomial должен иметь два метода класса:

from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c, которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов
from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c квадратного трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float 
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)
Sample Output 1:

1
-5
6
Sample Input 2:

polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)
Sample Output 2:

2
13
-1
Sample Input 3:

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
Sample Output 3:

-1.5
4.0
14.8
17.3

"""

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        return cls(*map(float, string.split()))

#4
"""

Класс Pet
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:

name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:

name — имя домашнего животного
Класс Pet должен иметь три метода класса:

first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
Примечание 1. Никаких ограничений касательно реализации класса Pet нет, она может быть произвольной.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())
Sample Output 1:

None
None
0
Sample Input 2:

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
Sample Output 2:

Ratchet
Rivet
3

"""
class Pet:
    LIST_INSTANCE = []
    def __init__(self, name):
        self.name = name
        self.__class__.LIST_INSTANCE.append(self)

    @classmethod
    def first_pet(cls):
        if not cls.LIST_INSTANCE:
            return None
        return cls.LIST_INSTANCE[0]


    @classmethod
    def last_pet(cls):
        if not cls.LIST_INSTANCE:
            return None
        return cls.LIST_INSTANCE[-1]

    @classmethod
    def num_of_pets(cls):
        return len(cls.LIST_INSTANCE)




if __name__ == "__main__":
    circle = Circle(5)

    print(circle.radius)
    circle = Circle.from_diameter(10)

    print(circle.radius)

    rectangle = Rectangle(4, 5)

    print(rectangle.length)
    print(rectangle.width)

    rectangle = Rectangle.square(5)

    print(rectangle.length)
    print(rectangle.width)

    polynom = QuadraticPolynomial(1, -5, 6)

    print(polynom.a)
    print(polynom.b)
    print(polynom.c)

    polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

    print(polynom.a)
    print(polynom.b)
    print(polynom.c)

    polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

    print(polynom.a)
    print(polynom.b)
    print(polynom.c)
    print(polynom.a + polynom.b + polynom.c)

    print(Pet.first_pet())
    print(Pet.last_pet())
    print(Pet.num_of_pets())

    pet1 = Pet('Ratchet')
    pet2 = Pet('Clank')
    pet3 = Pet('Rivet')

    print(Pet.first_pet().name)
    print(Pet.last_pet().name)
    print(Pet.num_of_pets())
