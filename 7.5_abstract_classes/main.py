#1
"""
Классы Average, Median и Harmonic
Вам доступны классы Average, Median и Harmonic, имеющие сходный интерфейс. Все три класса используются для обработки пользовательских оценок и оценок критиков некоторого медиаконтента по стобалльной шкале и вычисления средних значений этих оценок. Задачей класса Average является нахождение среднего арифметического пользовательских оценок или оценок критиков, классов Median и Harmonic — медианы и среднего гармонического соответственно.

Изучите приведенные классы, реализуйте абстрактный базовый класс Middle и постройте корректную схему наследования. При выполнении старайтесь избегать дублирования кода.

Примечание 1. Функционал классов Average, Median и Harmonic должен остаться прежним, необходимо лишь объединить их в иерархию, определив для них единый базовый абстрактный класс Middle.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
average = Average(user_votes, expert_votes)

print(average.get_correct_user_votes())
print(average.get_correct_expert_votes())
print(average.get_average())
print(average.get_average(False))
Sample Output 1:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
66.75
78.75
Sample Input 2:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
median = Median(user_votes, expert_votes)

print(median.get_correct_user_votes())
print(median.get_correct_expert_votes())
print(median.get_average())
print(median.get_average(False))
Sample Output 2:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
71
81
Sample Input 3:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
harmonic = Harmonic(user_votes, expert_votes)

print(harmonic.get_correct_user_votes())
print(harmonic.get_correct_expert_votes())
print(round(harmonic.get_average(), 2))
print(round(harmonic.get_average(False), 2))
Sample Output 3:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
65.46
77.92

"""
from abc import ABC, abstractmethod
class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self, to_sort=False):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.user_votes if 10 < vote < 90]
        return sorted(votes) if to_sort else votes

    def get_correct_expert_votes(self, to_sort=False):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.expert_votes if 5 < vote < 95]
        return sorted(votes) if to_sort else votes
    
    @abstractmethod
    def get_average(self, users=True, to_sort=False):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes(to_sort)
        else:
            votes = self.get_correct_expert_votes(to_sort)
        return votes  

class Average(Middle):
    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return sum(votes) / len(votes)

class Median(Middle):
    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users, to_sort=True)
        return votes[len(votes) // 2]

class Harmonic(Middle):
    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))
    

#2
"""

Классы ChessPiece, King и Knight
1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. Инициализатор класса должен принимать два аргумента в следующем порядке:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
Класс ChessPiece должен иметь один метод экземпляра:

can_move() — пустой абстрактный метод
2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля. Процесс создания экземпляра класса King должен совпадать с процессом создания экземпляра класса ChessPiece.

Класс King должен иметь один метод экземпляра:

can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, или False в противном случае
Экземпляр класса King  должен иметь два атрибута:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня. Процесс создания экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.

Класс Knight должен иметь один метод экземпляра:

can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, и False в противном случае
Экземпляр класса Knight  должен иметь два атрибута:

horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
Примечание 1. Шахматная доска имеет вид:

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))
Sample Output:

True
True
False

"""
from abc import ABC, abstractmethod
class ChessPiece(ABC):
    hor_coords = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    vert_coords = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}      
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
    
    @abstractmethod
    def can_move(self, horizontal_to, vertical_to):
        raise NotImplementedError
    
class King(ChessPiece):
    def can_move(self, horizontal_to, vertical_to):
        return (self.hor_coords[self.horizontal] - self.hor_coords[horizontal_to] in (1, -1) and\
              self.vert_coords[self.vertical] - self.vert_coords[vertical_to] == 0) or\
            (self.vert_coords[self.vertical] - self.vert_coords[vertical_to] in (1, -1) and\
            self.hor_coords[self.horizontal] - self.hor_coords[horizontal_to] == 0) or\
            (self.vert_coords[self.vertical] - self.vert_coords[vertical_to] in (1, -1) and\
            self.hor_coords[self.horizontal] - self.hor_coords[horizontal_to] in (1, -1))
    
class Knight(ChessPiece):
    def can_move(self, horizontal_to, vertical_to):
        return (self.hor_coords[horizontal_to] - self.hor_coords[self.horizontal]) ** 2\
              + (self.vert_coords[vertical_to] - self.vert_coords[self.vertical]) ** 2 == 5


from collections.abc import *
print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Iterator))
print(isinstance([1, 2, 3], Reversible))
print(isinstance([1, 2, 3], Collection))
print(isinstance([1, 2, 3], Sequence))
print(isinstance([1, 2, 3], MutableSequence))
print(isinstance([1, 2, 3], Mapping))
print(isinstance([1, 2, 3], MutableMapping))



if __name__ == '__main__':
    user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
    expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
    average = Average(user_votes, expert_votes)

    print(average.get_correct_user_votes())
    print(average.get_correct_expert_votes())
    print(average.get_average())
    print(average.get_average(False))

    king = King('b', 2)

    print(king.can_move('c', 3))
    print(king.can_move('a', 1))
    print(king.can_move('f', 7))
    print('____________________')

    from collections.abc import *
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance([1, 2, 3], Iterator))
    print(isinstance([1, 2, 3], Reversible))
    print(isinstance([1, 2, 3], Collection))
    print(isinstance([1, 2, 3], Sequence))
    print(isinstance([1, 2, 3], MutableSequence))
    print(isinstance([1, 2, 3], Mapping))
    print(isinstance([1, 2, 3], MutableMapping))

    print('____________________')

    from collections.abc import *
    print(isinstance({1, 2, 3}, Iterable))
    print(isinstance({1, 2, 3}, Iterator))
    print(isinstance({1, 2, 3}, Reversible))
    print(isinstance({1, 2, 3}, Collection))
    print(isinstance({1, 2, 3}, Sequence))
    print(isinstance({1, 2, 3}, MutableSequence))
    print(isinstance({1, 2, 3}, Set))
    print(isinstance({1, 2, 3}, MutableSet))


    print('____________________')

    from collections.abc import *
    print(isinstance({'one': 1, 'two': 2}, Iterable))
    print(isinstance({'one': 1, 'two': 2}, Iterator))
    print(isinstance({'one': 1, 'two': 2}, Reversible))
    print(isinstance({'one': 1, 'two': 2}, Collection))
    print(isinstance({'one': 1, 'two': 2}, Sequence))
    print(isinstance({'one': 1, 'two': 2}, MutableSequence))
    print(isinstance({'one': 1, 'two': 2}, Mapping))
    print(isinstance({'one': 1, 'two': 2}, MutableMapping))

    print('____________________')
    reversed('123')
    reversed((1, 2, 3))
    reversed([1, 2, 3])
    reversed({'one': 1, 'two': 2})

    print('____________________')
    from collections.abc import *

    obj = range(10)

    print(isinstance(obj, Sequence))
    print(isinstance(obj, MutableSequence))