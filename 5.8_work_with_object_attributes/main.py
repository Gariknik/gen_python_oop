#1
"""

Класс Item
Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:

name — название предмета
price — цена предмета в рублях
quantity — количество предметов
Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)
Sample Output 1:

15
5
Sample Input 2:

fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)
Sample Output 2:

Banana
75
Sample Input 3:

course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)
Sample Output 3:

Pygen
3900
2
7800

"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, attr):
        if attr == 'name':
            return object.__getattribute__(self, attr).title()
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        if attr == 'total': 
            return self.quantity * self.price
        
#2
"""

Класс Logger
Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать никаких аргументов.

Предполагалось, что при установке или изменении значения атрибута экземпляра класса Logger будет выводиться текст:

Изменение значения атрибута <имя атрибута> на <новое значение атрибута>
Также планировалось, что при удалении атрибута будет выводиться текст:

Удаление атрибута <имя атрибута>
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Logger.

Примечание. Никаких ограничений касательно реализации класса Logger нет, она может быть произвольной.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

obj = Logger()

obj.attr = 1
del obj.attr
Sample Output 1:

Изменение значения атрибута attr на 1
Удаление атрибута attr
Sample Input 2:

obj = Logger()

obj.name = 'pygen'
obj.rating = '5*'
obj.ceo = 'Timur'
del obj.rating
obj.rating = '6*'
Sample Output 2:

Изменение значения атрибута name на pygen
Изменение значения атрибута rating на 5*
Изменение значения атрибута ceo на Timur
Удаление атрибута rating
Изменение значения атрибута rating на 6*

"""

class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        object.__delattr__(self, name)



#3
"""

Класс Ord
Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Ord должен выступать в качестве альтернативы функции ord(). При обращении к атрибуту экземпляра, именем которого является одиночный символ, должна возвращаться его позиция в таблице символов Unicode.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Ord нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

obj = Ord()

print(obj.a)
print(obj.b)
Sample Output 1:

97
98
Sample Input 2:

obj = Ord()

print(obj.в)
print(obj.г)
Sample Output 2:

1074
1075

"""

class Ord:
    def __getattr__(self, attr):
        return ord(attr)


#4
"""

Класс DefaultObject
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default, имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.

При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса DefaultObject нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)
Sample Output 1:

Ares
greek
None
Sample Input 2:

god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)
Sample Output 2:

Tyr
scandinavian
0

"""



class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattribute__(self, attr):
        return super().__getattribute__(attr)

    def __getattr__(self, attr):
        return self.default



 #5
"""
 
 Класс NonNegativeObject
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)
Sample Output 1:

1
2
0
black
Sample Input 2:

point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)
Sample Output 2:

1.5
2.3
0.0
yellow
 
"""   

class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if type(value) in (int, float) and value < 0:
            value = value * (-1)
        super().__setattr__(key, value)



if __name__ == '__main__':

    course = Item('pygen', 3900, 2)

    print(course.name)
    print(course.price)
    print(course.quantity)
    print(course.total)


    obj = Logger()

    obj.name = 'pygen'
    obj.rating = '5*'
    obj.ceo = 'Timur'
    del obj.rating
    obj.rating = '6*'

    obj = Ord()

    print(obj.a)
    print(obj.b)

    god = DefaultObject(name='Ares', mythology='greek')
    print(god.name)
    print(god.mythology)
    print(god.age)


    point = NonNegativeObject(x=1, y=-2, z=0, color='black')

    print(point.x)
    print(point.y)
    print(point.z)
    print(point.color)
