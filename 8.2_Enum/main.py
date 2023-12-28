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


        

if __name__ == "__main__":
    print(HTTPStatusCodes.OK.info())
    print(HTTPStatusCodes.OK.code_class())

    print(HTTPStatusCodes.BAD_GATEWAY.info())
    print(HTTPStatusCodes.BAD_GATEWAY.code_class())

    print(Seasons.FALL.text_value('ru'))
    print(Seasons.FALL.text_value('en'))