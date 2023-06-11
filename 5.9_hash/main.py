#1 
"""
Функция hash_function()
Реализуйте функцию hash_function(), которая принимает один аргумент:

obj — произвольный объект
Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:

вычисление значения выражения:
ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
где obj — объект, преобразованный в строку с помощью функции str(). Обратите внимание, что суммироваться должны произведение первого и последнего элементов, второго и предпоследнего, и так далее до середины. Если obj имеет нечетное количество символов, то серединный элемент должен прибавляться без перемножения
вычисление значения выражения:
ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
где obj — объект, преобразованный в строку с помощью функции str()
вычисление значения выражения:
(temp1 * temp2) % 123456791
где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге
и возвращать значение, полученное в третьем шаге.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_function(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

print(hash_function('python'))
Sample Output 1:

111998846
Sample Input 2:

print(hash_function(12345))
Sample Output 2:

834432
Sample Input 3:

print(hash_function(None))
Sample Output 3:

119077607

"""

def hash_function(obj):
  res = str(obj)
  if len(res) % 2 == 0:
    left = res[:len(res)//2+1]
    right = res[len(res)//2:][::-1]
    temp1 = sum([ord(l) * ord(r) for l, r in zip(left, right)])
  else:
    left = res[:len(res)//2]
    right = res[len(res)//2+1:][::-1]
    temp1 = sum([ord(l) * ord(r) for l, r in zip(left, right)]) + ord(res[len(res)//2])
  temp2 = 0
  for key, item in enumerate(res, 1):
    if key % 2:
      temp2 += ord(res[key-1]) * key
    else:
      temp2 -= ord(res[key-1]) * key
  return (temp1 * temp2) % 123456791


#2
"""
Функция limited_hash() 🌶️
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:

left — целое число
right — целое число
hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()
Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right], и возвращает полученный результат.

Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его в left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования, но в другую сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться циклично при очередном выходе из диапазона.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию limited_hash(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

hash_function = limited_hash(10, 15)

print(hash_function(10))
print(hash_function(11))
print(hash_function(15))
Sample Output 1:

10
11
15
Sample Input 2:

hash_function = limited_hash(10, 15)

print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))
Sample Output 2:

10
11
15
10
11
Sample Input 3:

hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))
Sample Output 3:

15
14
10
15
14


"""

# def limited_hash(left, right, hash_function=hash):
#   def behavior(obj):
#     res = hash_function(obj)
#     while True:
#       if left <= res <= right:
#         return res
#       if res > right:
#         res = left + (res - right - 1)
#       if res < left:
#         res = right - (left - res) + 1
      
#   return behavior


def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(x):
        return left + (hash_function(x) - left) % (right - left + 1)
    return inner_hash_function




if __name__ == '__main__':
    hash_function = limited_hash(10, 15)
    print(hash_function(10))
    print(hash_function(11))
    print(hash_function(15))

    print(hash_function(16))
    print(hash_function(17))
    print(hash_function(21))
    print(hash_function(22))
    print(hash_function(23))
    print(hash_function(3))