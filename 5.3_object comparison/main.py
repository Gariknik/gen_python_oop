#1
"""

Класс Vector
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата вектора по оси
�
x
y — координата вектора по оси
�
y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:

Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать операции сравнения с помощью операторов == и!=. Два вектора считаются равными, если их координаты по обеим осям совпадают. Методы, реализующие операции сравнения, должны уметь сравнивать как два вектора между собой, так и вектор с кортежем из двух чисел, представляющих координаты
�
x и
�
y.

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)
Sample Output 1:

True
False
Sample Input 2:

a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
Sample Output 2:

True
False
False
False

"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        if type(other) == tuple and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return NotImplemented

#2
"""

Класс Word
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:

word — слово
Экземпляр класса Word должен иметь следующее формальное строковое представление:

Word('<слово в исходном виде>')
И следующее неформальное строковое представление:

<слово, в котором первая буква заглавная, а все остальные строчные>
Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают. Слово считается больше другого слова, если его длина больше.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Word нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))
Sample Output 1:

True
True
False
True
True
Sample Input 2:

words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))
Sample Output 2:

[Word('bee'), Word('geek'), Word('python')]
Bee
Python
Напишите про

"""

from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        self.__word = value

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return self.word.capitalize()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented


#3
"""

Класс Month
Реализуйте класс Month, описывающий месяц. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

year — год
month — порядковый номер месяца
Экземпляр класса Month должен иметь следующее формальное строковое представление:

Month(<год>, <порядковый номер месяца>)
И следующее неформальное строковое представление:

<год>-<порядковый номер месяца>
Также экземпляры класса Month должны поддерживать все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Month объекта считаются равными, если их годы и порядковые номера месяцев совпадают. Month объект считается больше другого Month объекта, если его год больше. В случае если два Month объекта имеют равные года, большим считается тот, чей месяц больше. Методы, реализующие операции сравнения, должны уметь сравнивать как два Month объекта между собой, так и Month объект с кортежем из двух чисел, представляющих год и месяц.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Month нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))
Sample Output 1:

True
True
False
True
False
Sample Input 2:

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))
Sample Output 2:

[Month(1998, 12), Month(1999, 12), Month(2000, 1)]
Sample Input 3:

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))
Sample Output 3:

1998-12
2000-1

"""
from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        if type(other) == tuple:
            return self.year == other[0] and self.month == other[1]
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year < other.year) or (self.year == other.year and self.month < other.month)
        if type(other) == tuple and len(other) == 2:
            return (self.year < other[0]) or (self.year == other[0] and self.month < other[1])
        return NotImplemented

#4
"""

Класс Version
Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:

version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
Экземпляр класса Version должен иметь следующее формальное строковое представление:

Version('<версия ПО в виде трех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:

<версия ПО в виде трех целых чисел, разделенных точками>
Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Version нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))
Sample Output 1:

False
False
True
False
True
Sample Input 2:

print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))
Sample Output 2:

True
True
True
Sample Input 3:

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))
Sample Output 3:

[Version('1.9.1'), Version('2.0.0'), Version('2.1.0')]
1.9.1
2.1.0

"""
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        if len(version.split('.')) == 3:
            self.version_t = tuple(int(num) for num in version.split('.'))
            self.version = version
        else:
            diff = 3 - len(version.split('.'))
            self.version_t = tuple([int(num) for num in version.split('.')] + [0] * diff)
            self.version = '.'.join([version] + ['0'] * diff)

    def __repr__(self):
        return f"Version('{self.version}')"

    def __str__(self):
        return self.version

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version_t == other.version_t
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version_t < other.version_t
        return NotImplemented

if __name__ == '__main__':
    # a = Vector(1, 2)
    # b = Vector(1, 2)
    #
    # print(a == b)
    # print(a != b)

    print(Word('bee') == Word('hey'))
    print(Word('bee') < Word('geek'))
    print(Word('bee') > Word('geek'))
    print(Word('bee') <= Word('geek'))
    print(Word('bee') >= Word('gee'))

    words = [Word('python'), Word('bee'), Word('geek')]

    print(sorted(words))
    print(min(words))
    print(max(words))

    print(Month(1999, 12) == Month(1999, 12))
    print(Month(1999, 12) < Month(2000, 1))
    print(Month(1999, 12) > Month(2000, 1))
    print(Month(1999, 12) <= Month(1999, 12))
    print(Month(1999, 12) >= Month(2000, 1))

    # TEST_4:
    month = Month(2023, 4)
    not_supported = ['04.2023', 4.0, 2023, True, {2023: 4}, {4, 2023}, False, (2023, 4, 'dont know')]
    for obj in not_supported:
        print(month == obj)

    versions = [Version('2'), Version('2.1'), Version('1.9.1')]

    print(sorted(versions))
    print(min(versions))
    print(max(versions))

    print(Version('3') == Version('3.0'))
    print(Version('3') == Version('3.0.0'))
    print(Version('3.0') == Version('3.0.0'))