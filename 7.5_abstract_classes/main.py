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
    


"""
Функции is_iterator() и is_iterable()
1. Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимые функции, но не код, вызывающий их.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(is_iterable(123))
print(is_iterable([1, 2, 3]))
print(is_iterable((1, 2, 3)))
print(is_iterable('123'))
print(is_iterable(iter('123')))
print(is_iterable(map(int, '123')))
Sample Output 1:

False
True
True
True
True
True
Sample Input 2:

print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))
Sample Output 2:

False
False
False
False
True
True
"""

def is_iterable(obj):
    return hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')
def is_iterator(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__')


"""
Классы Validator, Number и String
1. Реализуйте абстрактный класс Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является корректным. При создании экземпляра класс не должен принимать никаких аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен сперва проверять его на корректность с помощью метода validate().

Класс Validator должен иметь один абстрактный метод экземпляра:

validate() — пустой метод
2. Также реализуйте класс Number, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является числом из определенного диапазона. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

minvalue — левая граница диапазона, по умолчанию имеет значение None и не ограничивает число слева
maxvalue — правая граница диапазона, по умолчанию имеет значение None и не ограничивает число справа
Класс Number должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу int или float, должно быть возбуждено исключение TypeError с текстом:
Устанавливаемое значение должно быть числом
Если указанный объект является числом меньше minvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть больше или равно <minvalue>
Если указанный объект является числом больше maxvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть меньше или равно <maxvalue>
3. Наконец, реализуйте класс String, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является строкой определенной длины. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

minsize — минимальная длина слова, по умолчанию имеет значение None и не ограничивает минимальную длину
maxsize — максимальная длина слова, по умолчанию имеет значение None и не ограничивает максимальную длину
predicate — функция-предикат для дополнительной валидации, по умолчанию имеет значение None и не используется
Класс String должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу str, метод должен возбуждать исключение TypeError с сообщением:
Устанавливаемое значение должно быть строкой
Если указанный объект является строкой с длиной меньше minsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть больше или равна <minsize>
Если указанный объект является строкой с длиной больше maxsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть меньше или равна <maxsize>
Если указанный объект при передаче в функцию predicate() возвращает False, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемая строка не удовлетворяет дополнительным условиям
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)
Sample Output 1:

19
Sample Input 2:

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)
Sample Output 2:

Устанавливаемое значение должно быть числом
Sample Input 3:

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)
Sample Output 3:

Устанавливаемое число должно быть больше или равно 18
Sample Input 4:

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)
Sample Output 4:

Устанавливаемое число должно быть меньше или равно 99

"""
from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validate(value) is None:
            obj.__dict__[self.attr] = value
        else:
            raise ValueError('Некорректное значение')
    
    @abstractmethod 
    def validate(self, value):
        pass

class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = float('-inf') if minvalue is None else minvalue
        self.maxvalue = float('inf') if maxvalue is None else maxvalue
       
    def validate(self, value):
        if type(value) not in (int, float):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if value < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if value > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")


class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = float('-inf') if minsize is None else minsize
        self.maxsize = float('inf') if maxsize is None else maxsize
        self.predicate = predicate

    def validate(self, value):
        if type(value) != str:
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if len(value) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if len(value) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if self.predicate is not None and not self.predicate(value):
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")

"""

Класс CustomRange
Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 1, 2, 3 и 4.

Реализуйте класс CustomRange, описывающий последовательность, элементами которой являются одиночные целые числа и числа из определенных диапазонов. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является одиночным целым числом либо диапазоном.

При передаче экземпляра класса CustomRange в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса CustomRange в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса CustomRange, расположенные в обратном порядке.

Экземпляр класса CustomRange должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Помимо этого, экземпляр класса CustomRange должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Наконец, экземпляр класса CustomRange должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание 2. Реализация класса CustomRange может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])
Sample Output 1:

1
2
3
8
7
6
Sample Input 2:

customrange = CustomRange(1, '2-5', 3, '1-4')

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)
Sample Output 2:

1 2 3 4 5 3 1 2 3 4
4 3 2 1 3 5 4 3 2 1
10
True
False
Sample Input 3:

customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))
Sample Output 3:

0

"""
from collections.abc import Sequence

class CustomRange(Sequence):
    def __init__(self, *args):
        mut_iterable = self.mutable_iterable(args)
        self.iterable = mut_iterable
    
    @staticmethod
    def mutable_iterable(iterable):
        result = []
        for n in iterable:
            if type(n) == str:
                start, stop = map(int, n.split('-'))
                stop += 1
                result += list(range(start, stop))
            else:
                result += [n]
        return result
    
    def __getitem__(self, key):
        return self.iterable[key]
    
    def __len__(self):
        return len(self.iterable)


"""

Класс BitArray
Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и единицы. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный набор считается пустым
Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:

[<первый элемент битового списка>, <второй элемент битового списка>, ...]
При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса BitArray , расположенные в обратном порядке.

Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.

Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен являться новый экземпляр класса BitArray.

Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:

оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Экземпляр класса BitArray не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса BitArray измениться  не должен.

Примечание 4. Если объект, с которым выполняется логическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 5. Никаких ограничений касательно реализации класса BitArray нет, она может быть произвольной.

Примечание 6. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)
Sample Output 1:

[1, 0, 1, 1]
[0, 1, 0, 0]
1
0
1
True
False
Sample Input 2:

bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))
Sample Output 2:

[1, 0, 1, 1] <class '__main__.BitArray'>
[0, 0, 0, 1] <class '__main__.BitArray'>
[0, 1, 0, 0] <class '__main__.BitArray'>

"""

from collections.abc import Sequence

class BitArray(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self.it = []
            self.iterable = self.it[:]
        else:
            self.it = iterable
            self.iterable = self.it[:]

    def __str__(self):
        return f"[{', '.join([str(n) for n in self.iterable])}]"

    def __getitem__(self, key):
        return self.iterable[key]
    
    def __iter__(self):
        return iter(self.iterable)
    
    def __len__(self):
        return len(self.iterable)
    
    def reversed(self):
        return self.iterable[::-1]
    
    def __invert__(self):
        return BitArray([n-1 if n == 1 else n+1 for n in self.iterable])
    
    def __and__(self, other):
        if isinstance(other, BitArray):
            return BitArray([n1 and n2 for n1, n2 in zip(self.iterable, other.iterable)])
        return NotImplemented
    
    def __or__(self, other):
        if isinstance(other, BitArray):
            return BitArray([n1 or n2 for n1, n2 in zip(self.iterable, other.iterable)])
        return NotImplemented
    

"""
Класс DNA
ДНК состоит из двух цепей, ориентированных азотистыми основаниями друг к другу. В ДНК встречается четыре вида азотистых оснований: аденин (A), гуанин (G), тимин (T) и цитозин (C). Азотистые основания одной из цепей соединены с азотистыми основаниями другой цепи водородными связями согласно принципу комплементарности: аденин (A) соединяется только с тимином (T), гуанин (G) — только с цитозином (C).



Реализуйте класс DNA, описывающий двухцепочную спираль ДНК. При создании экземпляра класс должен принимать один аргумент:

chain — первая цепь ДНК, представляющая собой строку из символов A, G, T и C (азотистых оснований)
Экземпляр класса DNA должен иметь следующее неформальное строковое представление:

<азотистые основания первой цепи ДНК>
При передаче экземпляра класса DNA в функцию len() должно возвращаться количество азотистых оснований в одной из его цепей. При передаче экземпляра класса в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса DNA, расположенные в обратном порядке.

Помимо этого, экземпляр класса DNA должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса DNA должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.

В случае с функцией reversed(), итерацией и доступу по индексам элементы экземпляра класса DNA должны быть представлены в виде кортежей из двух элементов, первым из которых является основание первой цепи ДНК по указанному индексу, вторым — азотистое основание второй цепи ДНК по указанному индексу. Азотистое основание второй цепи ДНК можно получить при помощи принципа комплементарности.

Вдобавок ко всему, экземпляр класса DNA должен поддерживать операцию проверки на принадлежность с помощью оператора in. В данном случае должно проверяться, входит ли азотистое основание в первую цепь ДНК.

Экземпляры класса DNA должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две ДНК считаются равными, если их первые цепи совпадают.

Наконец, экземпляры класса DNA должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса DNA, первой цепью которого является конкатенация первых цепей исходных экземпляров класса DNA.

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание 2. Если объект, с которым выполняется операция сравнения или сложения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса DNA нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])
Sample Output 1:

('A', 'T')
('G', 'C')
('T', 'A')
('C', 'G')
('C', 'G')
('T', 'A')
Sample Input 2:

dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)
Sample Output 2:

AGT
3
True
False
Sample Input 3:

dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))
Sample Output 3:

ACGTTTAAT <class '__main__.DNA'>
TTTAATACG <class '__main__.DNA'>
Sample Input 4:

dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)
Sample Output 4:

False
True
True
False


"""
from collections.abc import Sequence

class DNA(Sequence):
    __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    def __init__(self, chain):
        self.chain = chain

    def __str__(self):
        return self.chain

    def __getitem__(self, key):
        return (self.chain[key], self.__BASE[self.chain[key]])
    
    def __iter__(self):
        return iter([(ch, self.__BASE[ch]) for ch in self.chain])
    
    def __len__(self):
        return len(self.chain)
    
    def reversed(self):
        return self.chain[::-1]
    
    def __contains__(self, value):
        return value in self.chain
    
    def __eq__(self, other):
        if isinstance(other, DNA):
            return all([ch1 == ch2 for ch1, ch2 in zip(self.chain, other.chain)])
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self.chain + other.chain)
        return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, DNA):
            return DNA(other.chain + self.chain)
        return NotImplemented
    
"""

Класс SortedList
Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.

Экземпляр класса SortedList должен иметь следующее формальное строковое представление:

SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.

Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.

Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:

оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:

оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.

Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.

Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 5. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 6. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.

Примечание 7. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)
Sample Output 1:

SortedList([1, 2, 3, 4, 5])
2
4
SortedList([0, 1, 2, 3, 4, 5])
SortedList([0, 1, 2, 3, 5])
SortedList([0, 1, 2, 3, 4, 5, 6])
Sample Input 2:

numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)
Sample Output 2:

5
1 2 3 4 5
True
False
Sample Input 3:

numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)
Sample Output 3:

SortedList([1, 2, 3, 4, 5])
SortedList([1, 1, 3, 3, 5, 5])
SortedList([2, 2, 4, 4])

"""
from collections.abc import Sequence

class SortedList(Sequence):
    def __init__(self, iterable=None):
        if iterable is not None:
            self.iterable = sorted(iterable)
        else:
            self.iterable = []
        self.append = self.extend = self.reverse = self.insert

    def __str__(self):
        return f'SortedList({self.iterable})'

    def __getitem__(self, key):
        return self.iterable[key]
    
    def __len__(self):
        return len(self.iterable)
    
    def __contains__(self, value):
        return super().__contains__(value)
    
    def __setitem__(self, key, val):
        raise NotImplementedError
    
    def __reversed__(self):
        raise NotImplementedError
    
    def __delitem__(self, index):
        del self.iterable[index]
    
    def add(self, val):
        self.iterable = sorted(self.iterable + [val])

    def discard(self, val):
        self.iterable = sorted(filter(lambda x: x != val, self.iterable))

    def update(self, it):
        self.iterable += list(it)
        self.iterable.sort()

    def insert(self, *args):
        raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, SortedList):
            result = self.iterable + other.iterable
            return SortedList(result)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.iterable = sorted(self.iterable + other.iterable)
            return self
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int):
            result = self.iterable * other
            return SortedList(result)
        return NotImplemented
    
    def __imul__(self, other):
        if isinstance(other, int):
            self.iterable = sorted(self.iterable * other)
            return self
        return NotImplemented


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


    class SequenceIterator:
        def __init__(self, iterable):
            self.iterable = iterable
            self.index = 0
            self.flag = True
        def __iter__(self):
            return self
        def __next__(self):
            if self.index >= len(self.iterable):
                if self.flag:
                    self.flag = False
                    self.index = 1
                else:
                    raise StopIteration
            result = self.iterable[self.index]
            self.index += 2
            return result   
            
            


    container = SequenceIterator([1, 5, 4, 6, 43, True, 'hello'])
    for i in container:
        print(i)
    for i in container:
        print(i)


    import json


    # Напишите определение класса AppConfig
    class AppConfig:
        data = None
        @classmethod
        def load_config(cls, name_file):
            with open(name_file) as f:
                cls.data = json.load(f)
        @classmethod
        def get_config(cls, key):
            return cls.data[key]

                
                


    class FibonacciIterator:
        def __init__(self, n):
            self.n = n
            self.index = -1
            self.num_1 = 0
            self.num_2 = 1
            
        def __iter__(self):
            return self
        
        def __next__(self):
            self.index += 1
            result = self.num_1
            if self.index >= self.n:
                raise StopIteration
            if self.num_1 == 0:
                self.num_1, self.num_2 = self.num_2, self.num_1 + self.num_2
                return result
            self.num_1, self.num_2 = self.num_2, self.num_1 + self.num_2
            return result
        
    fibonacci_iter = FibonacciIterator(7)

    for number in fibonacci_iter:
        print(number)


    class Book:
        def __init__(self, title, pages):
            self.title = title
            self.pages = pages


    class Library:
        def __init__(self):
            self.books = []

        def add_book(self, book):
            self.books.append(book)

        def __iter__(self):
            new_lib = []
            for book in self.books:
                new_lib += book.pages
            return LibraryIterator(new_lib) # тут определите, что будете передавать итератору


    class LibraryIterator:
        def __init__(self, book):
            self.book = book
            self.index = 0
              
        def __next__(self):
            curr_index = self.index
            if curr_index >= len(self.book):
                raise StopIteration
            self.index += 1
            return self.book[curr_index]

            


    # Пример использования
    book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
    book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
    book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Используем вложенный итератор для обхода страниц в библиотеке
    for page in library:
        print(page)



    class Student:
        age = Number(18, 99)

    try:
        student = Student()
        student.age = '19'
    except TypeError as error:
        print(error)



    customrange = CustomRange(1, '2-5', 5, '6-8')

    print(customrange[0])
    print(customrange[1])
    print(customrange[2])
    print(customrange[-1])
    print(customrange[-2])
    print(customrange[-3])

    data = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
            0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

    bitarray = BitArray(data)

    print(bitarray)
    data.extend([0, 0, 1, 0, 1, 1])

    print(data)
    print(bitarray)

    dna1 = DNA('ACG')
    dna2 = DNA('TTTAAT')
    dna3 = dna1 + dna2
    dna4 = dna2 + dna1

    print(dna3, type(dna3))
    print(dna4, type(dna4))


    numbers1 = SortedList([1, 3, 5])
    numbers2 = SortedList([2, 4])

    print(numbers1 + numbers2)
    print(numbers1 * 2)
    print(numbers2 * 2)

    numbers = SortedList([1, 2, 3, 4, 5])

    try:
        reversed(numbers)
    except NotImplementedError:
        print('Неподдерживаемая операция')