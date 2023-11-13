#1
"""
Классы Average, Median и Harmonic
Вам доступны классы Average, Median и Harmonic, имеющие сходный интерфейс. Все три класса используются для обработки пользовательских оценок и оценок критиков некоторого медиаконтента по стобалльной шкале и вычисления средних значений этих оценок. Задачей класса Average является нахождение среднего арифметического пользовательских оценок или оценок критиков, классов Median и Harmonic — медианы и среднего гармонического соответственно.

Изучите приведенные классы, реализуйте абстрактный базовый класс Middle и постройте корректную схему наследования. При выполнении старайтесь избегать дублирования кода.

Примечание 1. Функционал классов Average, Median и Harmonic должен остаться прежним, необходимо лишь объединить их в иерархию, определив для них единый базовый абстрактный класс Middle.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
Sample Input 1:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
average = Average(user_votes, expert_votes)

print(average.get_correct_user_votes())
print(average.get_correct_expert_votes())
print(average.get_average())
print(average.get_average(False))
Sample Output 1:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
66.75
78.75
Sample Input 2:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
median = Median(user_votes, expert_votes)

print(median.get_correct_user_votes())
print(median.get_correct_expert_votes())
print(median.get_average())
print(median.get_average(False))
Sample Output 2:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
71
81
Sample Input 3:

user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
harmonic = Harmonic(user_votes, expert_votes)

print(harmonic.get_correct_user_votes())
print(harmonic.get_correct_expert_votes())
print(round(harmonic.get_average(), 2))
print(round(harmonic.get_average(False), 2))
Sample Output 3:

[71, 56, 60, 80]
[87, 90, 67, 70, 81, 85, 79, 71]
65.46
77.92

"""
from abc import ABC, abstractmethod
class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self, to_sort=False):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.user_votes if 10 < vote < 90]
        return sorted(votes) if to_sort else votes

    def get_correct_expert_votes(self, to_sort=False):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        votes = [vote for vote in self.expert_votes if 5 < vote < 95]
        return sorted(votes) if to_sort else votes
    
    @abstractmethod
    def get_average(self, users=True, to_sort=False):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes(to_sort)
        else:
            votes = self.get_correct_expert_votes(to_sort)
        return votes  

class Average(Middle):
    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return sum(votes) / len(votes)

class Median(Middle):
    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users, to_sort=True)
        return votes[len(votes) // 2]

class Harmonic(Middle):
    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))
    


if __name__ == '__main__':
    user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
    expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
    average = Average(user_votes, expert_votes)

    print(average.get_correct_user_votes())
    print(average.get_correct_expert_votes())
    print(average.get_average())
    print(average.get_average(False))