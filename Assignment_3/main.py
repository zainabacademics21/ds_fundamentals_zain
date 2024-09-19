from read_matrix import ReadWriteMatrix
from read_matrix import ReadWriteMatrix
from multiply_matrix import MultiplyMatrices

matrix1 = ReadWriteMatrix.read_matrix("matrix1.csv")
matrix2 = ReadWriteMatrix.read_matrix("matrix2.csv") 

# Multiply the matrices
result_matrix = MultiplyMatrices.multiply_matrices(matrix1, matrix2)

# Write the result to a new CSV file
ReadWriteMatrix.write_matrix(result_matrix, "result_matrix1.csv")

print("Result matrix saved to 'result_matrix1.csv'")