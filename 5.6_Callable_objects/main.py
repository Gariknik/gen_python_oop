#1
"""

Класс Calculator
Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:

a — число
b — число
operation — один из символов +, -, * и /
Если operation равняется +, экземпляр класса Calculator должен вернуть сумму a и b, если - — разность a и b, если * — произведение a и b, если / — частное a и b. При попытке выполнить деление на ноль должно быть возбуждено исключение ValueError с текстом:

Деление на ноль невозможно
Примечание 1. Числами будет считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Calculator нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
Sample Output 1:

15
5
50
2.0
Sample Input 2:

calculator = Calculator()

try:
    print(calculator(10, 0, '/'))
except ValueError as e:
    print(e)
Sample Output 2:

Деление на ноль невозможно

"""

class Calculator:
    def __call__(self, a, b, oper):
        if oper == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{oper}{b}')


#2
"""

Класс RaiseTo
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень. При создании экземпляра класс должен принимать один аргумент:

degree — показатель степени
Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса RaiseTo должен возвращать значение x в степени degree.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RaiseTo нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

raise_to_two = RaiseTo(2)

print(raise_to_two(2))
print(raise_to_two(3))
print(raise_to_two(4))
Sample Output 1:

4
9
16
Sample Input 2:

raise_to_three = RaiseTo(3)
raise_to_four = RaiseTo(4)

print(raise_to_three(3))
print(raise_to_four(2))
Sample Output 2:

27
16

"""
class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree

#3
"""

Класс Dice
Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней. При создании экземпляра класс должен принимать один аргумент:

sides — количество граней игрального кубика
Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов. При вызове он должен возвращать значение случайной грани игрального кубика. Например, если кубик имеет 6 граней, экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6].

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Dice нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])
Sample Output:

True
True
False

"""
from random import randint
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)

#4
"""

 Класс QuadraticPolynomial
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
Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса QuadraticPolynomial должен возвращать значение выражения 
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
,
�
a,b и 
�
c — коэффициенты квадратного трехчлена.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

func = QuadraticPolynomial(1, 2, 1)

print(func(1))
print(func(2))
Sample Output 1:

4
9
Sample Input 2:

func = QuadraticPolynomial(1, 3, 4)

print(func(1))
print(func(2))
Sample Output 2:

8
14

"""

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

#5
"""

Класс Strip
Реализуйте класс Strip, экземпляры которого позволяют удалять из начала и конца строки определенные символы. При создании экземпляра класс должен принимать один аргумент:

chars — строка, в которой перечислены удаляемые символы
Экземпляр класса Strip должен являться вызываемым объектом и принимать один аргумент:

string — строка
Экземпляр класса Strip должен удалять из начала и конца строки string все символы, перечисленные в chars, и возвращать полученный результат.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Strip нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

strip = Strip('!? ')

print(strip('     ?beegeek!'))
print(strip('!bee?geek!'))
Sample Output 1:

beegeek
bee?geek
Sample Input 2:

strip = Strip('.,+-')

print(strip('     --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))
Sample Output 2:

     --++beegeek
bee...geek
b-e-e-g-e-e-k

"""

class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)

#6
"""

Класс Filter
Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов. При создании экземпляра класс должен принимать один аргумент:

predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение True.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Filter нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))
Sample Output 1:

[2, 4, 6]
Sample Input 2:

more_than_five = Filter(lambda x: x > 5)
numbers = [13, 1, 4, 10, 10, 7]

print(more_than_five(numbers))
Sample Output 2:

[13, 10, 10, 7]

"""
class Filter:
    def __init__(self, predicate):
        self.predicate = predicate
    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))

if __name__ == '__main__':
    calculator = Calculator()

    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '-'))
    print(calculator(10, 5, '*'))
    print(calculator(10, 5, '/'))

    raise_to_two = RaiseTo(2)

    print(raise_to_two(2))
    print(raise_to_two(3))
    print(raise_to_two(4))

    kingdice = Dice(6)

    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [7, 8, 9, 10])

    func = QuadraticPolynomial(1, 3, 4)

    print(func(1))
    print(func(2))

    strip = Strip('.,+-')

    print(strip('     --++beegeek++--'))
    print(strip('-bee...geek-'))
    print(strip('-+,.b-e-e-g-e-e-k-+,.'))

    leave_even = Filter(lambda x: x % 2 == 0)
    numbers = [1, 2, 3, 4, 5, 6]

    print(leave_even(numbers))