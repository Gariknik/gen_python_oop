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