import math

class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем.")

        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @classmethod
    def from_string(cls, input_string):
        parts = input_string.replace(' ', '').split('/')
        if len(parts) == 1:
            numerator = int(parts[0])
            denominator = 1
        else:
            numerator = int(parts[0])
            denominator = int(parts[1])
        return cls(numerator, denominator)

    @classmethod
    def from_file(cls, filename):
        numbers = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        numbers.append(cls.from_string(line))
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено.")
        return numbers

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            denom = self.denominator * other.denominator
            return RationalNumber(num, denom)
        elif isinstance(other, int):
            num = self.numerator + other * self.denominator
            return RationalNumber(num, self.denominator)
        else:
            raise TypeError("Непідтримуваний тип операнду для +: 'RationalNumber' та {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            denom = self.denominator * other.denominator
            return RationalNumber(num, denom)
        elif isinstance(other, int):
            num = self.numerator - other * self.denominator
            return RationalNumber(num, self.denominator)
        else:
            raise TypeError("Непідтримуваний тип операнду для -: 'RationalNumber' та {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            num = self.numerator * other.numerator
            denom = self.denominator * other.denominator
            return RationalNumber(num, denom)
        elif isinstance(other, int):
            num = self.numerator * other
            return RationalNumber(num, self.denominator)
        else:
            raise TypeError("Непідтримуваний тип операнду для *: 'RationalNumber' та {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            if other.numerator == 0:
                raise ZeroDivisionError("Ділення на нуль.")
            num = self.numerator * other.denominator
            denom = self.denominator * other.numerator
            return RationalNumber(num, denom)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Ділення на нуль.")
            num = self.numerator
            denom = self.denominator * other
            return RationalNumber(num, denom)
        else:
            raise TypeError("Непідтримуваний тип операнду для /: 'RationalNumber' та {}".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, RationalNumber):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        else:
            return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"RationalNumber({self.numerator}, {self.denominator})"

    def __abs__(self):
        return RationalNumber(abs(self.numerator), self.denominator)

    def __neg__(self):
        return RationalNumber(-self.numerator, self.denominator)

    def __pos__(self):
        return RationalNumber(self.numerator, self.denominator)

    def __int__(self):
        return self.numerator // self.denominator

    def numerator(self):
        return self.numerator

    def denominator(self):
        return self.denominator

    def is_integer(self):
        return self.denominator == 1

    def sign(self):
        if self.numerator > 0:
            return 1
        elif self.numerator < 0:
            return -1
        else:
            return 0



numbers1 = RationalNumber.from_file(r'C:\Users\ASUS\Downloads\input1.txt')


if numbers1:
    # Знаходження максимального числа
    max_number = max(numbers1, key=lambda x: float(x.numerator) / x.denominator)
    print(f"Максимальне число: {max_number}")

    # Знаходження максимального числа за модулем
    max_abs_number = max(numbers1, key=lambda x: abs(float(x.numerator) / x.denominator))
    print(f"Максимальне число за модулем: {max_abs_number}")


    average = sum(float(num.numerator) / num.denominator for num in numbers1) / len(numbers1)
    print(f"Середнє арифметичне: {average}")
else:
    print(f"Не вдалося знайти або обробити файл 'input1.txt'.")


