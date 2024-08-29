# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:26:18 2024

@author: Sharvari
"""

class MultiplyMatrices:
    def multiply_matrices(matrix1, matrix2):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #initialize 3x3 matrix
        for i in range(3):              #iterates over the rows of matrix1
            for j in range(3):          #iterates over the columns of matrix2
                for k in range(3):      #terates over the elements of the current row of matrix1 and the current column of matrix2
                    result[i][j] += matrix1[i][k] * matrix2[j][k]  
        return result