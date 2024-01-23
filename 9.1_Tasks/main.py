"""
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub

"""

class CaesarCipher:
    LENGTH = 26
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, shift):
        self.shift = shift

    def encode(self, string):
        result = ''
        for ch in string:
            if ch in self.upper_alpha or ch in self.lower_alpha:
                if ch.islower():
                    result += self.lower_alpha[(self.lower_alpha.find(ch)+self.shift) % self.LENGTH]
                elif ch.isupper():
                    result += self.upper_alpha[(self.upper_alpha.find(ch)+self.shift) % self.LENGTH]
            else:
                result += ch
        return result
    
    def decode(self, string):
        result = ''
        for ch in string:
            if ch in self.upper_alpha or ch in self.lower_alpha:
                if ch.islower():
                    result += self.lower_alpha[self.lower_alpha.find(ch)-self.shift]
                elif ch.isupper():
                    result += self.upper_alpha[self.upper_alpha.find(ch)-self.shift]
            else:
                result += ch
        return result
    

"""
Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.

Примечание. Тестовые данные доступны по ссылкам:

"""
from abc import ABC, abstractmethod

class Progression(ABC):
    def __init__(self, first, step):
        self.first = first
        self.step = step

    def __iter__(self):
        return self
    
    @abstractmethod
    def __next__(self):
        pass



class ArithmeticProgression(Progression):
    def __next__(self):
        it = self.first
        self.first += self.step
        return it

class GeometricProgression(Progression):
    def __next__(self):
        it = self.first
        self.first *= self.step
        return it




if __name__ == '__main__':
    cipher = CaesarCipher(10)

    words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
            'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
            'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
            'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
            'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
            'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
            'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
            'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
            'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

    encode_words = [cipher.encode(word) for word in words]
    print(encode_words)

    decode_words = [cipher.decode(word) for word in encode_words]
    print(decode_words)


    # progression = ArithmeticProgression(0, 1)

    # for elem in progression:
    #     if elem > 10:
    #         break
    #     print(elem, end=' ')


    progression = GeometricProgression(1, 2)

    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')