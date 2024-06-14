import math

class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Неможливий трикутник з такими сторонами")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c

class Rectangle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Неправильні розміри прямокутника")
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

class Trapeze:
    def __init__(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError("Неправильні розміри трапеції")
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate_area(self):
        # Використовуємо формулу площі трапеції за висотою:
        # h = sqrt(c^2 - ((a - b + c^2 - d^2)/(2(a - b)))^2)
        # Площа = ((a + b) / 2) * h
        s1 = (self.a + self.b - self.c + self.d) / 2
        s2 = (self.a + self.b + self.c - self.d) / 2
        s3 = (-self.a + self.b + self.c + self.d) / 2
        s4 = (self.a - self.b + self.c + self.d) / 2
        try:
            h = 2 * math.sqrt((s1 * s2 * s3 * s4) / (self.a + self.b))
            return ((self.a + self.b) / 2) * h
        except ValueError:
            return 0  # У разі коли корінь з від'ємного числа

    def calculate_perimeter(self):
        return self.a + self.b + self.c + self.d

class Circle:
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Неправильний радіус кола")
        self.r = r

    def calculate_area(self):
        return math.pi * self.r**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.r

def read_shapes(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            shape_type = parts[0]
            if shape_type == 'Triangle':
                a, b, c = map(float, parts[1:])
                if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
                    shapes.append(Triangle(a, b, c))
                else:
                    print(f"Ignoring invalid triangle: {parts[1:]}")
            elif shape_type == 'Rectangle':
                a, b = map(float, parts[1:])
                if a > 0 and b > 0:
                    shapes.append(Rectangle(a, b))
                else:
                    print(f"Ignoring invalid rectangle: {parts[1:]}")
            elif shape_type == 'Trapeze':
                try:
                    a, b, c, d = map(float, parts[1:])
                    if a > 0 and b > 0 and c > 0 and d > 0:
                        shapes.append(Trapeze(a, b, c, d))
                    else:
                        print(f"Ignoring invalid trapeze: {parts[1:]}")
                except ValueError as e:
                    print(f"Error processing trapeze: {line.strip()}, {e}")
            elif shape_type == 'Circle':
                r = float(parts[1])
                if r > 0:
                    shapes.append(Circle(r))
                else:
                    print(f"Ignoring invalid circle: {parts[1:]}")
    return shapes

def find_largest_area(shapes):
    if not shapes:
        return None
    return max(shapes, key=lambda x: x.calculate_area())

def find_largest_perimeter(shapes):
    if not shapes:
        return None
    return max(shapes, key=lambda x: x.calculate_perimeter())

shapes1 = read_shapes('input01.txt')
shapes2 = read_shapes('input02.txt')
shapes3 = read_shapes('input03.txt')

all_shapes = shapes1 + shapes2 + shapes3

largest_area_shape = find_largest_area(all_shapes)
largest_perimeter_shape = find_largest_perimeter(all_shapes)

if largest_area_shape:
    print(f"Фігура з найбільшою площею: {largest_area_shape.__class__.__name__}")
    print(f"Площа: {largest_area_shape.calculate_area()}")
else:
    print("Фігура з найбільшою площею не знайдена")

if largest_perimeter_shape:
    print(f"Фігура з найбільшим периметром: {largest_perimeter_shape.__class__.__name__}")
    print(f"Периметр: {largest_perimeter_shape.calculate_perimeter()}")
else:
    print("Фігура з найбільшим периметром не знайдена")
