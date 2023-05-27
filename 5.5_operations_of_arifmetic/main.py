#1
"""

Класс FoodInfo
Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

proteins — количество белков в граммах
fats — количество жиров в граммах
carbohydrates — количество углеводов в граммах
Экземпляр класса FoodInfo должен иметь следующее формальное строковое представление:

FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.

Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью операторов *, / и // соответственно:

результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого умножены на n
результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены на n
результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены нацело на n
Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса FoodInfo всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса FoodInfo нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)
Sample Output 1:

FoodInfo(20, 30, 50)
FoodInfo(20, 40, 60)
FoodInfo(5.0, 10.0, 15.0)
FoodInfo(5, 10, 15)
Sample Input 2:

food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
Sample Output 2:

Некорректный тип данных

"""
class FoodInfo:

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self,other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, other):
        if type(other) in (int, float):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __truediv__(self, other):
        if type(other) in (int, float) and other != 0:
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if type(other) in (int, float) and other != 0:
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented



#2
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
Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса Vector, координата по оси 
�
x которого равна сумме координат по оси 
�
x исходных векторов, координата по оси 
�
y — сумме координат по оси 
�
y исходных векторов
результатом вычитания должен являться новый экземпляр класса Vector координата по оси 
�
x которого равна разности координат по оси 
�
x исходных векторов с учетом порядка, координата по оси 
�
y — разности координат по оси 
�
y исходных векторов с учетом порядка
Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с помощью операторов * и / соответственно:

результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены на n
результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены на n
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как вектор на число, так и число на вектор.

Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса Vector всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

a = Vector(1, 2)
b = Vector(3, 4)

print(a + b)
print(a - b)
print(b + a)
print(b - a)
Sample Output 1:

Vector(4, 6)
Vector(-2, -2)
Vector(4, 6)
Vector(2, 2)
Sample Input 2:

a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)
Sample Output 2:

Vector(6, 8)
Vector(6, 8)
Vector(1.5, 2.0)

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float) and other != 0:
            return Vector(self.x / other, self.y / other)
        return NotImplemented

#3
"""

Класс SuperString
Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:

string — значение строки
Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:

<значение строки>
Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.

Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:

результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n
результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.

Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)
Sample Output 1:

beegeek
geekbee
Sample Input 2:

s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)
Sample Output 2:

beegeekbeegeek
beegeekbeegeekbeegeek
be
Sample Input 3:

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)
Sample Output 3:

bee
geek

"""

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if type(other) == int:
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == int:
            m = len(self.string)
            result = (m // other)
            return SuperString(self.string[:result])
        return NotImplemented

    def __lshift__(self, other):
        if type(other) == int:
            if other > len(self.string):
                return SuperString('')
            elif other == 0:
                return SuperString(self.string)
            return SuperString(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if type(other) == int:
            if other > len(self.string):
                return SuperString('')
            elif other == 0:
                return SuperString(self.string)
            return SuperString(self.string[other:])
        return NotImplemented

#4
"""

Класс Time
Реализуйте класс Time, описывающий время на цифровых часах. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
Экземпляр класса Time должен иметь следующее неформальное строковое представление:

<количество часов в формате HH>:<количество минут в формате MM>
Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:

результатом сложения с помощью оператора + должен являться новый экземпляр класса Time, количество часов которого равно сумме часов исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
результатом сложения с помощью оператора += должен являться левый экземпляр класса Time, количество часов которого увеличено на количество часов правого экземпляра класса Time, количество минут — на количество минут правого экземпляра класса Time
Примечание 1. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Time нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)
Sample Output 1:

05:40
05:40
Sample Input 2:

time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)
Sample Output 2:

05:40
03:10
Sample Input 3:

time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)
Sample Output 3:

01:20
12:10

"""


class Time:
    def __init__(self, hours, minutes):
        incr = minutes // 60
        if incr > 0:
            self.hours = (incr + hours) % 24
            self.minutes = minutes % 60
        else:
            self.hours = hours % 24
            self.minutes = minutes % 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}'

    def __add__(self, other):
        if isinstance(other, Time):
            hours = self.hours + other.hours
            minutes = self.minutes + other.minutes
            return Time(hours, minutes)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.minutes += other.minutes
            incr = self.minutes // 60
            if incr > 0:
                self.hours += (other.hours + incr)
                self.hours = self.hours % 24
                self.minutes = self.minutes % 60
            else:
                self.hours += (other.hours + incr)
                self.hours = self.hours % 24
                self.minutes = self.minutes % 60
            return self
        return NotImplemented


#5
"""

Класс Queue 🌶️
Очередь — абстрактный тип данных с дисциплиной доступа к элементам "первый пришёл — первый вышел". Добавление элемента возможно лишь в конец очереди, выборка — только из начала очереди, при этом выбранный элемент из очереди удаляется.

Реализуйте класс Queue, описывающий очередь. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является элементом очереди. Порядок следования аргументов образует порядок элементов в очереди, то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так далее.

Класс Queue должен иметь два метода экземпляра:

add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том порядке, в котором они были переданы
pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Если очередь пуста, метод должен вернуть значение None
Экземпляр класса Queue должен иметь следующее неформальное строковое представление:

<первый элемент очереди> -> <второй элемент очереди> -> <третий элемент очереди> -> ...
Помимо этого, экземпляры класса Queue должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две очереди считаются равными, если они имеют равную длину и содержат равные элементы на равных позициях.

Также экземпляры класса Queue должны поддерживать между собой операцию сложения с помощью операторов + и +=:

результатом сложения с помощью оператора + должен являться новый экземпляр класса Queue, представляющий очередь со всеми элементами исходных очередей: сначала все элементы левой очереди, затем все элементы правой очереди
результатом сложения с помощью оператора += должен являться левый экземпляр класса Queue, представляющий очередь, к которой добавлены все элементы правой очереди
Наконец, экземпляр класса Queue должен поддерживать операцию побитового сдвига вправо на целое число n с помощью оператора >>, результатом которой должен являться новый экземпляр класса Queue, представляющий исходную очередь без первых n элементов. Если n больше или равно длине исходной очереди, результатом должен являться экземпляр класса Queue, представляющий пустую очередь.

Примечание 1. Если объект, с которым выполняется операция сравнения или арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)
Sample Output 1:

1 -> 2 -> 3 -> 4 -> 5
1
2 -> 3 -> 4 -> 5
Sample Input 2:

queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)
Sample Output 2:

False
True
Sample Input 3:

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)
Sample Output 3:

1 -> 2 -> 3 -> 4 -> 5
Sample Input 4:

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)
Sample Output 4:

1 -> 2 -> 3 -> 4 -> 5
Sample Input 5:

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)
Sample Output 5:

4 -> 5

"""

class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def __str__(self):
        return ' -> '.join([str(el) for el in self.queue])

    def add(self, *args):
        self.queue += list(args)
        return self
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def __eq__(self, other):
        if isinstance(other, Queue):
            return len(self.queue) == len(other.queue) and \
                   all(s == o for s, o in zip(self.queue, other.queue))
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(self.add(*other.queue))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            return self.add(*other.queue)
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n == 0:
                return Queue(*self.queue)
            return Queue(*self.queue[n:])
        return NotImplemented

if __name__ == '__main__':
    # food1 = FoodInfo(10, 20, 30)
    # food2 = FoodInfo(10, 10, 20)
    #
    # print(food1 + food2)
    # print(food1 * 2)
    # print(food1 / 2)
    # print(food1 // 2)
    #
    # s1 = SuperString('bee')
    # s2 = SuperString('geek')
    #
    # print(s1 + s2)
    # print(s2 + s1)
    #
    # s = SuperString('beegeek')
    #
    # print(s << 4)
    # print(s >> 3)

    # INPUT DATA:

    # TEST_1:
    s1 = SuperString('bee')
    s2 = SuperString('geek')

    print(s1 + s2)
    print(s2 + s1)

    # TEST_2:
    s = SuperString('beegeek')

    print(s * 2)
    print(3 * s)
    print(s / 3)

    # TEST_3:
    s = SuperString('beegeek')

    print(s << 4)
    print(s >> 3)

    # TEST_4:
    s = SuperString('beegeek')
    for i in range(9):
        print(f'{s} << {i} =', s << i)

    # TEST_5:
    s = SuperString('beegeek')
    for i in range(9):
        print(f'{s} >> {i} =', s >> i)

    # TEST_6:
    names = ['Карп', 'Фотий', 'Любосмысл', 'Клавдия', 'Милован', 'Светлана', 'Александра', 'Ираида', 'Трифон',
             'Добромысл',
             'Евпраксия', 'Радим', 'Эдуард', 'Аристарх', 'Ульяна', 'Ираклий', 'Юлия', 'Марк', 'Демид', 'Творимир',
             'Орест',
             'Феоктист', 'Тимур', 'Филипп', 'Аверьян', 'Эраст', 'Осип', 'Станислав', 'Адриан', 'Милан', 'Парфен',
             'Велимир',
             'Филимон', 'Ратибор', 'Элеонора', 'Феофан', 'Ирина', 'Кузьма', 'Панфил', 'Венедикт', 'Парамон', 'Влас',
             'Надежда', 'Фрол', 'Мартьян', 'Моисей', 'Леонид', 'Мариан', 'Марина', 'Филарет', 'Валентина', 'Севастьян',
             'Светозар', 'Родион', 'Ростислав', 'Капитон', 'Герман', 'Геннадий', 'Иосиф', 'Гостомысл', 'Епифан',
             'Гордей',
             'Ферапонт', 'Януарий', 'Денис', 'Галина', 'Аггей', 'Харлампий', 'Акулина', 'Климент', 'Автоном', 'Никанор',
             'Фортунат', 'Сила', 'Федосий', 'Виктор', 'Арсений', 'Дементий', 'Спартак', 'Евгений', 'Феликс', 'Ананий',
             'Нинель', 'Стоян', 'Остромир', 'Никифор', 'Клавдий', 'Чеслав', 'Афанасий', 'Наум', 'Рубен', 'Азарий',
             'Виктория', 'Синклитикия', 'Тимофей', 'Фёкла', 'Нонна', 'Ким', 'София']

    for name in names:
        person = SuperString(name)
        print(person * 2, 2 * person, person / 2)

    # TEST_7:
    s = SuperString('beegeek')
    for i in range(1, 9):
        print(f'{s} / {i} =', s / i)

    # TEST_8:
    superstring = SuperString('bee')
    print(superstring.__add__([]))
    print(superstring.__mul__(()))
    print(superstring.__truediv__({}))
    print(superstring.__lshift__(set()))
    print(superstring.__rshift__('geek'))

    # TEST_8:
    t = Time(22, 0)
    t += Time(3, 0)
    print(t)

    # TEST_7:
    queue = Queue(*'beegeek')
    for i in range(9):
        print(f'Queue >> {i} =', queue >> i)