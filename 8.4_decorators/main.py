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
"""
Декоратор @type_check
Реализуйте класс декоратор @type_check, который принимает один аргумент:

types — список, элементами которого являются типы данных
Декоратор должен проверять, что типы всех позиционных аргументов, передаваемых в декорируемую функцию, полностью сопоставляются с типами из списка types, то есть типом первого аргумента является первый элемент списка types, типом второго аргумента — второй элемент списка types, и так далее. Если данное условие не выполняется, должно быть возбуждено исключение TypeError.

Если количество позиционных аргументов больше, чем количество элементов в списке types, то не сопоставляемые аргументы не должны учитываться при проверке. Если количество позиционных аргументов меньше чем количество элементов в списке types, то не сопоставляемые типы из списка types не должны учитываться при проверке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @type_check, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))
Sample Output 1:

3
Sample Input 2:

@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))
Sample Output 2:

<class 'TypeError'>
Sample Input 3:

@type_check([int, int, str, list])
def add(a, b):
    '''sum a and b'''
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))
Sample Output 3:

add
sum a and b
3
Sample Input 4:

@type_check([int, int])
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3.0))
Sample Output 4:

6.0
"""

import functools

class type_check:
    def __init__(self, types):
        self.types = types
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(el) == t for el, t in zip(args, self.types)]):
                return func(*args, **kwargs)
            raise TypeError
        return wrapper
        

"""
Декоратор @track_instances
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.

Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в котором они были созданы.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


obj1 = Person('object 1')
obj2 = Person('object 2')

print(Person.instances)
Sample Output:

[Person('object 1'), Person('object 2')]

"""

import functools

def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def wrapper(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances += [self]
    cls.__init__ = wrapper
    return cls


"""
Декоратор @add_attr_to_class
Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса, является объектом типа mappingproxy, а не dict.

Приведенный ниже код:

class MyClass:
    pass


print(type(MyClass.__dict__))
выводит:

<class 'mappingproxy'>
Тип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством методов, а главное — отсутствием магического метода __setitem__(). Это значит, в объект типа mappingproxy нельзя напрямую добавить новую пару ключ-значение, а также изменить значение имеющегося ключа.

Приведенный ниже код:

class MyClass:
    pass


MyClass.__dict__['__doc__'] = 'docstring'
приводит к возбуждению исключения:

TypeError: 'mappingproxy' object does not support item assignment
Для добавления классу необходимого атрибута можно использовать функцию setattr().

Приведенный ниже код:

class MyClass:
    pass


setattr(MyClass, '__doc__', 'docstring')

print(MyClass.__doc__)
выводит:

docstring
Реализуйте декоратор @add_attr_to_class для декорирования класса. Декоратор должен принимать произвольное количество именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)
Sample Output:

1
2

"""


def add_attr_to_class(**kwargs):
    def decorator(cls):
        for key, value in kwargs.items():
            setattr(cls, key, value)
        return cls
    return decorator


"""
Декоратор @jsonattr
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')

@jsonattr('test.json')
class MyClass:
    pass
    
print(MyClass.x)
print(MyClass.y)
Sample Output:

1
2

"""
import json

def jsonattr(file_name):
    def decorator(cls):
        with open(file_name) as file:
            data = json.load(file)
            for key, value in data.items():
                setattr(cls, key, value)
        return cls
    return decorator


"""
Декоратор @singleton
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.

Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

@singleton
class MyClass:
    pass
    
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)
Sample Output:

True

"""
import functools

def singleton(cls):
    cls.instance = None
    old_new = cls.__new__

    @functools.wraps(old_new)
    def wrapper(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = old_new(cls)
        return cls.instance

    cls.__new__ = wrapper
    return cls
    

"""
Декоратор @snake_case
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и Lower Camel Case на Snake case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и Lower Camel Case на Snake case, если False — остаться прежним.

Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, LowerCamelCase или Snake Case.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1
    
    def superSecondMethod(self):
        return 2

obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())
Sample Output 1:

1
2
Sample Input 2:

@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)
Sample Output 2:

1
2
Sample Input 3:

@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())
Sample Output 3:

1
1

"""
import functools


def snake_case(attrs=False):
    def decorator(cls):
        print(cls.__dict__)
        dct = tuple(cls.__dict__.items())
        for key, value in dct:
            new_key = ''
            if not key.startswith('_'):
                delattr(cls, key)
                print(callable(key))
                if attrs and not callable(key):
                    for i in range(len(key)):
                        new_key += f'_{key[i].lower()}' if key[i].isupper() else key[i]
                else:
                    for i in range(len(key)):
                        new_key += f'_{key[i].lower()}' if key[i].isupper() else key[i]
            new_key = new_key.strip('_')
            setattr(cls, new_key, value)
        return cls
    return decorator


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

    @type_check([int, int])
    def add(a, b, c):
        return a + b + c

    print(add(1, 2, 3.0))

    @track_instances
    class Person:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'Person({self.name!r})'


    obj1 = Person('object 1')
    obj2 = Person('object 2')

    print(Person.instances)


    @add_attr_to_class(first_attr=1, second_attr=2)
    class MyClass:
        pass

    print(MyClass.first_attr)
    print(MyClass.second_attr)


    @singleton
    class MyClass:
        pass
        
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 is obj2)


    @snake_case()
    class MyClass:
        FirstAttr = 1

        def FirstMethod(self):
            return 1


    obj = MyClass()


    print(obj.first_method())