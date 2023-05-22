#1
"""

Класс Book
Требовалось реализовать класс Book, описывающий книгу. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:

title — название книги
author — автор книги
year — год выпуска книги
Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:

Book('<название книги>', '<автор книги>', <год выпуска книги>)
И следующее неформальное строковое представление:

<название книги> (<автор книги>, <год выпуска книги>)
Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте класс Book правильно.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Book нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

book = Book('Изучаем Python', 'Марк Лутц', 2021)

print(book)
print(repr(book))
Sample Output 1:

Изучаем Python (Марк Лутц, 2021)
Book('Изучаем Python', 'Марк Лутц', 2021)
Sample Input 2:

book = Book('Программируем на Python', 'Майкл Доусон', 2023)

print(str(book))
print(repr(book))
Sample Output 2:

Программируем на Python (Майкл Доусон, 2023)
Book('Программируем на Python', 'Майкл Доусон', 2023)

"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


#2
"""

Класс Rectangle
Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:

Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Rectangle нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

rectangle = Rectangle(1, 2)

print(str(rectangle))
print(repr(rectangle))
Sample Output 1:

Rectangle(1, 2)
Rectangle(1, 2)
Sample Input 2:

rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)

print(rectangle1)
print(repr(rectangle2))
Sample Output 2:

Rectangle(1, 2)
Rectangle(3, 4)

"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


if __name__ == '__main__':
    book = Book('Изучаем Python', 'Марк Лутц', 2021)

    print(book)
    print(repr(book))

    rectangle = Rectangle(1, 2)

    print(str(rectangle))
    print(repr(rectangle))