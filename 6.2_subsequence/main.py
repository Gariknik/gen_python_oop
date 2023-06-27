#1
"""

Класс ReversedSequence
Реализуйте класс ReversedSequence, описывающий объект, который реализует доступ к элементам некоторой последовательности в обратном порядке. При создании экземпляра класс должен принимать один аргумент:

sequence — последовательность
При передаче экземпляра класса ReversedSequence в функцию len() должна возвращаться его длина, представленная количеством элементов в исходной последовательности.

Также экземпляр класса ReversedSequence должен быть итерируемым объектом, элементами которого являются элементы исходной последовательности в обратном порядке.

Наконец, экземпляр класса ReversedSequence должен позволять получать значения элементов исходной последовательности с помощью индексов, при этом индексация должна производиться в обратном порядке, то есть по индексу 0 должен быть доступен последний элемент исходной последовательности, по индексу 1 — предпоследний элемент, по индексу 2 — предпредпоследний элемент, и так далее.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса ReversedSequence должен зависеть от последовательности, на основе которой он был создан. Другими словами, если исходная последовательность изменится, то должен измениться и экземпляр класса ReversedSequence.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса ReversedSequence нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])
Sample Output 1:

5
4
3
Sample Input 2:

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])
Sample Output 2:

5
6
Sample Input 3:

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
Sample Output 3:

5
7

"""

class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        yield from self.sequence[::-1]

    def __len__(self):
        return len(self.sequence)
    
    def __getitem__(self, key):
        return self.sequence[~key]
    


#2
"""

Класс SparseArray
Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.

Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:

default — значение по умолчанию для неопределенных элементов разреженного массива
Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])
Sample Output 1:

1000
1001
0
Sample Input 2:

array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])
Sample Output 2:

Timur
Arthur
None

"""

class SparseArray:
    def __init__(self, default) -> None:
        self.default = default
        self.lst = []

    def __getitem__(self, key):
        if key >= len(self.lst):
            for _  in range(len(self.lst), key+1):
                self.lst += [self.default]
        return self.lst[key]
    
    def __setitem__(self, key, value):
        if key >= len(self.lst):
            for _  in range(len(self.lst), key+1):
                self.lst += [self.default]
        self.lst[key] = value

#3
"""

Класс CyclicList
Реализуйте класс CyclicList, описывающий циклический список. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов циклического списка. Если не передан, начальный набор элементов считается пустым
Класс CyclicList должен иметь два метода экземпляра:

append() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец циклического списка
pop() — метод, который принимает в качестве аргумента индекс элемента циклического списка, возвращает его значение и удаляет из циклического списка элемент с данным индексом. Если аргумент не передан, возвращаемым и удаляемым элементом считается последний элемент циклического списка 
При передаче экземпляра класса CyclicList в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса CyclicList должен быть зацикленным итерируемым объектом. Другими словами, итерация по нему должна происходить бесконечно, и при каждом достижении его последнего элемента она должна начинаться сначала.

Наконец, экземпляр класса CyclicList должен позволять получать значения своих элементов с помощью индексов, при этом индексы должны работать циклически. Например, в циклическом списке [1, 2, 3] элементом с индексом 4 должно являться число 2.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса CyclicList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса CyclicList измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса CyclicList нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')
Sample Output 1:

1 2 3 1 2 3 1
Sample Input 2:

cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))
Sample Output 2:

4
3
1
2

"""

class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        self.iterable = list(iterable)

    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key % len(self)]
    
    def append(self, *args):
        self.iterable += list(args)

    def pop(self, key=-1):
        return self.iterable.pop(key % len(self))

        

#4

"""

Класс SequenceZip
Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса SequenceZip не должен зависеть от итерируемых объектов, на основе которых он был создан. Другими словами, если исходные итерируемые объекты изменятся, то экземпляр класса SequenceZip измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))
Sample Output 1:

[('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3)]
(('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3))
Sample Input 2:

sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])
Sample Output 2:

3
('B', 'geek', 2)
('C', 'python', 3)

""" 
from copy import deepcopy
from typing import Any
class SequenceZip:
    def __init__(self, *args):
        self.iterables = deepcopy(tuple(args))

    def __len__(self):
        if list(self.iterables):
            return min(len(i) for i in self.iterables)
        return 0
    
    def __iter__(self):
        yield from zip(*self.iterables)
    
    def __getitem__(self, key):
        for index, it in enumerate(self):
            if key == index:
                return tuple(it)


#5
"""

​​​​​Класс OrderedSet
Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан, начальный набор элементов считается пустым
Класс OrderedSet должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного множества
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества, если он в нем присутствует
При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.

Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы, реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют равную длину и содержат равные элементы без учета их расположения.

Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.

Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))
Sample Output 1:

bee python stepik geek
4
Sample Input 2:

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)
Sample Output 2:

True
False
Sample Input 3:

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)
Sample Output 3:

green blue red
green red

"""

class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = dict()
        else:
            self.iterable = dict((it, it) for it in iterable)
    
    def add(self, obj):
        self.iterable |= {obj: obj}

    def discard(self, obj):
        if obj in self.iterable:
            self.iterable.pop(obj)

    def __len__(self):
        return len(self.iterable)
    
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and all(s == o for s, o in zip(self.iterable.keys(), other.iterable.keys()))
        if isinstance(other, set):
            return len(self) == len(other) and set(self.iterable.keys()) == other
        return NotImplemented
    
    def __iter__(self):
        yield from self.iterable.keys()

    def __contains__(self, item):
        return item in self.iterable


#6
"""

Класс AttrDict
Реализуйте класс AttrDict, описывающий упрощенный словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов упрощенного словаря. Если не передан, начальный набор элементов считается пустым
При передаче экземпляра класса AttrDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса AttrDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса AttrDict должен позволять получать значения своих элементов как по их ключам, так и по одноименным атрибутам. Реализовывать добавление элементов и изменение их значений по одноименным атрибутам не нужно.

Примечание 1. Экземпляр класса AttrDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса AttrDict измениться  не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AttrDict нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))
Sample Output 1:

X Æ A-12
Elon Musk
2
Sample Input 2:

attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)
Sample Output 2:

Dubai
31
Sample Input 3:

attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)
Sample Output 3:

BEEGEEK
BEEGEEK

"""

import copy
class AttrDict:
    def __init__(self, data={}):
        self.dict = copy.deepcopy(data)

    def __len__(self):
        return len(self.dict)
    
    def __getattr__(self, attr):
        return self.dict[attr]
    
    def __getitem__(self, key):
        return self.dict[key]
    
    def __setitem__(self, key, value):
        self.dict[key] = value
    
    def __iter__(self):
        yield from self.dict.keys()


#7
"""

Класс PermaDict
Реализуйте класс PermaDict, описывающий словарь, который позволяет добавлять и удалять пары (<ключ>, <значение>), но не позволяет изменять значения по уже имеющимся ключам. При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов экземпляра класса PermaDict. Если не передан, начальный набор элементов считается пустым
Класс PermaDict должен иметь три метода экземпляра:

keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса PermaDict
values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса PermaDict
items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса PermaDict в виде кортежей (<ключ>, <значение>)
При передаче экземпляра класса PermaDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса PermaDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса PermaDict должен позволять получать значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся с помощью оператора del. При этом изменение значений по уже имеющимся ключам должно быть недоступно, и при попытке выполнения такой операции должно возбуждаться исключение KeyError с текстом:

Изменение значения по ключу невозможно
Примечание 1. Экземпляр класса PermaDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса PermaDict измениться  не должен.

Примечание 2. Реализация класса PermaDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))
Sample Output 1:

Timur
2
Sample Input 2:

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())
Sample Output 2:

name city age
name city age
Timur Moscow 30
('name', 'Timur') ('city', 'Moscow') ('age', 30)
Sample Input 3:

permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))
Sample Output 3:

30
1
Sample Input 4:

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)
Sample Output 4:

'Изменение значения по ключу невозможно'

"""

import copy
class PermaDict:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = copy.deepcopy(data)

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data.keys()

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError ("Изменение значения по ключу невозможно")
        self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
        

    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()

#8
"""

Класс HistoryDict 🌶️
Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
Класс HistoryDict должен иметь пять методов экземпляра:

keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся.

Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.

Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))
Sample Output 1:

99
1
2
Sample Input 2:

historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())
Sample Output 2:

ducks cats
ducks cats
99 1
('ducks', 99) ('cats', 1)
Sample Input 3:

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))
Sample Output 3:

[99, 100]
[1]
[]
Sample Input 4:

historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())
Sample Output 4:

{'ducks': [99], 'cats': [1]}
{'ducks': [99, 100, 101], 'cats': [1, 2]}
Sample Input 5:

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))
Sample Output 5:

3
1

"""
class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = {}
            for key, value in data.items():
                self.data[key] = self.data.get(key, []) + [value]
        
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data.keys()

    def __getitem__(self, key):
        return self.data[key][-1]
    
    def __setitem__(self, key, value):
        if key not in self.data:
            self.data |= {key: [value]}
        else:
            self.data[key].append(value)
        
    def __delitem__(self, key):
        del self.data[key]

    def keys(self):
        return self.data.keys()
    
    def values(self):
        return (v[-1] for v in self.data.values())
    
    def items(self):
        return ((k, v[-1]) for k, v in self.data.items())
    
    def history(self, key):
        if key not in self.data:
            return []
        return self.data[key]
    
    def all_history(self):
        return self.data



#9
"""

Класс MutableString 🌶️
Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:

string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
Класс MutableString должен иметь два метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:

<текущее значение изменяемой строки>
Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:

MutableString('<текущее значение изменяемой строки>')
При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.

Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

mutablestring = MutableString('beegeek')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))
Sample Output 1:

b e e g e e k
beegeek
MutableString('beegeek')
Sample Input 2:

mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
Sample Output 2:

beegeek
BEEGEEK
Sample Input 3:

mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)
Sample Output 3:

beegeek
geekbee
Sample Input 4:

mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)
Sample Output 4:

beegeek
BeeGeek

"""
import copy
class MutableString:
    def __init__(self, string=None) -> None:
        self.string = copy.deepcopy(string) or ''
    
    def __str__(self) -> str:
        return str(self.string)
    
    def __repr__(self) -> str:
        return f'MutableString(\'{self.string}\')'
    
    def __len__(self):
        return len(self.string)
    
    def __iter__(self):
        yield from self.string

    def __getitem__(self, key):
        return MutableString(self.string[key])
    
    def __setitem__(self, key, value):
        lst = list(self.string)
        lst[key] = value
        self.string = ''.join(lst)

    def __delitem__(self, key):
        lst = list(self.string)
        del lst[key]
        self.string = ''.join(lst)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(str(self)+str(other))
        return NotImplemented
        
    def upper(self):
        self.string = str(self).upper()
        
    def lower(self):
        self.string = str(self).lower()

if __name__ == '__main__':
    # numbers = [1, 2, 3, 4, 5]
    # reversed_numbers = ReversedSequence(numbers)

    # print(reversed_numbers[0])
    # numbers.append(6)
    # print(reversed_numbers[0])


    # array = SparseArray(0)

    # array[5] = 1000
    # array[12] = 1001

    # print(array[5])
    # print(array[12])
    # print(array[13])

    # print('##################')

    # sequencezip = SequenceZip()
    # print(len(sequencezip))
    # print(list(sequencezip))

    # print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
    # print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
    # print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
    # print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
    # print(OrderedSet(['green', 'red', 'blue']) == 100)


    # attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

    # attrdict['city'] = 'Dubai'
    # attrdict['age'] = 31
    # print(attrdict.city)
    # print(attrdict.age)

    historydict = HistoryDict({'ducks': 99, 'cats': 1})

    historydict['dogs'] = 1
    print(len(historydict))
    del historydict['ducks']
    del historydict['cats']
    print(len(historydict))


    mutablestring = MutableString('beegeek')

    s1 = mutablestring[2:]
    s2 = mutablestring[:5]
    s3 = mutablestring[2:5:2]

    print(s1, type(s1))
    print(s2, type(s2))
    print(s3, type(s3))