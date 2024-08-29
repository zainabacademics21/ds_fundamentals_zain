# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:02:58 2024

@author: Sharvari
"""

#function to read matrix
def read_matrix(filename):
    matrix = []
    with open(filename, "r", encoding='utf-8-sig') as file:       #open filename for reading #bom error
        for line in file:
            row = list(map(int, line.strip().split(',')))  #strips whitespaces & splits the lines with comma #stores result in list row
            matrix.append(row)      #appends processed row to matrix list
    return matrix

def multiply_matrices(matrix1, matrix2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #initialize 3x3 matrix
    for i in range(3):              #iterates over the rows of matrix1
        for j in range(3):          #iterates over the columns of matrix2
            for k in range(3):      #terates over the elements of the current row of matrix1 and the current column of matrix2
                result[i][j] += matrix1[i][k] * matrix2[j][k]  
    return result

#function to write the matrix to csv file
def write_matrix(matrix, filename):
    with open(filename, "w") as file:       #open filename for writing
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')  #convert each element in the row to a string, joins element with comma
        
#Read matrix from the csv files
matrix1 = read_matrix('matrix1.csv')
matrix2 = read_matrix('matrix2.csv')
print(matrix1)
print(matrix2)

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Write the result to a new CSV file
write_matrix(result_matrix, 'result_matrix.csv')    #save the oputput in result_matrix in the folder
#print("Resulting Matrix saved in result_matrix , 'result_matrix.csv'")
