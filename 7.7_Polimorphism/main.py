from abc import ABC, abstractmethod

class UniversalDate(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return f'{self.year}-{self.month:0>2}-{self.day:0>2}'   

class USADate(UniversalDate):   
    def format(self):
        return f'{self.month:0>2}-{self.day:0>2}-{self.year}'


class ItalianDate(UniversalDate):   
    def format(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'


if __name__ == "__main__":
    usadate = USADate(2023, 4, 6)

    print(usadate.format())
    print(usadate.iso_format())