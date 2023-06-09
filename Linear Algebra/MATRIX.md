# Матрицы

**Матрицы** - это двумерная коллекция чисел. Сейчас мы будем реализовывать матрицы как списки списков,
где все внутренние списки имеют одинаковый размер и представляют строку матрицы. Если А - это матрица,
то А[i][j] - это элемент в i-строчке и j-м столбце.

    Matrix = List[List[float]]
    
    A = [[1,2,3], # Матрица A имеет 2 строки и 3 стоблца
         [4,5,6]]

    B = [[1,2],   # Матрица B имеет 3 строки и 2 столбца
         [3,4],
         [5,6]]

Представленная в виде списка списков матрица А имеет len(A) строк и len(A[0]) столбцов.
Эти значения образуют форму матрицы

    from typing import Typle

    def shape(A: Matrix) -> Typle[int, int]:
        """Возвращает (Число строк A, число столбцов A)"""
        num_rows = len(A)
        num_cols = len(A[0]) if A else 0 # Число элементов в первой строке
        return num_rows, num_cols

    assert shape([[1,2,3],[4,5,6]]) == (2,3) # 2 строки, 3 столбца

Если матрица имеет N строк и K столбцов, то мы будем говорить, что это (N x K) - матрица,
или матрица размера N x K. Каждая строка (N x K) - матрицы может быть представлена вектором длины K,
 а каждый столбец - вектором длины N.

    def get_row(A: Matrix, i: int) -> Vector:
        """Возвращает i-ю строку A (как тип Vector)"""
        return A[i]  #A[i] является i-й строкой

    def get_column(A: Matrix, j: int) -> Vector:
        """Возвращает j-й столбец A (как тип Vector)"""
        return [A_i[j]          # j-й элемент строки A_i
                for A_i in A    # для каждой строки A_i

Так же есть возможность создавать матрицу при наличии её формы и фунции, которая генерирует ее элементы.
Это можно сделать на основе вложеного включения в список.
    
    from typing improt Callable

    def make_matrix(num_rows: int,
                    num_cols: int,
                    entry_fn: Callable[[int, int], float]) -> Matrix:

    """Возвращает матрицу размера num_rows x num_cols,
       чей (i,j)-й элемент является функцией entry_fn(i,j)"""
    
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_cols)]

при наличии этой функции можно, например создать (5х5) - матрицу тоджественности (с единицами по
диагонали и нулями в остальных элементах)




