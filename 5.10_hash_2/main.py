#1
"""

Класс ColoredPoint
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
color — цвет точки
Класс ColoredPoint должен иметь три свойства:

x — свойство, доступное только для чтения, возвращающее координату точки по оси 
�
x
y — свойство, доступное только для чтения, возвращающее координату точки по оси 
�
y
color — свойство, доступное только для чтения, возвращающее цвет точки
Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.

Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение, вычисленное с помощью функции hash() на основе кортежа, первым элементом которого является координата точки по оси 
�
x, вторым — координата точки по оси 
�
y, третьим — цвет точки.

Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))
Sample Output 1:

True
True
False
False
Sample Input 2:

points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)
Sample Output 2:

{ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}
Sample Input 3:

point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')
Sample Output 3:

Error

"""
from typing import Any


class ColoredPoint:
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def color(self):
        return self.__color
    
    def __eq__(self, other) -> bool:
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.color))
    
#2
"""
Класс Row🌶️
Реализуйте класс Row, описывающий объект, содержащий произвольный набор атрибутов. При создании экземпляра класс должен принимать произвольное количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.

Класс Row должен запрещать устанавливать новые атрибуты своим экземплярам. Помимо этого класс должен запрещать изменять значения уже имеющихся атрибутов, а также удалять их. При попытке установить новый атрибут должно возбуждаться исключение AttributeError с текстом:

Установка нового атрибута невозможна
При попытке изменить значение уже имеющегося атрибута должно возбуждаться исключение AttributeError с текстом:

Изменение значения атрибута невозможно
При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:

Удаление атрибута невозможно
Экземпляр класса Row должен иметь следующее формальное строковое представление:

Row(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
Также экземпляры класса Row должны поддерживать между собой операции сравнения с помощью операторов == и!=. Два экземпляра класса Row считаются равными, если их наборы атрибутов полностью совпадают, то есть совпадает их количество, позиции, имена и соответствующие значения.

Наконец, при передаче экземпляра класса Row в функцию hash() должно возвращаться его хеш-значение. Алгоритм вычисления хеш-значения может быть произвольным, однако он должен учитывать все атрибуты экземпляра, их позиции, имена и соответствующие значения

Примечание 1. Гарантируется, что значениями атрибутов экземпляров класса Row являются хешируемые объекты.

Примечание 2. Обратите внимание, что в формальном строковом представлении значения атрибутов, которые принадлежат типу str, должны быть обрамлены апострофами.

Примечание 3. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса Row нет, она может быть произвольной.

Примечание 6. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)
Sample Output 1:

Row(a='A', b='B', c='C')
A B C
Sample Input 2:

row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))
Sample Output 2:

True
True
False
False
Sample Input 3:

row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)
Sample Output 3:

Установка нового атрибута невозможна


"""

class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __repr__(self):
        result = []
        for key, value in self.__dict__.items():
            result += [f"{key} = '{value}'"] if type(value) == str else [f"{key} = {value}"]
        return f"Row({', '.join(result)})"

    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            raise AttributeError ('Изменение значения атрибута невозможно')
        raise AttributeError ('Установка нового атрибута невозможна')
    
    def __delattr__(self, attr):
        raise AttributeError ('Удаление атрибута невозможно')
    
    def __eq__(self, other):
        if isinstance(other, Row):
            return repr(self) == repr(other)
        return NotImplemented
    
    def __hash__(self):
        return hash(repr(self))



if __name__ == '__main__':
    point1 = ColoredPoint(1, 2, 'white')
    point2 = ColoredPoint(1, 2, 'white')
    point3 = ColoredPoint(3, 4, 'black')

    print(point1 == point2)
    print(hash(point1) == hash(point2))
    print(point1 == point3)
    print(hash(point1) == hash(point3))

    row1 = Row(a=1, b=2, c=3)
    row2 = Row(a=1, b=2, c=3)
    row3 = Row(b=2, c=3, a=1)

    print(row1 == row2)
    print(hash(row1) == hash(row2))
    print(row1 == row3)
    print(hash(row1) == hash(row3))