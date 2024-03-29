"""
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub

"""

class CaesarCipher:
    LENGTH = 26
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, shift):
        self.shift = shift

    def encode(self, string):
        result = ''
        for ch in string:
            if ch in self.upper_alpha or ch in self.lower_alpha:
                if ch.islower():
                    result += self.lower_alpha[(self.lower_alpha.find(ch)+self.shift) % self.LENGTH]
                elif ch.isupper():
                    result += self.upper_alpha[(self.upper_alpha.find(ch)+self.shift) % self.LENGTH]
            else:
                result += ch
        return result
    
    def decode(self, string):
        result = ''
        for ch in string:
            if ch in self.upper_alpha or ch in self.lower_alpha:
                if ch.islower():
                    result += self.lower_alpha[self.lower_alpha.find(ch)-self.shift]
                elif ch.isupper():
                    result += self.upper_alpha[self.upper_alpha.find(ch)-self.shift]
            else:
                result += ch
        return result
    

"""
Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.

Примечание. Тестовые данные доступны по ссылкам:

"""
from abc import ABC, abstractmethod

class Progression(ABC):
    def __init__(self, first, step):
        self.first = first
        self.step = step

    def __iter__(self):
        return self
    
    @abstractmethod
    def __next__(self):
        pass



class ArithmeticProgression(Progression):
    def __next__(self):
        it = self.first
        self.first += self.step
        return it

class GeometricProgression(Progression):
    def __next__(self):
        it = self.first
        self.first *= self.step
        return it

"""
Классы Domain и DomainException
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса from_url() и from_email():

domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты должно быть возбуждено исключение DomainException с текстом:

Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:

print(str(domain1))                                # pygen.ru
print(str(domain2))                                # pygen.ru
print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует точка, а затем снова одна или более латинских букв.

Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой следует корректный домен. 

Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной или более латинских букв, за которой следует собачка (@), а затем корректный домен.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub

"""
import re

class DomainException(Exception):
    pass

class Domain:
    PATTERN = r'(?:http[s]?://|[a-zA-Z_]+@)?'
    FIND_MAIL_PATTERN = r'^[a-zA-Z_]+@\w+\.\w+$'
    FIND_URL_PATTERN = r'^(?:(?:http[s]?://[a-zA-Z_]+\.\w+)|(?:[a-zA-Z_]+\.\w+))$'
    
    def __init__(self, domain):
        if self.check_option(self.FIND_URL_PATTERN, domain):
            self.domain = re.sub(self.PATTERN, '', domain)
        elif self.check_option(self.FIND_MAIL_PATTERN, domain):
            self.domain = re.sub(self.PATTERN, '', domain)

    @classmethod
    def from_url(cls, url):
        if cls.check_option(cls.FIND_URL_PATTERN, url):
            return cls(re.sub(Domain.PATTERN, '', url))
                  
    @classmethod
    def from_email(cls, mail):
        if cls.check_option(cls.FIND_MAIL_PATTERN, mail):
            return cls(re.sub(cls.PATTERN, '', mail))
    
    @staticmethod    
    def check_option(pattern, domain):
        if re.findall(pattern, domain):
            return True
        raise DomainException('Недопустимый домен, url или email')

    def __str__(self):
        return self.domain



"""
Класс HighScoreTable
Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество баллов в зависимости от своего результата. Вашей задачей является реализация класса HighScoreTable — таблицы рекордов, которую можно будет обновлять с учетом итоговых результатов игрока.

Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:

high_score_table = HighScoreTable(3)
Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:

print(high_score_table.scores)    # []
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)    # [12, 10, 8]
Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды, то после заполнения таблицы добавляться должны только те результаты, которые лучше текущих:

high_score_table.update(6)
high_score_table.update(7)
print(high_score_table.scores)    # [12, 10, 8]
high_score_table.update(9)
print(high_score_table.scores)    # [12, 10, 9]
Таблица должна поддерживать сброс всех результатов:

high_score_table.reset()
print(high_score_table.scores)    # []
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub

"""

class HighScoreTable:
    def __init__(self, limit):
        self.limit = limit
        self.scores = []

    def update(self, score):
        self.scores = sorted(self.scores + [score], reverse=True)[:self.limit]

    def reset(self):
        self.scores = []


"""
Класс Pagination
Реализуйте класс Pagination для обработки данных с разбивкой по страницам. Разбивка по страницам используется для разделения большого количества данных на части. Экземпляр класса Pagination должен создаваться на основе двух значений:

исходные данные, представленные в виде списка с произвольными элементами
размер страницы, то есть количество элементов, отображаемых на каждой странице
alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
Для получения содержимого страницы должен использоваться метод get_visible_items():

print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
Обратите внимание, содержимое страницы должно быть представлено в виде списка. Перемещение по страницам должно происходить с помощью следующих методов:

prev_page() — вернуться к предыдущей странице
next_page() — перейти к следующей странице
first_page() — вернуться к первой странице
last_page() — перейти к последней странице
go_to_page() — перейти к странице с указанным номером (1 — первая страница, 2 — вторая страница, и так далее)
pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']
Методы для перемещения по страницам должны быть применимы друг за другом:

pagination.first_page()
pagination.next_page().next_page()   
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']
С помощью атрибутов total_pages и current_page должна быть возможность получить общее количество страниц и текущую страницу соответственно:

print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3
При нахождении на первой странице и перемещении к предыдущей странице, текущей страницей должна остаться первая страница. Аналогично при нахождении на последней странице и перемещении к следующей странице, текущей страницей должна остаться последняя страница:

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']
При перемещении к нулевой или менее странице, текущей страницей должна стать первая страница. Аналогично при перемещении к странице, номер которой превышает общее количество страниц, текущей страницей должна стать последняя страница:

pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub

"""    

class Pagination:
    

    def __init__(self, text, size):
        self.total_pages = len(text) // size + 1 if len(text) % size else len(text) // size
        self.matrix = [text[size*i:size*(i+1)] for i in range(self.total_pages)]
        self.current_page = 1

    def get_visible_items(self):
        return self.matrix[self.current_page-1]
    
    def next_page(self):
        if self.current_page + 1 < self.total_pages-1:
            self.current_page += 1
        return self

    def prev_page(self):
        if self.current_page - 1 > 0:
            self.current_page -= 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = len(self.matrix)
        return self

    def go_to_page(self, num):
        if num - 1 > self.total_pages: self.current_page = len(self.matrix)
        elif num - 1 < 0: self.current_page = 1
        else: self.current_page = num
        return self


"""
Классы Testpaper и Student
В этой задаче вам необходимо реализовать класс Testpaper, который позволит составлять экзаменационные тесты. Каждый тест должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений:

testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
Созданные тесты должны сдаваться студентом — экземпляром класса Student. Он должен иметь метод take_test(), который принимает в качестве аргументов тест и ответы студента на этот тест:

student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
Результаты тестов должны быть доступны в виде словаря, ключом в котором является тема теста, а значением — результат теста (сдан или не сдан) и процент верных решений:

print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}
Если студент еще не сдал ни одного теста, атрибут tests_taken должен содержать строку No tests taken:

student3 = Student()

print(student3.tests_taken)    # No tests taken
Примечание 1. Округление процента верных решений должно происходить до ближайшего целого числа.

Примечание 2. Тестовые данные доступны по ссылкам:

"""
from dataclasses import dataclass


@dataclass
class Testpaper:
    title: str
    answers: list
    min_persents: str

class Student:
    def __init__(self):
        self.tests = {}

    def take_test(self, testpaper, answers):
        bals = round((sum(a == b for a, b in zip(answers, testpaper.answers))/len(testpaper.answers)) * 100)
        results = (f'Failed! ({bals}%)', f'Passed! ({bals}%)')
        self.tests |= {testpaper.title: results[bals >= int(testpaper.min_persents[:-1])]}

    @property
    def tests_taken(self):
        return self.tests if self.tests else 'No tests taken'


    
"""
Класс TicTacToe
Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, ставящий крестики:

tictactoe = TicTacToe()

tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)
Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:

tictactoe.mark(1, 1)         # Недоступная клетка

tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)
С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:

символ X, если победил игрок, ставящий крестики
символ O, если победил игрок, ставящий нолики
строку Ничья, если произошла ничья
значение None, если победитель еще не определен
print(tictactoe.winner())    # X
Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:

tictactoe.mark(2, 1)         # Игра окончена
С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов tictactoe.show() должен вывести следующее:

X|O|X
-----
 |O|X
-----
O| |X
Примечание. Тестовые данные доступны по ссылкам:

"""

class TicTacToe:
    X = "X"
    O = "O"

    def __init__(self):
        self.pole = [["" for _ in range(3)] for _ in range(3)]
        self.move = 1

    def mark(self, row, col):
        if not self.pole[row-1][col-1] and self.winner() is None:
            self.pole[row-1][col-1] = (self.O, self.X)[self.move % 2]
            self.move += 1
        elif self.winner():
            print("Игра окончена")
        else:
            print('Недоступная клетка')

    def show(self):
        print('\n-----\n'.join(['|'.join([col if col else ' ' for col in row]) for row in self.pole]))

    def winner(self):
        if any([all(el == self.X for el in row) for row in self.pole]) or\
        any([all(self.pole[j][i] == self.X for j in range(3)) for i in range(3)]) or \
        all(self.pole[i][i] == self.O for i in range(3)) or \
        all(self.pole[i][i] == self.X for i in range(2, -1, -1)):
            return self.X
        elif any([all(el == self.O for el in row) for row in self.pole]) or\
        any([all(self.pole[j][i] == self.O for j in range(3)) for i in range(3)]) or \
        all(self.pole[i][i] == self.O for i in range(3)) or \
        all(self.pole[i][i] == self.O for i in range(2, -1, -1)):
            return self.O
        elif all([all(bool(el) for el in row) for row in self.pole]):
            return "Ничья"


"""
Классы Game и Cell
В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух классов Game и Cell. Экземпляр первого класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен создаваться на основе трех значений: количество строк (длина поля), количество столбцов (ширина поля) и общее количество мин на поле:

game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин
Количество строк и столбцов, а также общее количество мин должны быть доступны по соответствующим атрибутам:

print(game.rows)           # 14
print(game.cols)           # 18
print(game.mines)          # 40
Также экземпляр класса Game должен иметь атрибут board, представляющий игровое поле в виде двумерного списка. Количество подсписков в этом списке должно совпадать с количеством строк, количество элементов в подсписках — с количеством столбцов. Каждый элемент подсписка должен представлять собой экземпляр класса Cell и иметь соответствующий набор атрибутов:

cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках
Игровое поле при создании должно заполняться минами случайным образом.

Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное количество мин в соседних ячейках, в одном из тестов мы используем собственную функцию get_neighbours_count(), которая считает это количество.

Примечание 2. Тестовые данные доступны по ссылкам:
"""







    # Напишите определение классов Product и ShoppingCart 
from dataclasses import dataclass, field

@dataclass(order=True)
class Product:
    name: str
    price: float = field(compare=False)

class ShoppingCart:
    def __init__(self):
        self._items = []
        self.__total_price = 0
    
    @property
    def items(self):
        return sorted(self._items, key=lambda x: (x.price, x.name))
    
    @property
    def total_price(self):
        return sum([x.price for x in self._items])
    
    
    def add_item(self, item):
        self._items.append(item)
        
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError
    
    def __len__(self):
        return len(self.items)







if __name__ == '__main__':
    cipher = CaesarCipher(10)

    words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
            'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
            'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
            'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
            'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
            'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
            'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
            'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
            'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

    encode_words = [cipher.encode(word) for word in words]
    print(encode_words)

    decode_words = [cipher.decode(word) for word in encode_words]
    print(decode_words)


    # progression = ArithmeticProgression(0, 1)

    # for elem in progression:
    #     if elem > 10:
    #         break
    #     print(elem, end=' ')


    # progression = GeometricProgression(1, 2)

    # for elem in progression:
    #     if elem > 10:
    #         break
    #     print(elem, end=' ')

    domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
    domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
    domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты

    print(type(domain1))
    print(type(domain2))
    print(type(domain3))



    high_score_table = HighScoreTable(3)

    print(high_score_table.scores)
    high_score_table.update(10)
    high_score_table.update(8)
    high_score_table.update(12)
    print(high_score_table.scores)

    high_score_table.update(18)
    high_score_table.update(11)
    high_score_table.update(13)
    print(high_score_table.scores)


    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    pagination = Pagination(alphabet, 4)
    pagination.go_to_page(-100)
    print(pagination.get_visible_items())

    pagination.go_to_page(100)
    print(pagination.get_visible_items())


    paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
    paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
    paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

    student = Student()

    print(student.tests_taken)


        


    apple = Product("Apple", 1.5)
    banana = Product("Banana", 0.75)
    chocolate = Product("Chocolate", 2.99)

    cart = ShoppingCart()
    cart.add_item(banana)
    cart.add_item(apple)
    cart.add_item(chocolate)

    assert len(cart) == 3
    assert cart.items == [banana, apple, chocolate]

    milk = Product('Milk', 1)
    cart.add_item(milk)
    assert cart.items == [banana, milk, apple, chocolate]
    print("Items in the cart:", [item.name for item in cart.items])
    print("Total price:", cart.total_price)
    assert cart.total_price == 6.24
    cart.add_item(banana)
    assert len(cart) == 5
    assert cart.total_price == 6.99
    cart.remove_item(milk)
    assert len(cart) == 4
    cart.remove_item(banana)
    cart.remove_item(banana)
    assert len(cart) == 2
    try:
        cart.remove_item(banana)
    except ValueError:
        pass


    tictactoe = TicTacToe()

    tictactoe.mark(1, 1)
    tictactoe.mark(3, 2)
    tictactoe.mark(1, 1)

    tictactoe.mark(1, 3)
    tictactoe.mark(1, 2)
    tictactoe.mark(3, 3)
    tictactoe.mark(2, 2)
    tictactoe.mark(2, 3)

    print(tictactoe.winner())
    tictactoe.show()