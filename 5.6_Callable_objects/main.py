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