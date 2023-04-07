from numbers import Number
import itertools
import copy
from exeptions import *
class Matrix:
    
    def __init__(self, list_of_lists = 0):
        # проверка корректонсти ввода:
        if isinstance(list_of_lists, list):
            if all(isinstance(l, Number) for l in list_of_lists):
                list_of_lists = [[list_of_lists[i]] for i in range(len(list_of_lists))]
            elif not(all(isinstance(l, list) for l in list_of_lists)):
                raise MatrixTypeError("You are trying to create matrix from " + repr(list_of_lists))
            if not(all(len(i) == len(list_of_lists[0]) for i in list_of_lists)):
                raise MatrixDimensionError("You are trying to create a matrix with variable row size")
            elif all([(isinstance(i, Number) and isinstance(l, list)) for l in list_of_lists for i in l]):
                self.body = copy.deepcopy(list_of_lists)
                self.m = len(self.body)
                self.n = len(self.body[0]) 
            else:
                raise MatrixTypeError("You are trying to create matrix from " + repr(list_of_lists))
            
    def size(self):
        sizepair = (self.m, self.n)
        return sizepair
    
    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self.body)
    
    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            return False
        elif all(self.body[i][j] == other.body[i][j] for i in range(m) for j in range(n)):
            return True
        else:
            return False
    
    def __add__(self, other):
        # только если одного размера
        if self.m == other.m and self.n == other.n:
            return Matrix(copy.deepcopy([[self.body[i][j] + other.body[i][j] for j in range(self.n)] for i in range(self.m)]))
        else:
            raise MatrixSizeError("You are trying to sum matrices of different sizes")
    
    def __mul__(self, other):
        # операция умножения(в том числе на константу)
        if isinstance(other, Number):
            return Matrix(copy.deepcopy([[other*self.body[i][j] for j in range(self.n)] for i in range(self.m)]))
        elif not(isinstance(other, Matrix)):
            raise MatrixTypeError("You are trying to multiply the matrix by " + repr(x))
        # число столбцов первой матрицы равно числу строк второй матрицы
        elif self.n == other.m:
            m_mul = [[0 for i in range(other.n)] for j in range(self.m)]
            for i in range(other.n):
                # иду по столбикам второй матрицы
                for j in range(self.m):
                    # иду по строкам первой матрицы
                    for k in range(self.n):
                        # иду по элементам строки(столбикам) первой матрицы и по элементам столбика(строкам) второй матрицы
                        m_mul[j][i] += self.body[j][k] * other.body[k][i]
            return Matrix(copy.deepcopy(m_mul))
        else:
            raise MatrixSizeError("The number of columns of the first matrix is not equal to the number of rows of the second")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __neg__(self):
        return self.__mul__(-1)
    
    def __sub__(self, other):
        if self.m == other.m and self.n == other.n:
            return self.__add__(other.__mul__(-1))
        else:
            raise MatrixSizeError("You are trying to subtract matrices of different sizes")
    
    def __rsub__(self, other):
        if self.m == other.m and self.n == other.n:
            return other.__add__(self.__mul__(-1))
        else:
            raise MatrixSizeError("You are trying to subtract matrices of different sizes")
    
    def transpose(self):
        transposed = [[row[i] for row in self.body] for i in range(self.n)]
        return(Matrix(copy.deepcopy(transposed)))