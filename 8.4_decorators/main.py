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

"""
Декоратор @returns
Реализуйте класс декоратор @returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое значение принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError.

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @returns, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@returns(int)
def add(a, b):
    return a + b

print(add(1, 2))
Sample Output 1:

3
Sample Input 2:

@returns(int)
def add(a, b):
    return a + b

try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))
Sample Output 2:

<class 'TypeError'>

"""
import functools
class returns:
    def __init__(self, datatype) -> None:
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            all = func(*args, **kwargs)
            if self.datatype != type(all):
                raise TypeError
            return all
        return wrapper


"""
Декоратор @exception_decorator
Реализуйте класс декоратор @exception_decorator, который возвращает

кортеж (value, None), если декорируемая функция завершила свою работу без возбуждения исключения, где value — возвращаемое значение декорируемой функции
кортеж (None, errortype), если во время выполнения декорируемой функции было возбуждено исключение, где errortype — тип возбужденного исключения
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @exception_decorator, но не код, вызывающий его. 

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@exception_decorator
def func(x):
    return 2*x + 1
    
print(func(1))
print(func('bee'))
Sample Output 1:

(3, None)
(None, <class 'TypeError'>)
Sample Input 2:

@exception_decorator
def f(x, y):
    return x * y
    
print(f('stepik', 10))
Sample Output 2:

('stepikstepikstepikstepikstepikstepikstepikstepikstepikstepik', None)

"""
import functools

class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.predicat(self.func, *args, **kwargs)
    
    @staticmethod
    def predicat(func, *args, **kwargs):
        try:
            return (func(*args, **kwargs), None)
        except Exception as e:
            return (None, type(e))
        
        
"""
Декоратор @ignore_exception
Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:

Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @ignore_exception, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x
    
func(0)
Sample Output 1:

Исключение ZeroDivisionError обработано
Sample Input 2:

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))
Sample Output 2:

<class 'TypeError'>

"""

import functools

class ignore_exception:
    def __init__(self, *args, **kwargs):
        self.exceptions = (*args, *kwargs.values())
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')
        return wrapper

        


if __name__ == '__main__':
    @takes_numbers
    def mul(a, b):
        return a * b
        
    print(mul(1, 2))
    print(mul(1, 2.5))
    print(mul(1.5, 2))
    print(mul(1.5, 2.5))

    @returns(list)
    def beegeek():
        '''beegeek docs'''
        return 'beegeek'

    print(beegeek.__name__)
    print(beegeek.__doc__)

    try:
        print(beegeek())
    except TypeError as e:
        print(type(e))


    @exception_decorator
    def func(x):
        return 2*x + 1
        
    print(func(1))
    print(func('bee'))

    @ignore_exception(ZeroDivisionError, TypeError, ValueError)
    def func(x):
        return 1 / x
        
    func(0)