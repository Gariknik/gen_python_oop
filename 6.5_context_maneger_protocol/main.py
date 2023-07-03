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