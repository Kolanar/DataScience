from typing import List

Vector = List[float]

"""
Сложение двух векторов
"""
def add(v: Vector, w: Vector) -> Vector:
    """Складывает соответствующие элементы"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 4], [4, 5, 6]) == [5, 7, 10]

"""
Получение разности двух векторов
"""
def subtract(v: Vector, w: Vector) -> Vector:
    """Вычесляет соответствующие элементы"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

"""
Покомпонентная сумма списка векторов
"""
def vector_sum(vectors: List[Vector]) -> Vector:
    """Суммирует все соответствующие элементы"""
    # Проверить что векторы не пустые
    assert vectors, 'векторый не предоставлены'

    # Проверить что векторы имеют одинаковый размер
    num_elems = len(vectors[0])
    assert all(len(v) == num_elems for v in vectors), 'разнве размеры'

    # i-элемент результата является суммой каждого элемента vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elems)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

"""
Умножение вектора на скаляр
"""
def scalar_multiply(c: float, v: Vector) -> Vector:
    """Умножает каждый элемент на c"""

    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


"""
Покомпонентное среднее значение списка векторов
"""
def vector_mean(vectors: List[Vector]) -> Vector:
    """Вычисляет поэлементное среднее арифмитическое"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


"""
Скалярное произведение 
"""
def dot(v: Vector, w: Vector) -> float:
    """Вычисляет v_1 * w_1 + ... v_n * w_n"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

"""Сумма квадратов вектора"""
def sum_of_squares(v: Vector) -> float:
    """Возвращает v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3])  # 1 * 1 + 2 * 2 + 3 * 3

# И эту же функцию можно применить для вычисления магнитуды (или длины) вектора

import math


def magnitude(v: Vector) -> float:
    """Возвращает магнитуду (или длину) вектора"""
    # math.sqrt - это функция квадратного корня
    return math.sqrt(sum_of_squares(v))

"""Квадрат растояния между двумя векторами"""
def squared_distance(v: Vector, w: Vector) -> float:
    """Вычисляет (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v,w))

"""Растояние между двумя векторами"""
def distance(v: Vector, w: Vector) -> float:
    """Вычисляет расстояние между v и w"""
    return math.sqrt(squared_distance(v,w))
