#1
"""

Контекстный менеджер make_tag
Реализуйте контекстный менеджер make_tag с помощью декоратора @contextmanager, который принимает один аргумент:

tag — произвольная строка
Контекстный менеджер должен выводить строку tag при входе в блок with и после выхода из блока with.

Примечание 1. Наглядные примеры использования контекстного менеджера make_tag продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

with make_tag('---'):
    print('Поколение Python')
Sample Output:

---
Поколение Python
---

"""

from contextlib import contextmanager


@contextmanager
def make_tag(tag: str):
    print(tag)
    yield   
    print(tag)


#2
"""

Контекстный менеджер reversed_print
Реализуйте контекстный менеджер reversed_print с помощью декоратора @contextmanager, который не принимает никаких аргументов.

Контекстный менеджер reversed_print должен позволять выполнять все операции записи в стандартный поток вывода sys.stdout внутри блока with в обратном порядке.

Примечание 1. Наглядные примеры использования класса reversed_print продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')
Sample Output 1:

Вывод вне блока with
htiw аколб иртунв довыВ
Вывод вне блока with
Sample Input 2:

with reversed_print():
    print('python')
    print('beegeek')

print('Вывод вне блока with')
Sample Output 2:

nohtyp
keegeeb
Вывод вне блока with
Sample Input 3:

print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with reversed_print():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
Sample Output 3:

Если жизнь одаривает вас лимонами — не делайте лимонад
Заставьте жизнь забрать их обратно!
!ыномил еытялкорп иовт ынжун ен енМ
?ьталед имин с енм отЧ
Требуйте встречи с менеджером, отвечающим за жизнь!

"""
from contextlib import contextmanager
import sys

@contextmanager
def reversed_print():
    try:
        s = sys.stdout.write
        sys.stdout.write = lambda x: s(x[::-1])
        yield
    finally:
        sys.stdout.write = s

#3
"""

Контекстный менеджер safe_write
Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:

filename — имя файла
Контекстный менеджер должен открывать файл с именем filename в режиме w и позволять выполнять с ним соответствующие операции. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:

Во время записи в файл было возбуждено исключение <тип исключения>
Примечание 1. Наглядные примеры использования контекстного менеджера safe_write продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный контекстный менеджер используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью')
    
with open('undertale.txt') as file:
    print(file.read())
Sample Output 1:

Тень от руин нависает над вами, наполняя вас решительностью
Sample Input 2:

with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
    
with safe_write('undertale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('undertale.txt') as file:
    print(file.read())
Sample Output 2:

Во время записи в файл было возбуждено исключение ValueError
Тень от руин нависает над вами, наполняя вас решительностью

"""


from contextlib import contextmanager
import sys

@contextmanager
def safe_write(filename):
    lst = []
    try:
        file = open(filename, 'w')
        yield file
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")
        
    finally:
        if file:
            file.close()
        


if __name__ == '__main__':
    with make_tag('---'):
        print('Поколение Python')




    print('Вывод вне блока with')
    with reversed_print():
        print('Вывод внутри блока with')

    print('Вывод вне блока with')


    with safe_write('undertale.txt') as file:
        file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
        
    with safe_write('undertale.txt') as file:
        print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
        raise ValueError

    with open('undertale.txt') as file:
        print(file.read())