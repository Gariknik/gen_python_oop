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