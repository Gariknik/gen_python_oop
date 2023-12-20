
"""
Функция get_method_owner()
Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:

cls — произвольный класс
method — строковое название метода
Функция должна возвращать класс, от которого класс cls унаследовал метод method. Если метода method нет ни в самом классе, ни в одном другом классе из его иерархии, функция get_method_owner() должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_method_owner(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class A:
    def m(self):
        pass
        
class B(A):
    pass

print(get_method_owner(B, 'm'))
Sample Output 1:

<class '__main__.A'>
Sample Input 2:

class A:
    def m(self):
        pass
        
class B(A):
    def m(self):
        pass

print(get_method_owner(B, 'm'))
Sample Output 2:

<class '__main__.B'>
Sample Input 3:

class A:
    pass
        
class B(A):
    pass

print(get_method_owner(B, 'm'))
Sample Output 3:

None

"""
def get_method_owner(cls, method):
    for c in cls.mro():
        if method in c.__dict__:
            return c
        
"""
Семья
С помощью множественного наследования постройте иерархию из приведенных ниже четырех классов. При решении старайтесь свести дублирование кода к минимуму.

1. Реализуйте класс Father, описывающий отца. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Father должен иметь один атрибут:

mood — настроение
Класс Father должен иметь два метода экземпляра:

greet() — метод, возвращающий строку Hello!
be_strict() — метод, изменяющий значение атрибута mood на строку strict
2. Также реализуйте класс Mother, описывающий мать. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Mother должен иметь один атрибут:

mood — настроение
Класс Mother должен иметь два метода экземпляра:

greet() — метод, возвращающий строку Hi, honey!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
3. Помимо этого, реализуйте класс Daughter, описывающий дочь. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Daughter должен иметь один атрибут:

mood — настроение
Класс Daughter должен иметь три метода экземпляра:

greet() — метод, возвращающий строку Hi, honey!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
be_strict() — метод, изменяющий значение атрибута mood на строку strict
4. Наконец, реализуйте класс Son, описывающий сына. При создании экземпляра класс должен принимать один аргумент:

mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Son должен иметь один атрибут:

mood — настроение
Класс Son должен иметь три метода экземпляра:

greet() — метод, возвращающий строку Hello!
be_kind() — метод, изменяющий значение атрибута mood на строку kind
be_strict() — метод, изменяющий значение атрибута mood на строку strict
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())
Sample Output 1:

neutral
neutral
Hello!
Hi, honey!
Sample Input 2:

father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)
Sample Output 2:

happy
unhappy
strict
kind
"""

from abc import ABC, abstractmethod

class Family(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood
    @abstractmethod
    def greet(self):
        pass

class Father(Family):
    def be_strict(self):
        self.mood = 'strict'

    def greet(self):
        return 'Hello!'

class Mother(Family):
    def be_kind(self):
        self.mood = 'kind'

    def greet(self):
        return 'Hi, honey!'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass



"""
Класс MROHelper
Реализуйте класс MROHelper, описывающий набор функций для работы с MRO произвольных классов. При создании экземпляра класс не должен принимать никаких аргументов.

Класс MROHelper должен иметь три статических метода:

len() — метод, принимающий в качестве аргумента класс и возвращающий количество элементов в его MRO
class_by_index() — метод, принимающий в качестве аргументов класс cls и целое число n, по умолчанию равное нулю, и возвращающий класс с индексом n в MRO класса cls
index_by_class() — метод, принимающий в качестве аргументов два класса child и parent и возвращающий целое число — индекс класса parent в MRO класса child
Примечание 1. Нумерация классов в MRO начинается с нуля.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса MROHelper нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.len(D))
Sample Output 1:

5
Sample Input 2:

class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))
Sample Output 2:

<class '__main__.C'>
<class '__main__.B'>
Sample Input 3:

class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.index_by_class(D, A))
Sample Output 3:

3
"""

class MROHelper:

    @staticmethod
    def len(cls):
        return len(cls.mro())
    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        chld = child.mro()
        for i, it in enumerate(chld):
            if parent == it:
                return i


if __name__ == "__main__":
    class A:
        def m(self):
            pass
            
    class B(A):
        pass

    print(get_method_owner(B, 'm'))


    father = Father()
    mother = Mother()

    print(father.mood)
    print(mother.mood)
    print(father.greet())
    print(mother.greet())

    class A:
        pass
        
    class B(A):
        pass
        
    class C(A):
        pass
        
    class D(B, C):
        pass
        
    print(MROHelper.index_by_class(D, A))