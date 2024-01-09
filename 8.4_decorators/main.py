"""
Декоратор @reverse_args
Вам доступен декоратор @reverse_args, который передает все позиционные аргументы в декорируемую функцию в обратном порядке. Реализуйте декоратор @reverse_args в виде класса декоратора.

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @reverse_args, но не код, вызывающий его.﻿

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))
Sample Output 1:

9
Sample Input 2:

@reverse_args
def concat(a, b, c):
    return a + b + c
    
print(concat('apple', 'cherry', 'melon'))
Sample Output 2:

meloncherryapple

"""
import functools
from typing import Any

class reverse_args:
    def __init__(self, func: object) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args[::-1], **kwargs)

"""
Декоратор @limited_calls
Реализуйте класс декоратор @limited_calls, который принимает один аргумент:

n — целое число
Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз, должно быть возбуждено исключение MaxCallsException с текстом:

Превышено допустимое количество вызовов
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @limited_calls, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

@limited_calls(3)
def add(a, b):
    return a + b
    
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)
Sample Output:

3
7
11
Превышено допустимое количество вызовов

"""
import functools

class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n) -> None:
        self.n = n
        self.count = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.count += 1
            if self.count > self.n:
                raise MaxCallsException ('Превышено допустимое количество вызовов')
            return func(*args, **kwargs)
        return wrapper
    

"""
Декоратор @takes_numbers
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

Аргументы должны принадлежать типам int или float
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@takes_numbers
def mul(a, b):
    return a * b
    
print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))
Sample Output 1:

2
2.5
3.0
3.75
Sample Input 2:

@takes_numbers
def mul(a, b):
    return a * b
    
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
Sample Output 2:

Аргументы должны принадлежать типам int или float

"""
import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if not all([type(el) in (int, float) for el in list(args) + list(kwargs.values())]):
            raise TypeError ("Аргументы должны принадлежать типам int или float")
        return self.func(*args, **kwargs)





if __name__ == '__main__':
    @takes_numbers
    def mul(a, b):
        return a * b
        
    print(mul(1, 2))
    print(mul(1, 2.5))
    print(mul(1.5, 2))
    print(mul(1.5, 2.5))