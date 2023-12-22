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
        
"""
Классы LeftParagraph и RightParagraph
Будем называть словом любую последовательность из одной или более латинских букв.

1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен принимать один аргумент:

length — длина строки абзаца
Класс LeftParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс должен принимать один аргумент:

length — длина строки абзаца
Класс RightParagraph должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода текущий абзац считается пустым, то есть начинается формирование нового
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()
Sample Output 1:

death can
have me
when it
earns me
Sample Input 2:

rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()
Sample Output 2:

 death can
   have me
   when it
  earns me

"""

from abc import ABC, abstractmethod

class AbstractString(ABC):
    def __init__(self, length):
        self.length = length
        self.string = []

    def add(self, string):
        self.string += string.split()

    
    def __str__(self):
        return self.string

    @abstractmethod
    def end(self):
        pass
    


class LeftParagraph(AbstractString):

    def end(self):
        result = []
        last = ''
        row = ''
        for i in range(len(self.string)):
            if not last: 
                if len(row + self.string[i] + ' ') <= self.length:
                    row += self.string[i] + ' '
                else:
                    last = self.string[i]
                    result.append(row.strip())
                    row = ''
            else:
                row += last + ' ' + self.string[i] + ' '
                last = ''
        print('\n'.join(result))

        
            

class RightParagraph(AbstractString):
    def end(self):
        result = []
        last = ''
        row = ''
        for i in range(len(self.string)):
            if not last: 
                if len(row + self.string[i] + ' ') <= self.length:
                    row += self.string[i] + ' '
                else:
                    last = self.string[i]
                    result.append(row.strip())
                    row = ''
            else:
                row += last + ' ' + self.string[i] + ' '
                last = ''
        [print(r.rjust(self.length, ' ')) for r in result]






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

    leftparagraph = RightParagraph(23)

    leftparagraph.add('Multiply noise and joy')
    leftparagraph.add('Sing songs in a good hour')
    leftparagraph.add('Friendship grace and youth')
    leftparagraph.add('Our birthday girls')
    leftparagraph.end()