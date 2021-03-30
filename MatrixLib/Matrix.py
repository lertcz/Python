from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class MatrixException(Exception):
    pass

class Matrix:
    def __init__(self, Row, Col):
        self._row = Row
        self._col = Col
        self._matrix = []

        for x in range(self._row):
            temp = []
            for y in range(self._col):
                temp.append(0)
            
            self._matrix.append(temp)
    
    def printMatix(self):
        for x in range(self._row):
            print(self._matrix[x])
    
    def getItem(self, Row, Col):
        if(not (isinstance(Row, int) or isinstance(Col, int))):
            raise ValueError("Not an integer")
        if(Row < 0 or Row > self._row-1 or Col < 0 or Col > self._col-1):
            raise IndexError("Item out of bound")

        return self._matrix[Row][Col]

    def setItem(self, Row, Col, Val):
        if(not (isinstance(Row, int) or isinstance(Col, int))):
            raise ValueError("Not an integer")
        if(Row < 0 or Row > self._row-1 or Col < 0 or Col > self._col-1):
            raise IndexError("Out of bound")
        
        self._matrix[Row][Col] = Val

    def add(self, matrix):
        mRow = len(matrix)
        mCol = len(matrix[0])
        for element in matrix:
            if(not(len(element) == len(matrix[0]))):
                raise MatrixException("Matrix is not rectengular")
        if(not(mRow == self._row and mCol == self._col)):
            raise MatrixException("Different size of Matrix")
        
        for i in range(mRow):
            for j in range(mCol):
                self._matrix[i][j] += matrix[i][j]

    def sub(self, matrix):
        mRow = len(matrix)
        mCol = len(matrix[0])
        for element in matrix:
            if(not(len(element) == len(matrix[0]))):
                raise MatrixException("Matrix is not rectengular")
        if(not(mRow == self._row and mCol == self._col)):
            raise MatrixException("Different size of Matrix")
        
        for i in range(mRow):
            for j in range(mCol):
                self._matrix[i][j] -= matrix[i][j]
    
    def transpose(self):
        for i in range(self._row): # row
            for j in range(self._col): # col
                if(j > i):
                    symbol1, symbol2 = self._matrix[i][j], self._matrix[j][i]
                    self._matrix[j][i] = symbol1
                    self._matrix[i][j] = symbol2

    def _multiplyConstant(self, num):
        for i in range(self._row):
            for j in range(self._col):
                self._matrix[i][j] *= num

    def _multiplyMatrix(self, matrix):
        if(not(len(self._matrix[0]) == len(matrix))):
            raise MatrixException("Columns don't match rows")
        
        finalMatrix = [[0 for i in range(len(self._matrix))] for j in range(len(matrix[0]))]

        for fMatrixRow in range(len(finalMatrix)):
            for fMatrixCol in range(len(finalMatrix[0])):
                for length in range(len(matrix)):
                    finalMatrix[fMatrixRow][fMatrixCol] += (self._matrix[fMatrixRow][length] * matrix[length][fMatrixCol])

        self._matrix = finalMatrix
    
    def multiply(self, argument):
        if(isinstance(argument, int)):
            Matrix._multiplyConstant(self, argument)
            

        elif(isinstance(argument, list)):
            Matrix._multiplyMatrix(self, argument)