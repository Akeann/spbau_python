from matrix_class import Matrix

print('первая матрица:')
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
ma = Matrix(a)
print(ma)

print('вторая матрица:')
b = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
mb = Matrix(b)
print(mb)

# сумма матриц
ab_sum = ma + mb
print('их сумма:')
print(ab_sum)

# разность матриц
print('разность:')
ab_sub = ma - mb
print(ab_sub)

# произведение матриц
print('произведение:')
print(ma*mb)

# размер матрицы(число строк, число столбцов)
print('размер первой матрицы:')
print(ma.size())

# транспонирование матриц
print('транспонированная первая матрица:')
print(ma.transpose())