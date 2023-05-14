"""

Класс Circle
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:

_radius — радиус круга
_diameter — диаметр круга
_area — площадь круга
Класс Circle должен иметь три метода экземпляра:

get_radius() — метод, возвращающий радиус круга
get_diameter() — метод, возвращающий диаметр круга
get_area() — метод, возвращающий площадь круга
Примечание 1. Площадь круга вычисляется по формуле
�
�
2
πr
2
 , где
�
r — радиус круга,
�
π — константа, которая выражает отношение длины окружности к ее диаметру.

Примечание 2. Импортировать константу
�
π можно из модуля math:

from math import pi
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
Sample Output 1:

1
2
3
Sample Input 2:

circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
Sample Output 2:

5
10
79

"""

import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = math.pi * radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area

#-----------------------//----------------------

"""

Класс BankAccount
Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:

balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:

_balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:

get_balance() — метод, возвращающий актуальный баланс счета
deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())
Sample Output 1:

0
100
50
Sample Input 2:

account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)
Sample Output 2:

На счете недостаточно средств
Sample Input 3:

account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())
Sample Output 3:

50
250
Sample Input 4:

account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
Sample Output 4:

На счете недостаточно средств

"""


class BankAccount:
    def __init__(self, balance: int | float=0):
        self._balance = balance

    def get_balance(self) -> int | float:
        return self._balance

    def deposit(self, amount: int | float):
        self._balance += amount

    def withdraw(self, amount: int | float):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account: object, amount: int | float):
        if self._balance - amount >= 0:
            account.deposit(amount)
            self._balance -= amount
        else:
            raise ValueError("На счете недостаточно средств")

# ________________________//_______________________________

"""

Класс User
Реализуйте класс User, описывающий интернет-пользователя. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Примечание 1. Если при создании экземпляра класса User имя и возраст одновременно являются некорректными, должно быть возбуждено исключение, связанное с именем.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())
Sample Output 1:

Гвидо
67
Sample Input 2:

user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())
Sample Output 2:

Тимур
30

"""

class User:
    RANGE_AGE = range(111)

    def __init__(self, name: str, age: int):
        if type(name) != str or not name or not name.isalpha():
            raise ValueError ("Некорректное имя")
        if type(age) != int or age not in self.RANGE_AGE:
            raise ValueError("Некорректный возраст")
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str):
        if type(new_name) != str or not new_name or not new_name.isalpha():
            raise ValueError ("Некорректное имя")
        self._name = new_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        if type(new_age) != int or new_age not in self.RANGE_AGE:
            raise ValueError("Некорректный возраст")
        self._age = new_age


if __name__ == "__main__":

    # 1
    circle = Circle(1)

    print(circle.get_radius())
    print(circle.get_diameter())
    print(round(circle.get_area()))


    # 2
    account = BankAccount()

    print(account.get_balance())
    account.deposit(100)
    print(account.get_balance())
    account.withdraw(50)
    print(account.get_balance())

    try:
        account.withdraw(150)
    except ValueError as e:
        print(e)

    account1 = BankAccount(100)
    account2 = BankAccount(200)

    account1.transfer(account2, 50)
    print(account1.get_balance())
    print(account2.get_balance())

    # 3

    user = User('Гвидо', 67)

    print(user.get_name())
    print(user.get_age())



    user.set_name('Тимур')
    user.set_age(30)

    print(user.get_name())
    print(user.get_age())