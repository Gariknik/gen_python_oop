

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