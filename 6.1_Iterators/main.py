#1
"""
Класс Point
Реализуйте класс Point, описывающий точку в пространстве. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
z — координата точки по оси 
�
z
Экземпляр класса Point должен иметь следующее формальное строковое представление:

Point(<координата x>, <координата y>, <координата z>)
Также экземпляр класса Point должен быть итерируемым объектом, элементами которого являются его координаты по осям 
�
x, 
�
y и 
�
z.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Point нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

point = Point(1, 2, 3)

print(list(point))
Sample Output 1:

[1, 2, 3]
Sample Input 2:

point = Point(1, 2, 3)
x, y, z = point

print(x, y, z)
Sample Output 2:

1 2 3
Sample Input 3:

points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
print(points)
Sample Output 3:

[Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]


"""
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        yield from self.__dict__.values()


#2
"""

Класс DevelopmentTeam
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший). При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:

add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков
Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:

(<имя разработчика>, 'junior')
в то время как senior-разработчики — в виде кортежей:

(<имя разработчика>, 'senior')
Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')
Sample Output 1:

('Timur', 'junior')
('Arthur', 'junior')
('Valery', 'junior')
('Gvido', 'senior')
Sample Input 2:

beegeek = DevelopmentTeam()

print(len(list(beegeek)))
Sample Output 2:

0
Sample Input 3:

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')
Sample Output 3:

('Timur', 'junior')
('Arthur', 'junior')
('Valery', 'junior')

"""

class DevelopmentTeam:
    def __init__(self):
        self.LIST_EMPLOYEES = []

    def add_junior(self, *args):
        self.LIST_EMPLOYEES += [(arg, 'junior') for arg in args]

    def add_senior(self, *args):
        self.LIST_EMPLOYEES += [(arg, 'senior') for arg in args]

    def __iter__(self):
        yield from sorted(self.LIST_EMPLOYEES, key=lambda x: x[1])


if __name__ == '__main__':
    point = Point(1, 2, 3)

    print(list(point))

    beegeek = DevelopmentTeam()

    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    beegeek.add_senior('Gvido')
    print(*beegeek, sep='\n')


    smart_monkey = DevelopmentTeam()

    smart_monkey.add_senior('Gvido', 'Alan')
    smart_monkey.add_junior('Denis')

    print(list(smart_monkey))