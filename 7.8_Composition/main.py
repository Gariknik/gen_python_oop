"""
Классы Point и Circle
1. Реализуйте класс Point, описывающий точку на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата точки по оси 
�
x
y — координата точки по оси 
�
y
Экземпляр класса Point должен иметь следующее неформальное строковое представление:

​(<координата x>, <координата y>)
2. Также реализуйте класс Circle, описывающий окружность на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

radius — радиус окружности
center — точка с координатами центра окружности, представленная экземпляром класса Point
Экземпляр класса Circle должен иметь следующее неформальное строковое представление:

(<координата центра по оси x>, <координата центра по оси y>), r = <радиус>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

point = Point(1, 1)
circle = Circle(5, point)

print(point)
print(circle)
Sample Output:

(1, 1)
(1, 1), r = 5
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{self.center}, r = {self.radius}'

"""
Классы Item и ShoppingCart
1. Реализуйте класс Item, описывающий товар. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — название товара
price — цена товара в долларах
Экземпляр класса Item должен иметь следующее неформальное строковое представление:

<название товара>, <цена товара>$
2. Также реализуйте класс ShoppingCart, описывающий корзину для покупок. При создании экземпляра класс должен принимать один аргумент:

items — итерируемый объект, определяющий начальный набор товаров в корзине. Если не передан, корзина считается пустой
Класс ShoppingCart должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента товар и добавляющий его в корзину
total() — метод, возвращающий суммарную стоимость всех товаров в корзине
remove() — метод, принимающий в качестве аргумента название товара и удаляющий его из корзины. Если в корзине несколько товаров с указанным именем, они должны быть удалены все
Экземпляр класса ShoppingCart должен иметь следующее неформальное строковое представление:

<название первого товара в корзине>, <цена первого товара в корзине>$
<название второго товара в корзине>, <цена второго товара в корзине>$
...
Примечание 1. Если корзина для покупок пуста, то ее неформальным строковым представлением должна быть пустая строка.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)
Sample Output 1:

Yoga Mat, 130$
Flannel Shirt, 22$
Sample Input 2:

shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())
Sample Output 2:

Yoga Mat, 130$
Flannel Shirt, 22$
152
Sample Input 3:

shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())
Sample Output 3:

Flannel Shirt, 22$
22

"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'
    
class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items
    def __str__(self):
        return '\n'.join(str(item) for item in self.items)

    def add(self, item):
        self.items.append(item)
    def total(self):
        return sum([x.price for x in self.items])
    def remove(self, name):
        self.items = list(filter(lambda x: x.name != name, self.items))

if __name__ == "__main__":
    point = Point(1, 1)
    circle = Circle(5, point)

    print(point)
    print(circle)


    item1 = Item('Yoga Mat', 130)
    item2 = Item('Flannel Shirt', 22)

    print(item1)
    print(item2)