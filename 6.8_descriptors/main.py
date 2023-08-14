"""

Класс NonKeyword
Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:

name — имя атрибута, за которым будет закреплен дескриптор
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError с текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)
Sample Output 1:

Peter
Sample Input 2:

class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
Sample Output 2:

Атрибут не найден
Sample Input 3:

class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)
Sample Output 3:

Некорректное значение


"""
from keyword import kwlist
class NonKeyword:
    key_words = kwlist
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if  value not in self.key_words:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')
        
    def __delete__(self, obj):
        del obj.__dict__[self._attr]

#2
"""
Класс NonNegativeInteger
Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя атрибута, за которым будет закреплен дескриптор
default — значение по умолчанию. Если не передан, имеет значение None
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию равняется None, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

print(student.score)
Sample Output 1:

90
Sample Input 2:

class Student:
    score = NonNegativeInteger('score', 0)

student = Student()

print(student.score)
student.score = 0
print(student.score)
Sample Output 2:

0
0
Sample Input 3:

class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)
Sample Output 3:

Атрибут не найден
Sample Input 4:

class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)
Sample Output 4:

Некорректное значение


"""

class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name_attr = name
        self.default = default

    def __get__(self, obj, cls):
        if self._name_attr not in obj.__dict__ and self.default is None:
            raise AttributeError('Атрибут не найден')
        if self._name_attr in obj.__dict__:
            return obj.__dict__[self._name_attr]
        else:
            obj.__dict__[self._name_attr] = self.default
            return obj.__dict__[self._name_attr]

    def __set__(self, obj, value):
        if  type(value) != int or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._name_attr] = value
            
#3
"""
Класс LimitedTakes
Реализуйте класс LimitedTakes, описывающий дескриптор, который позволяет получать значение атрибута лишь определенное количество раз. При создании экземпляра класс должен принимать один аргумент:

times — количество доступных обращений к атрибуту
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
Если к атрибуту было выполнено times обращений, во время всех последующих обращений должно возбуждаться исключение MaxCallsException с текстом:

Превышено количество доступных обращений
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса LimitedTakes нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class Student:
    name = LimitedTakes(3)

student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)
Sample Output 1:

Gwen
Gwen
Gwen
Превышено количество доступных обращений
Sample Input 2:

class Student:
    name = LimitedTakes(3)

student = Student()

for _ in range(100):
    student.name = 'Gwen'
    
print(student.name)
Sample Output 2:

Gwen


"""
class MaxCallsException(Exception):
    pass

class LimitedTakes:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, times):
        self._times = times

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        if self._times > 0:
            self._times -= 1
            return obj.__dict__[self._attr]
        else:
            raise MaxCallsException('Превышено количество доступных обращений')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value



if __name__ == "__main__":
    
    class NonKeywordData:
        obj = NonKeyword('obj')


    data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
    nonkeyworddata = NonKeywordData()

    for item in data:
        nonkeyworddata.obj = item
        print(nonkeyworddata.obj)


    class Student:
        score = NonNegativeInteger('score')

    student = Student()
    student.score = 90

    print(student.score)

    class Student:
        score = NonNegativeInteger('score', 0)

    student = Student()

    print(student.score)
    student.score = 0
    print(student.score)


    class Student:
        name = LimitedTakes(3)

    student = Student()
    student.name = 'Gwen'

    print(student.name)
    print(student.name)
    print(student.name)

    try:
        print(student.name)
    except MaxCallsException as e:
        print(e)