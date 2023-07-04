#1
"""

Класс SuppressAll
Требовалось реализовать класс SuppressAll. При создании экземпляра класс не должен был принимать никаких аргументов.

Предполагалось, что экземпляр класса SuppressAll будет являться контекстным менеджером, подавляющим любое исключение, которое возбуждается во время выполнения кода внутри блока with.

Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте класс SuppressAll правильно.

Примечание 1. Наглядные примеры использования класса SuppressAll продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс SuppressAll должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print('start')

with SuppressAll():
    print('Python generation!')
    raise ValueError

print('end')
Sample Output 1:

start
Python generation!
end
Sample Input 2:

print('start')

with SuppressAll():
    print('Python generation!')

print('end')
Sample Output 2:

start
Python generation!
end

"""


class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return bool(exc_value)
    

#2
"""

Класс Greeter
Реализуйте класс Greeter. При создании экземпляра класс должен принимать один аргумент:

name — имя пользователя
Экземпляр класса Greeter должен иметь один атрибут:

name — имя пользователя
Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name перед выполнением блока with и выводит текст:

Приветствую, <имя пользователя>!
а также прощается с ним после выполнения блока with и выводит текст:

До встречи, <имя пользователя>!
Примечание 1. Наглядные примеры использования класса Greeter продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Greeter должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

with Greeter('Кейв'):
    print('...')
Sample Output 1:

Приветствую, Кейв!
...
До встречи, Кейв!
Sample Input 2:

with Greeter('Кейв') as greeter:
    print(greeter.name)
Sample Output 2:

Приветствую, Кейв!
Кейв
До встречи, Кейв!

"""
class Greeter:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')
        return True
    

#3
"""

Класс Closer
Реализуйте класс Closer. При создании экземпляра класс должен принимать один аргумент:

obj — произвольный объект
Экземпляр класса Closer должен являться контекстным менеджером, который закрывает используемый объект obj с помощью метода close() после выполнения кода внутри блока with. Если объект не поддерживает операцию закрытия, контекстный менеджер должен вывести:

Незакрываемый объект
Примечание 1. Наглядные примеры использования класса Closer продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Closer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

output = open('output.txt', 'w', encoding='utf-8')

with Closer(output) as file:
    print(file.closed)
    
print(file.closed)
Sample Output 1:

False
True
Sample Input 2:

with Closer(5) as i:
    i += 1
    
print(i)
Sample Output 2:

Незакрываемый объект
6

"""

class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj
    
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.obj.close()
            return False
        except:
            print('Незакрываемый объект')
            return True
        


#4
"""

Класс ReadableTextFile
Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:

filename — имя текстового файла
Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце. Также контекстный менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile('glados_quotes.txt') as file:
    for line in file:
        print(line)
Sample Output 1:

Только посмотрите!
Как величаво она парит в воздухе
Как орел
На воздушном шаре
Sample Input 2:

with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)
Sample Output 2:

Я кашлянул в звенящей тишине,
И от шального эха стало жутко…
Расскажет ли утятам обо мне
под утро мной испуганная утка?

"""

class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.filename = open(self.filename, 'r' ,encoding='utf-8')
        return (line.rstrip() for line in self.filename.readlines())

    def __exit__(self, *args, **kwargs):
        self.filename.close()
        return True

#5
"""

Класс Reloopable
Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:

file — открытый на чтение файловый объект
Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый объект после выполнения кода внутри блока with.

Примечание 1. Наглядные примеры использования класса Reloopable продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Reloopable должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

with open('file.txt', 'w') as file:
    file.write('Evil is evil\n')
    file.write('Lesser, greater, middling\n')
    file.write('Makes no difference\n')
    
with Reloopable(open('file.txt')) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())
Sample Output 1:

Evil is evil
Lesser, greater, middling
Makes no difference
Evil is evil
Lesser, greater, middling
Makes no difference
Sample Input 2:

with open('file.txt', 'w') as file:
    pass
    
file = open('file.txt')
print(file.closed)

with Reloopable(file) as reloopable:
    pass

print(file.closed)
Sample Output 2:

False
True

"""
class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return [line.rstrip() for line in self.file.readlines()]

    def __exit__(self, *args, **kwargs):
        self.file.close()

#6
"""

Класс UpperPrint
Реализуйте класс UpperPrint. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса UpperPrint должен являться контекстным менеджером, который внутри блока with позволяет выполнять все операции записи в стандартный поток вывода sys.stdout в верхнем регистре.

Примечание 1. Наглядные примеры использования класса UpperPrint продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс UpperPrint должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
Sample Output 1:

Если жизнь одаривает вас лимонами — не делайте лимонад
Заставьте жизнь забрать их обратно!
МНЕ НЕ НУЖНЫ ТВОИ ПРОКЛЯТЫЕ ЛИМОНЫ!
ЧТО МНЕ С НИМИ ДЕЛАТЬ?
Требуйте встречи с менеджером, отвечающим за жизнь!
Sample Input 2:

with UpperPrint():
    print('Bee', 'Geek', 'Love', sep=' one ', end=' end')
Sample Output 2:

BEE ONE GEEK ONE LOVE END

"""

import sys
class UpperPrint:
    def printUpper(self, *args, **kwargs):
        self.d(*tuple(i.upper() for i in args))


    def __enter__(self):
        self.d = sys.stdout.write
        sys.stdout.write = self.printUpper

    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.d

#7
"""

Класс Suppress
Реализуйте класс Suppress. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых представляет собой тип исключения.

Экземпляр класса Suppress должен являться контекстным менеджером, подавляющим исключение, если оно возбуждается во время выполнения кода внутри блока with. Подавляться должны исключения тех типов, которые были перечислены при создании контекстного менеджера.

Также экземпляр класса Suppress должен иметь один атрибут:

exception — исключение, которое было подавлено контекстным менеджером. Если исключение не было подавлено или код был выполнен без исключений, атрибут должен иметь значение None
Примечание 1. Наглядные примеры использования класса Suppress продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Класс Suppress должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

with Suppress(NameError):
    print('Этой переменной не существует -->', variable)
    
print('Завершение программы')
Sample Output 1:

Завершение программы
Sample Input 2:

with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))
Sample Output 2:

invalid literal for int() with base 10: 'я число'
<class 'ValueError'>
Sample Input 3:

with Suppress() as context:
    print('All success!')

print(context.exception)
Sample Output 3:

All success!
None

"""
class Suppress:
    def __init__(self, *args):
        self.list_exp = list(args)
        self.exception = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.list_exp:
            self.exception = exc_value
        return self.exception

if __name__ == "__main__":
    print('start')

    with SuppressAll():
        print('Python generation!')
        raise ValueError

    print('end')


    with Greeter('Кейв') as greeter:
        print(greeter.name)


    output = open('output.txt', 'w', encoding='utf-8')

    with Closer(output) as file:
        print(file.closed)
        
    print(file.closed)


    with open('poem.txt', 'w', encoding='utf-8') as file:
        print('Я кашлянул в звенящей тишине,', file=file)
        print('И от шального эха стало жутко…', file=file)
        print('Расскажет ли утятам обо мне', file=file)
        print('под утро мной испуганная утка?', file=file)

    with ReadableTextFile('poem.txt') as file:
        for line in file:
            print(line)

    with open('file.txt', 'w') as file:
        file.write('Evil is evil\n')
        file.write('Lesser, greater, middling\n')
        file.write('Makes no difference\n')
        
    with Reloopable(open('file.txt')) as reloopable:
        for line in reloopable:
            print(line.strip())
        for line in reloopable:
            print(line.strip())


    print('Если жизнь одаривает вас лимонами — не делайте лимонад')
    print('Заставьте жизнь забрать их обратно!')

    with UpperPrint():
        print('Мне не нужны твои проклятые лимоны!')
        print('Что мне с ними делать?')

    print('Требуйте встречи с менеджером, отвечающим за жизнь!')

    with Suppress(TypeError, ValueError) as context:
        number = int('я число')

    print(context.exception)
    print(type(context.exception))
