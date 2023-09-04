

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