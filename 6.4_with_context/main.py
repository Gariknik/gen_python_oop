#1
"""

Функция is_context_manager()
Реализуйте функцию is_context_manager(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является контекстным менеджером, или False в противном случае. 

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_context_manager(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input:

print(is_context_manager(open('output.txt', mode='w')))
Sample Output:

True


"""

def is_context_manager(obj):
    try:
        with obj as o:
            return True
    except:
        return False
    
# def is_context_manager(obj):
#     return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')

if __name__ == '__main__':
    print(is_context_manager(open('output.txt', mode='w')))