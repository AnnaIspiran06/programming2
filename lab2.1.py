import math

class Vector:
    def __init__(self, components):
        self.components = list(components)

    def __str__(self):
        return f"Vector({self.components})"

    def dimension(self):
        return len(self.components)

    def length(self):
        return math.sqrt(sum(comp**2 for comp in self.components))

def read_vectors(filename):
    vectors = []
    with open(filename, 'r') as file:
        for line in file:
            components = list(map(float, line.split()))
            vectors.append(Vector(components))
    return vectors

def find_largest_dimension_vector(vectors):
    return max(vectors, key=lambda v: v.dimension())

def find_shortest_vector(vectors):
    return min(vectors, key=lambda v: v.length())

def find_longest_vector(vectors):
    return max(vectors, key=lambda v: v.length())

def average_length(vectors):
    return sum(v.length() for v in vectors) / len(vectors)

def count_above_average_length(vectors):
    avg_length = average_length(vectors)
    return sum(1 for v in vectors if v.length() > avg_length)

# Читаємо вектори з файлів
vectors1 = read_vectors('input011.txt')
vectors2 = read_vectors('input022.txt')
vectors3 = read_vectors('input033.txt')
vectors4 = read_vectors('input044.txt')

largest_dimension_vector = find_largest_dimension_vector(vectors1 + vectors2 + vectors3 + vectors4)
shortest_vector = find_shortest_vector(vectors1 + vectors2 + vectors3 + vectors4)
longest_vector = find_longest_vector(vectors1 + vectors2 + vectors3 + vectors4)
avg_length_all = average_length(vectors1 + vectors2 + vectors3 + vectors4)
count_above_avg_length = count_above_average_length(vectors1 + vectors2 + vectors3 + vectors4)


min_min_comp_vector = min(vectors1 + vectors2 + vectors3 + vectors4, key=lambda v: min(v.components))
max_max_comp_vector = max(vectors1 + vectors2 + vectors3 + vectors4, key=lambda v: max(v.components))
min_min_comp_coordinate = min(min_min_comp_vector.components)
max_max_comp_coordinate = max(max_max_comp_vector.components)


print("Вектор з найбільшою розмірністю та найменшою довжиною:")
print(largest_dimension_vector)
print("Вектор з найбільшою довжиною та найменшою розмірністю:")
print(longest_vector)
print("Середня довжина вектора серед заданого набору:", avg_length_all)
print("Кількість векторів з довжиною більшою за середню:", count_above_avg_length)
print("Вектор з мінімальною компонентою та її значенням:")
print(min_min_comp_vector, min_min_comp_coordinate)
print("Вектор з максимальною компонентою та її значенням:")
print(max_max_comp_vector, max_max_comp_coordinate)
