from typing import List

Vector = List[float]

"""
Сложение двух векторов
"""

def add(v: Vector, w: Vector) -> Vector:
    """Складывает соответствующие элементы"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'

    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1,2,4],[4,5,6]) == [5,7,10]

"""
Получение разности двух векторов
"""

def subtract(v: Vector, w: Vector) -> Vector:
    """Вычесляет соответствующие элементы"""
    assert len(v) == len(w), 'Векторы должны иметь одинаковую длину'

    return [v_i - w_i for v_i, w_i in zip(v,w)]
assert subtract([5,7,9],[4,5,6]) == [1,2,3]


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

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]


"""
Умножение вектора на скаляр
"""

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Умножает каждый элемент на c"""

    return [c * v_i for v_i in v]

assert scalar_multiply(2,[1,2,3]) == [2,4,6]
