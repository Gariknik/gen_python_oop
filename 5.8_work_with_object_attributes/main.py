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