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