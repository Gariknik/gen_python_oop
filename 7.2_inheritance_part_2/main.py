

#1
"""

Классы BasicPlan и подклассы
1. Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе. При создании экземпляра класс не должен принимать никаких аргументов.

Класс BasicPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение False
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 1
price — атрибут, имеющий значение 8.99$
2. Также реализуйте класс SilverPlan, наследника класса BasicPlan, описывающий подписку среднего уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса SilverPlan должен совпадать с процессом создания экземпляра класса BasicPlan.

Класс SilverPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение False
num_of_devices — атрибут, имеющий значение 2
price — атрибут, имеющий значение 12.99$
3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan, описывающий подписку высокого уровня на некотором онлайн-сервисе. Процесс создания экземпляра класса GoldPlan должен совпадать с процессом создания экземпляра класса BasicPlan.

Класс GoldPlan должен иметь семь атрибутов:

can_stream —  атрибут, имеющий значение True
can_download — атрибут, имеющий значение True
has_SD — атрибут, имеющий значение True
has_HD — атрибут, имеющий значение True
 has_UHD — атрибут, имеющий значение True
num_of_devices — атрибут, имеющий значение 4
price — атрибут, имеющий значение 15.99$
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(BasicPlan.can_stream)
print(BasicPlan.can_download)
print(BasicPlan.has_SD)
print(BasicPlan.has_HD)
print(BasicPlan.has_UHD)
print(BasicPlan.num_of_devices)
print(BasicPlan.price)
Sample Output 1:

True
True
True
False
False
1
8.99$
Sample Input 2:

print(SilverPlan.can_stream)
print(SilverPlan.can_download)
print(SilverPlan.has_SD)
print(SilverPlan.has_HD)
print(SilverPlan.has_UHD)
print(SilverPlan.num_of_devices)
print(SilverPlan.price)
Sample Output 2:

True
True
True
True
False
2
12.99$
Sample Input 3:

print(GoldPlan.can_stream)
print(GoldPlan.can_download)
print(GoldPlan.has_SD)
print(GoldPlan.has_HD)
print(GoldPlan.has_UHD)
print(GoldPlan.num_of_devices)
print(GoldPlan.price)
Sample Output 3:

True
True
True
True
True
4
15.99$

"""
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'

class SilverPlan(BasicPlan):
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = True
    has_UHD = False
    num_of_devices = 2
    price = '12.99$'

class GoldPlan(BasicPlan):
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'
#2
"""

Классы WeatherWarning и WeatherWarningWithDate
Реализуйте класс WeatherWarning, описывающий объект, предупреждающий о погодных изменениях. При создании экземпляра класс не должен принимать никаких аргументов.

Класс WeatherWarning должен иметь три метода экземпляра:

rain() — метод, выводящий текст:
Ожидаются сильные дожди и ливни с грозой
snow() — метод, выводящий текст:
Ожидается снег и усиление ветра
low_temperature() — метод, выводящий текст:
Ожидается сильное понижение температуры
Также реализуйте класс WeatherWarningWithDate, наследника класса WeatherWarning, описывающий объект, предупреждающий о погодных изменениях с указанием даты. Процесс создания экземпляра класса WeatherWarningWithDate должен совпадать с процессом создания экземпляра класса WeatherWarning.

Класс WeatherWarningWithDate должен иметь три метода экземпляра:

rain() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
<дата в формате DD.MM.YYYY>
Ожидаются сильные дожди и ливни с грозой
snow() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
<дата в формате DD.MM.YYYY>
Ожидается снег и усиление ветра
low_temperature() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
<дата в формате DD.MM.YYYY>
Ожидается сильное понижение температуры
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(WeatherWarningWithDate, WeatherWarning))
Sample Output 1:

True
Sample Input 2:

weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()
Sample Output 2:

Ожидаются сильные дожди и ливни с грозой
Ожидается снег и усиление ветра
Ожидается сильное понижение температуры
Sample Input 3:

from datetime import date

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)
Sample Output 3:

12.12.2022
Ожидаются сильные дожди и ливни с грозой
12.12.2022
Ожидается снег и усиление ветра
12.12.2022
Ожидается сильное понижение температуры

"""
from datetime import date
from typing import Any
# from typing_extensions import SupportsIndex

class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')
    
    def snow(self):
        print('Ожидается снег и усиление ветра')
    
    def low_temperature(self):
        print('Ожидается сильное понижение температуры')

class WeatherWarningWithDate(WeatherWarning):
    def rain(self, obj):
        if isinstance(obj, date):
            print(f"{obj.strftime('%d.%m.%Y')}")
            print('Ожидаются сильные дожди и ливни с грозой')
    
    def snow(self, obj):
        if isinstance(obj, date):
            print(f"{obj.strftime('%d.%m.%Y')}")
            print('Ожидается снег и усиление ветра')
    
    def low_temperature(self, obj):
        if isinstance(obj, date):
            print(f"{obj.strftime('%d.%m.%Y')}")
            print("Ожидается сильное понижение температуры")



# Напишите определение класса File       
class File:
    def __init__(self, size):
        self._size_in_bytes = size

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B" 
        elif 1023 < self._size_in_bytes and self._size_in_bytes < 1048576:
            return f"{self._size_in_bytes/1024:.2f} KB"
        elif 1048575 < self._size_in_bytes and self._size_in_bytes < 1073741824:
            return f"{self._size_in_bytes/1048576:.2f} MB"
        else:
             return f"{self._size_in_bytes/1073741824:.2f} GB"
    @size.setter
    def size(self, value):
        self._size_in_bytes = value

#3
"""

Классы Triangle и EquilateralTriangle
Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — длина стороны треугольника
b — длина стороны треугольника
c — длина стороны треугольника
Класс Triangle должен иметь один метод экземпляра:

perimeter() — метод, возвращающий периметр треугольника
Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний треугольник. При создании экземпляра класс должен принимать один аргумент:

side — длина стороны треугольника
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(EquilateralTriangle, Triangle))
Sample Output 1:

True
Sample Input 2:

triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())
Sample Output 2:

12
9

"""
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 3 * self.a


#4
"""

Класс Counter и DoubledCounter
Вам доступен класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс принимает один аргумент:

start — начальное значение счетчика, по умолчанию равняется 0
Экземпляр класса Counter имеет один атрибут:

value — текущее значение счетчика
Класс Counter имеет два метода экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если число не передано, метод увеличивает значение счетчика на единицу
dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число не передано, метод уменьшает значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным
Реализуйте класс DoubledCounter, наследника класса Counter, описывающий неотрицательный счетчик, значение которого увеличивается и уменьшается дважды при вызове соответствующих методов. Процесс создания экземпляра класса DoubledCounter должен совпадать с процессом создания экземпляра класса Counter.

Экземпляр класса DoubledCounter должен иметь один атрибут:

value — текущее значение счетчика
Класс DoubledCounter должен иметь два метода экземпляра:

inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число дважды. Если число не передано, метод должен увеличить значение счетчика на два
dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число дважды. Если число не передано, метод должен уменьшить значение счетчика на два. Значение счетчика считается равным 0, если при уменьшении оно становится отрицательным
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(DoubledCounter, Counter))
Sample Output 1:

True
Sample Input 2:

counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
Sample Output 2:

10
16
5
0
Sample Input 3:

counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
Sample Output 3:

20
32
10
0

"""

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)

class DoubledCounter(Counter):
    def inc(self, n=1):
        self.value += n*2

    def dec(self, n=1):
        self.value = max(self.value - n*2, 0) 


#5
"""
Классы Summator и подклассы🌶️
1. Реализуйте класс Summator, описывающий объект, вычисляющий сумму натуральных чисел от 
1
1 до 
�
n:
1
+
2
+
3
+
.
.
.
+
�
1+2+3+...+n
При создании экземпляра класс не должен принимать никаких аргументов.

Класс Summator должен иметь один метод экземпляра:

total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел от 1 до n включительно
2. Помимо этого, реализуйте класс SquareSummator, наследника класса Summator, описывающий объект, вычисляющий сумму квадратов натуральных чисел от 
1
1 до 
�
n:
1
2
+
2
2
+
3
2
+
.
.
.
+
�
2
1 
2
 +2 
2
 +3 
2
 +...+n 
2
 
Процесс создания экземпляра класса SquareSummator должен совпадать с процессом создания экземпляра класса Summator.

Класс SquareSummator должен иметь один метод экземпляра:

total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму квадратов целых чисел от 1 до n включительно
3. Также реализуйте класс QubeSummator, наследника класса Summator, описывающий объект, вычисляющий сумму кубов натуральных чисел от 
1
1 до 
�
n:
1
3
+
2
3
+
3
3
+
.
.
.
+
�
3
1 
3
 +2 
3
 +3 
3
 +...+n 
3
 

Процесс создания экземпляра класса QubeSummator должен совпадать с процессом создания экземпляра класса Summator.

Класс QubeSummator должен иметь один метод экземпляра:

total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму кубов целых чисел от 1 до n включительно
4. Наконец, реализуйте класс CustomSummator, наследника класса Summator, описывающий объект, вычисляющий сумму произвольных степеней натуральных чисел от 
1
1 до 
�
n:
1
�
+
2
�
+
3
�
+
.
.
.
+
�
�
1 
m
 +2 
m
 +3 
m
 +...+n 
m
 

При создании экземпляра класс должен принимать один аргумент:

m — степень чисел в последовательности
Класс CustomSummator должен иметь один метод экземпляра:

total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел в степени m от 1 до n включительно
Примечание 1. Попытайтесь реализовать классы таким образом, чтобы метод total() был определен лишь в классе Summator.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))
Sample Output 1:

True
True
Sample Input 2:

summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
Sample Output 2:

6
14
36
Sample Input 3:

summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
Sample Output 3:

6
14
36


"""
class Summator:
    def __init__(self, m=1):
        self.m = m
    
    def total(self, n):
        return sum([num ** self.m for num in range(1, n+1)])
    
class SquareSummator(Summator):
    def __init__(self, m=2):
        self.m = m
    
class QubeSummator(Summator):
    def __init__(self, m=3):
        self.m = m 
    
class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

#7
"""

Класс FieldTracker🌶️🌶️
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:

base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута было изменено хотя бы раз, или False в противном случае
changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а значениями — их исходные значения
save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои значения, а их текущие значения считаются исходными
Гарантируется, что наследники класса FieldTracker:

всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений отслеживаемым атрибутам
Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение отличается от текущего.

Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)

print(point.base('x'))
print(point.has_changed('x'))
print(point.changed())
Sample Output 1:

1
False
{}
Sample Input 2:

class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
Sample Output 2:

1
3
True
True
{'x': 1, 'z': 3}
Sample Input 3:

class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()

point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base('x'))
print(point.base('z'))
print(point.has_changed('x'))
print(point.has_changed('z'))
print(point.changed())
Sample Output 3:

0
4
False
False
{}

"""
class FieldTracker:
    def base(self, attr):
        pass

    def has_changed(self):
        pass

    def changed(self):
        pass

    def save(self):
        pass


#8
"""

Класс UpperPrintString
Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра класса UpperPrintString должен совпадать с процессом создания экземпляра класса str.

Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:

<значение строки в верхнем регистре>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса UpperPrintString нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)
Sample Output 1:

BEEGEEK
BEEGEEK
Sample Input 2:

s = UpperPrintString('beegeek')
print(list(s))
Sample Output 2:

['b', 'e', 'e', 'g', 'e', 'e', 'k']

"""
class UpperPrintString(str):
    def __str__(self):
        return self.upper()

#9
"""
Класс LowerString
Реализуйте класс LowerString, наследника класса str, описывающий строку, которая во время создания автоматически переводится в нижний регистр. При создании экземпляра класс должен принимать один аргумент:

obj — объект, определяющий начальное значение строки. Может быть не передан, в таком случае начальное значение считается пустой строкой
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса LowerString нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))
Sample Output 1:

beegeek
beegeek
True
True
Sample Input 2:

print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))
Sample Output 2:

['bee', 'geek']
{'a': 1, 'b': 2, 'c': 3}
Sample Input 3:

s = LowerString('BeeGeek')

print(s[0], s[3])
Sample Output 3:

b g

"""
class LowerString(str):
    def __new__(cls, obj=None):
        if obj:
            return super().__new__(cls, str(obj).lower())
        return super().__new__(cls, '')



#10
"""

Класс FuzzyString
Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)
Sample Output:

True
True
True
False

"""

class FuzzyString(str):
    def __eq__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() == other.lower() 
    def __ne__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() != other.lower()      

    def __lt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() < other.lower()  
    def __gt__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() > other.lower()  
    def __le__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() <= other.lower()  
    def __ge__(self, other):
        if not isinstance(other, (FuzzyString, str)):
            return NotImplemented
        return self.lower() >= other.lower()  
    def __contains__(self, other):
        if not isinstance(other, (FuzzyString, str)) or not isinstance(self, (FuzzyString, str)):
            return NotImplemented
        return other.lower() in self.lower()  
    
#11
"""

Класс TitledText
Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

content — текст
text_title — заголовок текста
Класс TitleText должен иметь один метод экземпляра:

title() — метод, возвращающий заголовок текста
Примечание 1. Значением экземпляра класса TitledText должен быть именно текст, а не заголовок текста или текст вместе с заголовком.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса TitledText нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))
Sample Output 1:

Сreate a class Soda
Homework
True
Sample Input 2:

titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)
Sample Output 2:

True

"""
class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance
   
    def title(self):
        return self.text_title
    
#12
"""

Класс SuperInt
Реализуйте класс SuperInt, наследника класса int, описывающий целое число с дополнительным функционалом. Процесс создания экземпляра класса SuperInt должен совпадать с процессом создания экземпляра класса int.

Класс SuperInt должен иметь четыре метода экземпляра:

repeat() — метод, принимающий в качестве аргумента целое число n, по умолчанию равное 2, и возвращающий экземпляр класса SuperInt, продублированный n раз
to_bin() — метод, возвращающий двоичное представление экземпляра класса SuperInt. Двоичное представление может быть как в виде экземпляра класса str, так и int
next() — метод, возвращающий новый экземпляр класса SuperInt, который больше текущего на единицу
prev() — метод, возвращающий новый экземпляр класса SuperInt, который меньше текущего на единицу
Также экземпляр класса SuperInt должен быть итерируемым объектом, элементами которого являются его цифры слева направо. Сами цифры так же должны быть представлены в виде экземпляров класса SuperInt.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса SuperInt нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))
Sample Output 1:

1717
-171717
Sample Input 2:

superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())
Sample Output 2:

10001
-10001
Sample Input 3:

superint = SuperInt(17)

print(superint.prev())
print(superint.next())
Sample Output 3:

16
18
Sample Input 4:

superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
Sample Output 4:

1 3 3 7
2 0 7 7


"""

# class SuperInt(int):
#     def __init__(self, num):
#         self.num = num

#     def __str__(self):
#         return str(self.num)

#     def repeat(self, rep=2):
#         if self.num < 0:
#             return SuperInt(int(str(self)[0] + str(self)[1:] * rep))
#         return SuperInt(int(str(self)*rep))
    
#     def to_bin(self):
#         bin_int = bin(self.num)
#         if self.num < 0:   
#             return bin_int[0]+bin_int[3:]
#         return bin_int[2:]

#     def next(self):
#         return SuperInt(self.num+1)
    
#     def prev(self):
#         return SuperInt(self.num-1)
    
#     def __iter__(self):
#         return iter(map(SuperInt, str(abs(self))))
    

class SuperInt(int):
    def repeat(self, n=2):
        digit = f"{'-' * (self < 0)}{f'{abs(self)}' * n}"
        return type(self)(digit)

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return type(self)(self + 1)

    def prev(self):
        return type(self)(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))




#13
"""

Класс RoundedInt
Ближайшим четным числом для целого нечетного числа n будем считать n + 1, ближайшим четным числом для целого четного числа будет оно само. Аналогично ближайшим нечетным числом для целого четного числа n будем считать n + 1, ближайшим нечетным числом для целого нечетного числа будет оно само.

Реализуйте класс RoundedInt, наследника класса int, описывающий целое число, которое во время создания автоматически округляется до ближайшего четного или нечетного числа. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

num — объект, определяющий числовое значение экземпляра класса RoundedInt
even — булево значение, определяющее четность при округлении. Если имеет значение True, округление происходит до ближайшего четного, если False — до ближайшего нечетного. По умолчанию имеет значение True
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RoundedInt нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))
Sample Output 1:

8
8
7
9
Sample Input 2:

roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
Sample Output 2:

15
9
8
<class '__main__.RoundedInt'>
<class '__main__.RoundedInt'>

"""
class RoundedInt(int):
    def __new__(cls, num, even=True):
        num += (num % 2 == 1) if even else (num % 2 == 0)
        instance = super().__new__(cls, num)
        return instance
    

#14
"""
Класс AdvancedTuple
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)
Sample Output 1:

(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
('a', 'b', 1, 2, 3)
Sample Input 2:

advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))
Sample Output 2:

(1, 2, 3, 4, 5, 6, 7, 8)
<class '__main__.AdvancedTuple'>
"""
class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented
    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented



"""
Класс ModularTuple
Реализуйте класс ModularTuple, наследника класса tuple, описывающий кортеж, элементы которого во время создания автоматически делятся с остатком на заданное число. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса ModularTuple. Если не передан, начальный набор элементов считается пустым
size — целое число, на которое делятся с остатком все элементы создаваемого экземпляра класса ModularTuple, по умолчанию имеет значение 100
Примечание 1. Экземпляр класса ModularTuple не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса ModularTuple измениться  не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ModularTuple нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))
Sample Output 1:

(1, 2, 3, 4, 5)
<class '__main__.ModularTuple'>
Sample Input 2:

modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)
Sample Output 2:

(1, 0, 1, 0, 1)


"""

class ModularTuple(tuple):
    def __new__(cls, iterable=None, size=100):
        if iterable:
            iterable = map(lambda x: x%size, iterable)
            instance = super().__new__(cls, iterable)
            return instance
        return super().__new__(cls, ())

"""
Класс DefaultList
Реализуйте класс DefaultList, наследника класса UserList, описывающий список, который при попытке получить элемент по несуществующему индексу возвращает значение по умолчанию. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса DefaultList. Если не передан, начальный набор элементов считается пустым
default — значение, возвращаемое при попытке получить элемент по несуществующему индексу. По умолчанию равняется None
Примечание 1. Экземпляр класса DefaultList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса DefaultList измениться  не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DefaultList нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

defaultlist = DefaultList([1, 2, 3])

print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])
Sample Output 1:

1
3
None
None
Sample Input 2:

defaultlist = DefaultList([1, 2, 3], 0)

print(defaultlist[0])
print(defaultlist[-1])
print(defaultlist[100])
print(defaultlist[-100])
Sample Output 2:

1
3
0
0

"""

from collections import UserList
class DefaultList(UserList):  
    def __init__(self, iterable, default=None):
        super().__init__(item for item in iterable)
        self.default = default

    def __getitem__(self, key):
        try:
            return self.data[key]
        except:
            return self.default

"""

Класс EasyDict
Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать с процессом создания экземпляра класса dict.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)
Sample Output 1:

Timur
Moscow
Sample Input 2:

easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

easydict['city'] = 'Dubai'
easydict['age'] = 30
print(easydict.city)
print(easydict.age)
Sample Output 2:

Dubai
30
Sample Input 3:

easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)
Sample Output 3:

{'name': 'Artur', 'city': 'Almetevsk'}

"""
from collections import UserDict
class EasyDict(UserDict):
    def __getattr__(self, attr):
        return self.data[attr]

"""

Класс TwoWayDict
Реализуйте класс TwoWayDict, наследника класса UserDict, описывающий двунаправленный словарь, в который при добавлении пары ключ: значение также добавляется и пара значение: ключ. Процесс создания экземпляра класса TwoWayDict должен совпадать с процессом создания экземпляра класса UserDict.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса TwoWayDict нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

twowaydict = TwoWayDict({'apple': 1})

twowaydict['banana'] = 2

print(twowaydict['apple'])
print(twowaydict[1])
print(twowaydict['banana'])
print(twowaydict[2])
Sample Output 1:

1
apple
2
banana
Sample Input 2:

d = TwoWayDict()
d[3] = 8
d[7] = 6
print(d[3], d[8])
print(d[7], d[6])

d.update({9: 7, 8: 2})
print(d[9], d[7])
print(d[8], d[2])
Sample Output 2:

8 3
6 7
7 9
2 8

"""
from collections import UserDict
class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key


"""
Класс AdvancedList
Реализуйте класс AdvancedList, наследника класса list, описывающий список с дополнительным функционалом. Процесс создания экземпляра класса AdvancedList должен совпадать с процессом создания экземпляра класса list.

Класс AdvancedList должен иметь три метода экземпляра:

join() — метод, объединяющий все элементы экземпляра класса AdvancedList в строку и возвращающий полученный результат. Метод должен принимать один строковый аргумент, по умолчанию равный пробелу, который является разделителем элементов списка в результирующей строке
map() — метод, принимающий в качестве аргумента функцию func и применяющий ее к каждому элементу экземпляра класса AdvancedList. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый
filter() — метод, принимающий в качестве аргумента функцию func и удаляющий из экземпляра класса AdvancedList те элементы, для которых функция func вернула значение False. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AdvancedList нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join('-'))
Sample Output 1:

1 2 3 4 5
1-2-3-4-5
Sample Input 2:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
Sample Output 2:

[-1, -2, -3, -4, -5]
Sample Input 3:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)
Sample Output 3:

[2, 4]
Sample Input 4:

advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)
Sample Output 4:

[1, 2, 3, 4, 5]
True
"""


class AdvancedList(list):
    def join(self,  sep=' '):
        string = ''
        length = len(sep)
        for ch in self:
            string += str(ch)
            string += sep
        return string[:-length]
    
    def map(self, func):
        self[:] = [func(el) for el in self]

    def filter(self, func):
        self[:] = [el for el in self if func(el)]



"""

Класс NumberList
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа
Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:

Элементами экземпляра класса NumberList должны быть числа
Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)
Sample Output 1:

[0, 1, 2, 3, 4, 5]
Sample Input 2:

numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)
Sample Output 2:

[0, 1, 2, 3, 4, 5]
Sample Input 3:

try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)
Sample Output 3:

Элементами экземпляра класса NumberList должны быть числа
Sample Input 4:

numberlist = NumberList([1, 2, 3])

try:
    numberlist.append('4')
except TypeError as error:
    print(error)
Sample Output 4:

Элементами экземпляра класса NumberList должны быть числа


"""

class NumberList(list):
    
    def __init__(self, iterable):
        if self.check_num(iterable):
            super().__init__(iterable)
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
   
    @staticmethod
    def check_num(obj):
        if hasattr(obj, '__iter__'):
            return all(type(el) in (int, float) for el in obj)
        return type(obj) in (int, float)
        
    def __setitem__(self, key, value):
        if self.check_num(value):
            super().__setitem__(key, value)
            return self
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __add__(self, other):
        if isinstance(other, NumberList):
            return super().__add__(other)
        elif isinstance(other,  list):  
            return super().__add__(NumberList(other))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other,  NumberList):
            super().__iadd__(other)
            return self
        elif isinstance(other,  list):
            super().__iadd__(NumberList(other))
            return self
        return NotImplemented
    
    def append(self, num):
        if self.check_num(num):
            super().append(num)
            return self
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
        
    def extend(self, it):
        if self.check_num(it):
            super().extend(it)
            return self
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
    
    def insert(self, index, obj):
        if type(obj) in (int, float):
            super().insert(index, obj)
            return self
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")


"""

Класс ValueDict
Реализуйте класс ValueDict, наследника класса dict, описывающий словарь c дополнительным функционалом. Процесс создания экземпляра класса ValueDict должен совпадать с процессом создания экземпляра класса dict.

Класс ValueDict должен иметь два метода экземпляра:

key_of() — метод, принимающий в качестве аргумента объект value и возвращающий первый ключ экземпляра класса ValueDict, имеющий значение value. Если такого ключа нет, метод должен вернуть None.
keys_of() — метод, принимающий в качестве аргумента объект value и возвращающий итерируемый объект, элементами которого являются все ключи экземпляра класса ValueDict, имеющие значение value
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ValueDict нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))
Sample Output 1:

banana
banana orange
Sample Input 2:

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

valuedict = ValueDict(countries)

print(valuedict.key_of('Moscow'))
print(*valuedict.keys_of('Washington'))
Sample Output 2:

None
Sample Input 3:

valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))
Sample Output 3:

None


"""
from collections import UserDict
class ValueDict(UserDict):
    def key_of(self, value):
        for key, val in self.data.items():
            if value == val:
                return key

    def keys_of(self, value):
        result = [k for k, v in self.data.items() if value == v]
        return result


"""

Класс BirthdayDict
Реализуйте класс BirthdayDict, наследника класса UserDict, описывающий словарь с информацией о днях рождения, ключами в котором являются имена, а значениями — даты дней рождения. Процесс создания экземпляра класса BirthdayDict должен совпадать с процессом создания экземпляра класса UserDict.

При добавлении новой пары ключ: значение в экземпляр класса BirthdayDict должна производиться проверка на наличие в этом экземпляре пары, которая имеет такое же значение, что и добавляемая пара. И если такая пара есть, должен выводиться текст:

Хей, <ключ добавляемой пары>, не только ты празднуешь день рождения в этот день!
Аналогичное поведение должно быть и при изменении значения по ключу.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса BirthdayDict нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

from datetime import date

birthdaydict = BirthdayDict()

birthdaydict['Боб'] = date(1987, 6, 15)
birthdaydict['Том'] = date(1984, 7, 15)
birthdaydict['Мария'] = date(1987, 6, 15)
Sample Output 1:

Хей, Мария, не только ты празднуешь день рождения в этот день!
Sample Input 2:

from datetime import date

birthdaydict = BirthdayDict()

birthdaydict['Боб'] = date(1987, 6, 15)
birthdaydict['Том'] = date(1984, 7, 15)
birthdaydict['Мария'] = date(1989, 10, 1)
birthdaydict['Боб'] = date(1989, 10, 1)
Sample Output 2:

Хей, Боб, не только ты празднуешь день рождения в этот день!

"""
from collections import UserDict
class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        super().__setitem__(key, value)
        
        
"""

Класс MutableString
Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.

Класс MutableString должен иметь три метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()
Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса MutableString нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)
Sample Output 1:

beegeek
BEEGEEK
BEEEEGK
Sample Input 2:

mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)
Sample Output 2:

beegeek
BeeGeek

"""
from collections import UserString
class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()
    
    def upper(self):
        self.data = self.data.upper()
    
    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))
    
    def __setitem__(self, key, value):
        lst = list(self.data)
        lst[key] = value
        self.data = ''.join(lst)

    def __delitem__(self, key):
        lst = list(self.data)
        del lst[key]
        self.data = ''.join(lst)
        

if __name__ == '__main__':
    print(SilverPlan.can_stream)
    print(SilverPlan.can_download)
    print(SilverPlan.has_SD)
    print(SilverPlan.has_HD)
    print(SilverPlan.has_UHD)
    print(SilverPlan.num_of_devices)
    print(SilverPlan.price)

    from datetime import date

    weatherwarning = WeatherWarningWithDate()
    dt = date(2022, 12, 12)

    weatherwarning.rain(dt)
    weatherwarning.snow(dt)
    weatherwarning.low_temperature(dt)

    triangle1 = Triangle(3, 4, 5)
    triangle2 = EquilateralTriangle(3)

    print(triangle1.perimeter())
    print(triangle2.perimeter())





    # Ниже код для проверки методов класса File

    file = File(5)
    assert file.size == "5 B"
    file.size = 1023

    assert file.size == "1023 B"
    print(file.size)
    file.size = 1024
    print(file.size)
    assert file.size == "1.00 KB"

    file_1 = File(1500000)
    #assert file_1._size_in_bytes == 1500000
    print(file_1._size_in_bytes)
    # assert file_1.size == "1.43 MB"
    print(file_1.size)


    file_2 = File(1500)
    # assert file_2.size == "1.46 KB"


    file_3 = File(2789326322)
    # assert file_3.size == "2.60 GB"
    file_3.size = 1073741824
    # assert file_3.size == "1.00 GB"

    print('Good')

    counter = DoubledCounter(20)

    print(counter.value)
    counter.inc()
    counter.inc(5)
    print(counter.value)
    counter.dec()
    counter.dec(10)
    print(counter.value)
    counter.dec(10)
    print(counter.value)


    summator1 = Summator()
    summator2 = CustomSummator(2)
    summator3 = CustomSummator(3)

    print(summator1.total(3))    # 1 + 2 + 3
    print(summator2.total(3))    # 1 + 4 + 9
    print(summator3.total(3))    # 1 + 8 + 27


    s1 = UpperPrintString('beegeek')
    s2 = UpperPrintString('BeeGeek')

    print(s1)
    print(s2)

    print(LowerString(['Bee', 'Geek']))
    print(LowerString({'A': 1, 'B': 2, 'C': 3}))

    s1 = FuzzyString('BeeGeek')
    s2 = FuzzyString('bee')

    print(s2 in s1)
    print(s1 in s2)


    titled = TitledText('Сreate a class Soda', 'Homework')

    print(titled)
    print(titled.title())
    print(issubclass(TitledText, str))


    superint1 = SuperInt(2023)

    for item in superint1:
        print(item, type(item))

    print(RoundedInt(7))
    print(RoundedInt(8))
    print(RoundedInt(7, False))
    print(RoundedInt(8, False))

    advancedtuple = AdvancedTuple([1, 2, 3])

    advancedtuple += [4, 5]
    advancedtuple += iter([6, 7, 8])
    print(advancedtuple)
    print(type(advancedtuple))


    modulartuple = ModularTuple([101, 102, 103, 104, 105])

    print(modulartuple)
    print(type(modulartuple))


    data = [1, 2, 3]
    defaultlist = DefaultList(data)

    print(defaultlist)
    data.extend([4, 5, 6])
    print(data)
    print(defaultlist)


    easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

    print(easydict['name'])
    print(easydict.city)


    twowaydict = TwoWayDict({'apple': 1})

    twowaydict['banana'] = 2

    print(twowaydict['apple'])
    print(twowaydict[1])
    print(twowaydict['banana'])
    print(twowaydict[2])

    numberlist = NumberList([1, 2, 3])

    try:
        numberlist.append('4')
    except TypeError as error:
        print(error)

    valuedict = ValueDict({})

    print(valuedict.key_of(12))
    print(*valuedict.keys_of(33))


    from datetime import date

    birthdaydict = BirthdayDict()

    birthdaydict['Боб'] = date(1987, 6, 15)
    birthdaydict['Том'] = date(1984, 7, 15)
    birthdaydict['Мария'] = date(1989, 10, 1)
    birthdaydict['Боб'] = date(1989, 10, 1)

    mutablestring = MutableString('Beegeek')

    mutablestring.lower()
    print(mutablestring)
    mutablestring.upper()
    print(mutablestring)
    mutablestring.sort()
    print(mutablestring)