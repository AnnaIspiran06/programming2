from math import isqrt


class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        if isinstance(numerator, Rational):
            numerator, denominator = numerator.numerator, numerator.denominator
        common = self.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // common
        self.denominator = denominator // common

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def from_string(cls, s):
        parts = s.strip().split('/')
        if len(parts) == 1:
            return cls(int(parts[0].strip()))
        elif len(parts) == 2:
            return cls(int(parts[0].strip()), int(parts[1].strip()))
        else:
            raise ValueError("Invalid rational number format")

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator +
                             other.numerator * self.denominator)
            return Rational(new_numerator, common_denominator)
        elif isinstance(other, int):
            return self + Rational(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            new_numerator = (self.numerator * other.denominator -
                             other.numerator * self.denominator)
            return Rational(new_numerator, common_denominator)
        elif isinstance(other, int):
            return self - Rational(other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self * Rational(other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError("Division by zero")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self / Rational(other)
        else:
            return NotImplemented

    def __pow__(self, power):
        if not isinstance(power, int):
            return NotImplemented
        if power == 0:
            return Rational(1)
        elif power > 0:
            return Rational(self.numerator ** power, self.denominator ** power)
        else:
            return Rational(self.denominator ** -power, self.numerator ** -power)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self == Rational(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __pos__(self):
        return Rational(self.numerator, self.denominator)

    def __bool__(self):
        return self.numerator != 0


def evaluate_polynomial(coeffs, x):
    result = Rational(0)
    for i, coeff in enumerate(coeffs):
        result += coeff * x ** (len(coeffs) - i - 1)
    return result


def get_quadratic_equation(coeffs):
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    return f"{a}*x^2 + {b}*x + {c} = 0"


def find_quadratic_roots(coeffs):
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (Rational(2) * a)
        return [root]
    else:
        sqrt_discriminant = isqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (Rational(2) * a)
        root2 = (-b - sqrt_discriminant) / (Rational(2) * a)
        return [root1, root2]


def find_rational_roots(coeffs):
    leading_coefficient = coeffs[0]
    constant_term = coeffs[-1]
    rational_roots = []
    for p in range(1, abs(constant_term) + 1):
        if constant_term % p == 0:
            for q in range(1, abs(leading_coefficient) + 1):
                if leading_coefficient % q == 0:
                    candidate = Rational(p, q)
                    if evaluate_polynomial(coeffs, candidate).numerator == 0:
                        rational_roots.append(candidate)
    return rational_roots


def determine_degree_and_find_roots(coeffs):
    degree = len(coeffs) - 1
    if degree == 0:
        return "Degree is 0, no equation to solve"
    elif degree == 1:
        return find_quadratic_roots(coeffs)
    elif degree == 2:
        return find_quadratic_roots(coeffs)
    else:
        return find_rational_roots(coeffs)


def process_input_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            coeffs = [Rational.from_string(token) for token in line.strip().split(',')]
            output_file.write(f"Coefficients: {coeffs}\n")

            degree = len(coeffs) - 1
            if degree == 0:
                output_file.write("Degree is 0, no equation to solve\n")
            elif degree == 1:
                linear_equation = get_quadratic_equation(coeffs)
                output_file.write(f"Linear equation: {linear_equation}\n")
                roots = find_quadratic_roots(coeffs)
                output_file.write(f"Roots: {roots}\n")
            elif degree == 2:
                quadratic_equation = get_quadratic_equation(coeffs)
                output_file.write(f"Quadratic equation: {quadratic_equation}\n")
                roots = find_quadratic_roots(coeffs)
                output_file.write(f"Roots: {roots}\n")
            else:
                output_file.write("Polynomial degree > 2, finding rational roots\n")
                rational_roots = find_rational_roots(coeffs)
                output_file.write(f"Rational roots: {rational_roots}\n")
            output_file.write("\n")


if __name__ == "__main__":
    input_file = (r'C:\Users\ASUS\Downloads\input1.txt')  # Припустимо, що файл input.txt містить коефіцієнти многочленів
    output_file = "output21.txt"  # Файл, в який будуть записуватись результати
    process_input_file(input_file, output_file)
