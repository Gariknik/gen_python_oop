from abc import ABC, abstractmethod

class UniversalDate(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return f'{self.year}-{self.month:0>2}-{self.day:0>2}'   

class USADate(UniversalDate):   
    def format(self):
        return f'{self.month:0>2}-{self.day:0>2}-{self.year}'


class ItalianDate(UniversalDate):   
    def format(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'
    



"""

Классы MinStat, MaxStat и AverageStat
1. Реализуйте класс MinStat, описывающий объект, который находит минимальное значение среди определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MinStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий минимальное число из набора. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
2. Также реализуйте класс MaxStat, описывающий объект, который находит максимальное значение среди определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MaxStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий максимальное число из набора. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
3. Наконец, реализуйте класс AverageStat, описывающий объект, который находит среднее арифметическое определенного набора чисел. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс AverageStat должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
result() — метод, возвращающий среднее арифметическое набора чисел. Если набор пуст, метод должен вернуть значение None
clear() — метод, удаляющий из набора все числа
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
Sample Output 1:

1
5
3.0
Sample Input 2:

minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
Sample Output 2:

1
5
3.0
Sample Input 3:

minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
Sample Output 3:

None
None
None

"""
from abc import ABC, abstractmethod

class Stat(ABC):
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = iterable
    
    def __getitem__(self, indx):
        return self.iterable[indx]
    
    def __len__(self):
        return len(self.iterable)

    def add(self, num):
        self.iterable.append(num)
    
    def clear(self):
        self.iterable = []

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        if self:
            return min(self)
        
class MaxStat(Stat):
    def result(self):
        if self:
            return max(self)

class AverageStat(Stat):
    def result(self):
        if self:
            return sum(self)/len(self)










if __name__ == "__main__":
    usadate = USADate(2023, 4, 6)

    print(usadate.format())
    print(usadate.iso_format())

    minstat = MinStat([1, 2, 4])
    maxstat = MaxStat([1, 2, 4])
    averagestat = AverageStat([1, 2, 4])

    minstat.add(5)
    maxstat.add(5)
    averagestat.add(5)

    print(minstat.result())
    print(maxstat.result())
    print(averagestat.result())