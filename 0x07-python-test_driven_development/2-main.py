#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [1, 2, 3],
        [4, 5, 6]
]
print(matrix_divided(matrix, 3))
matrix = [1, 3, [4, 5, 6]]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)

matrix = [[1, 2, 3], [4, 5, 6]]
try:
    print(matrix_divided(matrix, 'joe'))
except Exception as e:
    print(e)

