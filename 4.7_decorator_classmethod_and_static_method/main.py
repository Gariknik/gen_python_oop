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

# 5
"""

Класс StrExtension
Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен принимать никаких аргументов.

Класс StrExtension должен иметь три статических метода:

remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
Sample Output 1:

Pthn
Stpk
Sample Input 2:

print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
Sample Output 2:

Python
Stepik
Sample Input 3:

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
Sample Output 3:

-y-ho-
S#epi#

"""
import re
class StrExtension:
    PATTERN_V = r'[aeiouyAEIOUY]'
    PATTERN_A = r'[^a-zA-Z]'
    @staticmethod
    def remove_vowels(string: str) -> str:
        new_string = re.sub(StrExtension.PATTERN_V, '', string)
        return new_string

    @staticmethod
    def leave_alpha(string: str) -> str:
        new_string = re.sub(StrExtension.PATTERN_A, '', string)
        return new_string

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        PATTERN = h = re.compile(fr'[{chars}]')
        new_string = re.sub(PATTERN, char, string)
        return new_string


# 6
"""

Класс CaseHelper 🌶️
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
Sample Output 1:

True
True
False
False
Sample Input 2:

print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))
Sample Output 2:

False
False
True
True
Sample Input 3:

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
Sample Output 3:

beegeek
bee_geek
Sample Input 4:

print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
Sample Output 4:

Beegeek
BeeGeek

"""
import re
class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
        return all(l.islower() or l == '_' for l in string) and ('_' != string[0] or '_' != string[-1] or '__' not in string)

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        return string[0].isupper() and '_' not in string

    @staticmethod
    def to_snake(string: str) -> str:
        func = lambda x: f'_{x.group().lower()}'
        if CaseHelper.is_upper_camel(string):
            return re.sub(r'[A-Z]', func, string)[1:]
        return string

    @staticmethod
    def to_upper_camel(string: str) -> str:
        func = lambda x: f'{x.group().upper()}'[-1]
        if CaseHelper.is_snake(string):
            return re.sub(r'(?:^[a-z]|_[a-z])', func, string)
        return string



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

    print(StrExtension.replace_all('Python', 'Ptn', '-'))
    print(StrExtension.replace_all('Stepik', 'stk', '#'))
    print(StrExtension.leave_alpha('Python111'))
    print(StrExtension.leave_alpha('__Stepik__()'))
    print(StrExtension.remove_vowels('Python'))
    print(StrExtension.remove_vowels('Stepik'))

    print(CaseHelper.to_snake('Beegeek'))
    print(CaseHelper.to_snake('BeeGeek'))

    print(CaseHelper.to_upper_camel('beegeek'))
    print(CaseHelper.to_upper_camel('bee_geek'))