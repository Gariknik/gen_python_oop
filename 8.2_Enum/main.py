"""
Класс HTTPStatusCodes
Коды состояния HTTP представляют собой трехзначные целые числа и используются для указания успешности конкретного HTTP запроса. Выделяют пять групп кодов состояния:

информация (100-199)
успех (200-299)
перенаправление (300-399)
ошибка клиента (400-499)
ошибка сервера (500-599)
Реализуйте класс HTTPStatusCodes, описывающий перечисление с  кодами состояния HTTP. Перечисление должно иметь пять элементов:

CONTINUE — элемент со значением 100
OK — элемент со значением 200
USE_PROXY — элемент со значением 305
NOT_FOUND — элемент со значением 404
BAD_GATEWAY — элемент со значением 502
Элемент перечисления должен иметь два метода:

info() — метод, возвращающий двухэлементный кортеж, содержащий имя элемента и его значение
code_class() — метод, возвращающий название группы на русском, к которой относится элемент
Примечание 1. Подробнее про коды состояния HTTP можно почитать по ссылке.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса HTTPStatusCodes нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())
Sample Output:

('OK', 200)
успех

"""
from enum import Enum
class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502
    
    def info(self):
        return self.name, self.value

    def code_class(self):
        match self.value//100:
            case 1: return 'информация'
            case 2: return 'успех'
            case 3: return 'перенаправление'
            case 4: return 'ошибка клиента'
            case 5: return 'ошибка сервера'
            case _: return 'другое'


"""
Класс Seasons
Реализуйте класс Seasons, описывающий перечисление с временами года. Перечисление должно иметь четыре элемента:

WINTER — элемент со значением 1
SPRING — элемент со значением 2
SUMMER — элемент со значением 3
FALL — элемент со значением 4
Элемент перечисления должен иметь один метод:

text_value() — метод, принимающий в качестве аргумента код страны en или ru и возвращающий строковое значение элемента в зависимости от переданного аргумента. Для WINTER en и ru значениями являются winter и зима соответственно, для SPRING — spring и весна, для SUMMER — summer и лето, для FALL — fall и осень
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Seasons нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))
Sample Output:

осень
fall
"""

from enum import Enum, auto

class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, l):
        dict_seasons = {1: {'en': 'winter', 'ru': 'зима'},
                        2: {'en': 'spring', 'ru': 'весна'},
                        3: {'en': 'summer', 'ru': 'лето'},
                        4: {'en': 'fall', 'ru': 'осень'}}
        return dict_seasons[self.value][l]

"""
Классы Weekday и NextDate
1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

MONDAY — элемент со значением 0
TUESDAY — элемент со значением 1
WEDNESDAY — элемент со значением 2
THURSDAY — элемент со значением 3
FRIDAY — элемент со значением 4
SATURDAY — элемент со значением 5
SUNDAY — элемент со значением 6
2. Также реализуйте класс NextDate, позволяющий определять дату следующего дня недели, начиная с текущего дня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

today — дата текущего дня, представленная экземпляром класса date
weekday — день недели, представленный элементом перечисления Weekday
after_today — булево значение, по умолчанию равняется False
Параметр after_today должен определять, учитывается ли текущая дата при определении даты следующего дня недели. Если он имеет значение False, текущая дата не должна учитываться, если True — должна учитываться.

Класс NextDate должен иметь два метода экземпляра:

date() — метод, возвращающий дату следующего дня недели в виде экземпляра класса date
days_until() — метод, возвращающий количество дней до даты следующего дня недели
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница

print(next_friday.date())
print(next_friday.days_until())
Sample Output 1:

2023-04-21
4
Sample Input 2:

from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего

print(next_monday.date())
print(next_monday.days_until())
Sample Output 2:

2023-04-24
7
Sample Input 3:

from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего

print(next_monday.date())
print(next_monday.days_until())
Sample Output 3:

2023-04-17
0

"""

from enum import Enum
from datetime import datetime, timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:
    def __init__(self, today, weekday, after_today=False) -> None:
        self.count = 0
        self.today = datetime(today.year, today.month, today.day)
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.today.date().weekday() == self.weekday.value and self.after_today == True:
            return self.today.date()
        if self.today.date().weekday() == self.weekday.value and self.after_today == False:
            self.today += timedelta(days=1)
            self.count += 1
            self.today, self.count = self.find_next_day(self.today, self.weekday, self.count)
            return self.today.date()
        if self.today.date().weekday() != self.weekday.value:
            self.today, self.count = self.find_next_day(self.today, self.weekday, self.count)
            return self.today.date()
    @staticmethod
    def find_next_day(today, weekday, count):
        while today.date().weekday() != weekday.value:
            today += timedelta(days=1)
            count += 1
        return today, count
        
    def days_until(self):
        return self.count



if __name__ == "__main__":
    print(HTTPStatusCodes.OK.info())
    print(HTTPStatusCodes.OK.code_class())

    print(HTTPStatusCodes.BAD_GATEWAY.info())
    print(HTTPStatusCodes.BAD_GATEWAY.code_class())

    print(Seasons.FALL.text_value('ru'))
    print(Seasons.FALL.text_value('en'))


    from datetime import date

    for weekday in Weekday:
        today = date(2023, 4, 27)                              # четверг
        next_date = NextDate(today, weekday, True)

        print(next_date.date())
        print(next_date.days_until())