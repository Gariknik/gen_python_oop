
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



if __name__ == "__main__":
    class A:
        def m(self):
            pass
            
    class B(A):
        pass

    print(get_method_owner(B, 'm'))