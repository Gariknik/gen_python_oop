"""
Класс Knight ♞
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:

horizontal — координата коня на шахматной доске по горизонтали
vertical — координата коня на шахматной доске по вертикали
color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали, и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *

Примечание 1. Шахматное поле имеет вид:

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)
Sample Output 1:

white N
c 3
Sample Input 2:

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
Sample Output 2:

c 3
False
True
e 4
Sample Input 3:

knight = Knight('c', 3, 'white')

knight.draw_board()
Sample Output 3:

........
........
........
.*.*....
*...*...
..N.....
*...*...
.*.*....


"""


class Knight:
    X: str = 'abcdefgh'
    Y: list = [1, 2, 3, 4, 5, 6, 7, 8]
    COLORS: list = ['black', 'white']
    LENGTH: int = 8
    F_MARK: str = 'N'
    M_MARK: str = '*'
    E_MARK: str = '.'

    def __init__(self, horizontal: str, vertical: int, color: str):
        if horizontal in self.X and vertical in self.Y and color in self.COLORS:
            self.horizontal = horizontal
            self.vertical = vertical
            self.color = color

    def get_char(self) -> str:
        return self.F_MARK

    def can_move(self, h: str, v: int) -> bool:
        return (self.X.find(h) - self.X.find(self.horizontal)) ** 2 + (v - self.vertical) ** 2 == 5

    def move_to(self, h: str, v: int):
        if self.can_move(h, v):
            self.horizontal = h
            self.vertical = v

    def draw_board(self):
        self.board = [[self.E_MARK
                       for _ in range(self.LENGTH)]
                      for _ in range(self.LENGTH)]

        for v in range(self.LENGTH):
            for h in range(self.LENGTH):
                if h == self.X.find(self.horizontal) and v == self.vertical - 1:
                    self.board[v][h] = self.get_char()
                elif self.can_move(self.X[h], v + 1):
                    self.board[v][h] = self.M_MARK

        for i in range(self.LENGTH - 1, -1, -1):
            for j in range(self.LENGTH):
                print(self.board[i][j], end='')
            print()




knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

knight.draw_board()