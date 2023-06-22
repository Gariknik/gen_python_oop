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




if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = ReversedSequence(numbers)

    print(reversed_numbers[0])
    numbers.append(6)
    print(reversed_numbers[0])


    array = SparseArray(0)

    array[5] = 1000
    array[12] = 1001

    print(array[5])
    print(array[12])
    print(array[13])