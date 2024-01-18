"""

Класс City
Вам доступен класс City, описывающий город. При создании экземпляра класс принимает три аргумента в следующем порядке:

name — название города (тип str)
population — население города (тип int)
founded — год основания города (тип int)
Экземпляр класса City имеет три атрибута:

name — название города
population — население города
founded — год основания города
Также экземпляр класса City имеет следующее формальное строковое представление:

City(name='<название города>', population=<население города>, founded=<год основания города>)
Наконец, экземпляры класса City поддерживают между собой операцию сравнения с помощью операторов == и !=. Два города считаются равными, если их названия, население и годы основания совпадают.

Реализуйте класс City в виде класса данных.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса City нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)
Sample Output 1:

City(name='Tokyo', population=14043239, founded=1457)
Tokyo
14043239
1457
Sample Input 2:

city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)
Sample Output 2:

False
True
True
False

"""
from dataclasses import dataclass

@dataclass
class City:
    name: str
    population: int
    founded: int



"""

Класс MusicAlbum
Реализуйте неизменяемый класс MusicAlbum, описывающий музыкальный альбом. При создании экземпляра класс должен принимать четыре аргумента в следующем порядке:

title — название альбома (тип str)
artist — автор альбома (тип str)
genre — жанр альбома (тип str)
year — год выпуска альбома (тип int)
Экземпляр класса MusicAlbum должен иметь четыре атрибута:

title — название альбома
artist — автор альбома
genre — жанр альбома
year — год выпуска альбома
Также экземпляр класса MusicAlbum должен иметь следующее формальное строковое представление:

MusicAlbum(title='<название альбома>', artist='<автор альбома>')
Наконец, экземпляры класса MusicAlbum должны поддерживать между собой операцию сравнения с помощью операторов == и!=. Два музыкальных альбома считаются равными, если их названия, авторы и годы выпуска совпадают.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса MusicAlbum нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))
Sample Output 1:

MusicAlbum(title='Calendar', artist='Motorama')
Sample Input 2:

musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)
Sample Output 2:

True
False
Sample Input 3:

musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)

try:
    musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
except:
    print('Error')
Sample Output 3:

Error
"""

from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(compare=False)
    year: int

    def __repr__(self):
        return f"{self.__class__.__name__}(title='{self.title}', artist='{self.artist}')"


"""

Класс Point
Реализуйте класс данных Point, описывающий точку на координатной плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата точки по оси 
�
x (тип float), по умолчанию имеет значение 0.0
y — координата точки по оси 
�
y (тип float), по умолчанию имеет значение 0.0
Экземпляр класса Point должен иметь три атрибута:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
quadrant — координатная четверть, к которой принадлежит точка (тип int). Если точка лежит на одной из осей, координатная четверть считается равной 0
Класс Point должен иметь два метода экземпляра:

symmetric_x() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси 
�
x
symmetric_y() — метод, возвращающий новый экземпляр класса Point, представляющий точку, симметричную текущей точке относительно оси 
�
y
Экземпляр класса Point должен иметь следующее формальное строковое представление:

Point(x=<координата x>, y=<координата y>, quadrant=<координатная четверть>)
Наконец, экземпляры класса Point должны поддерживать между собой операцию сравнения с помощью операторов == и!=. Две точки считаются равными, если их координаты по обеим осям совпадают.

Примечание 1. Для точки с координатами 
(
�
,
�
)
(x,y) симметричной относительно оси 
�
x будем считать точку с координатами 
(
�
,
−
�
)
(x,−y), симметричной относительно оси 
�
y — точку с координатами 
(
−
�
,
�
)
(−x,y).

Примечание 2. Координатные четверти:



Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)
Sample Output 1:

Point(x=0.0, y=0.0, quadrant=0)
0.0
0.0
0
Sample Input 2:

point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
Sample Output 2:

Point(x=1.0, y=-2.0, quadrant=4)
Point(x=-1.0, y=2.0, quadrant=2)
Sample Input 3:

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)
Sample Output 3:

True
False
True
"""

from dataclasses import dataclass, field

@dataclass(order=True)
class Point:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    quadrant: int = field(init=False, default=0 , compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 and self.y > 0:
            self.quadrant =2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4


    def symmetric_x(self):
        return Point(self.x * (-1), self.y)

    def symmetric_y(self):
        return Point(self.x, self.y * (-1))

    def __repr__(self):
        return f"{self.__class__.__name__}(x='{self.x}', y='{self.y}, quadrant={self.quadrant}')"

if __name__ == "__main__":
    city = City('Tokyo', 14043239, 1457)

    print(city)
    print(city.name)
    print(city.population)
    print(city.founded)

    print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))
    musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
    musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

    print(musicalbum1 == musicalbum2)
    print(musicalbum1 != musicalbum2)


    point = Point(1.0, 2.0)

    print(point.symmetric_x())
    print(point.symmetric_y())