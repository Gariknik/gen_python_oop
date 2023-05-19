#1
"""

Класс Processor
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

Класс Processor имеет один статический метод:

process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.

Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.

Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))
Sample Output 1:

20
10.4
HELLO
(1, 2, 3, 4)
[1, 2, 3]
Sample Input 2:

try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
Sample Output 2:

Аргумент переданного типа не поддерживается

"""
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def num_process(data):
        return data * 2

    @process.register
    @staticmethod
    def str_process(data: str):
        return data.upper()

    @process.register
    @staticmethod
    def list_process(data: list):
        return sorted(data)

    @process.register
    @staticmethod
    def tuple_process(data: tuple):
        return tuple(sorted(data))


#2
"""

Класс Negator
Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Negator должен иметь один статический метод:

neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. Если методу передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Negator нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
Sample Output 1:

-11.0
12
False
True
Sample Input 2:

try:
    Negator.neg('number')
except TypeError as e:
    print(e)
Sample Output 2:

Аргумент переданного типа не поддерживается

"""
from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError ("Аргумент переданного типа не поддерживается")

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def num_neg(data):
        return data * (-1)

    @neg.register(bool)
    @staticmethod
    def num_neg(data):
        return not data


if __name__ == '__main__':
    print(Processor.process(10))
    print(Processor.process(5.2))
    print(Processor.process('hello'))
    print(Processor.process((4, 3, 2, 1)))
    print(Processor.process([3, 2, 1]))