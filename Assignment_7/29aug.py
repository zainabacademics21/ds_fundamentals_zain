#finds and returns the longest contiguous sequence of 1s in any horizontal slice of the matrix, 
#along with the starting position of this sequence.

import numpy as np

def generate_matrix(x, y, z):        #generate 3d matrix with indices x,y,z
    matrix = np.zeros((x, y, z), dtype=int)
    
    for i in range(x):
        for j in range(y):
            for k in range(z):
                sum = i + j + k
                if (sum % 10 == 2) or (sum % 10 == 6):
                    matrix[i, j, k] = 0  # Even sum of indices
                else:
                    matrix[i, j, k] = 1  # Odd sum of indices
    
    return matrix

def longest_substring(matrix):
    x, y, z = matrix.shape
    max_length = 0
    max_position = None
    longest_coordinates = []  # List to store the coordinates of the longest substring
    
    for i in range(x):
        for j in range(y):
            current_length = 0
            current_coordinates = []  # Temporarily store coordinates for the current row
            
            for k in range(z):
                if matrix[i, j, k] == 1:
                    current_coordinates.append((i, j, k))  # Store the coordinate
                    current_length += 1
                    
                    if current_length > max_length:
                        max_length = current_length
                        max_position = (i, j, k - current_length + 1)
                        longest_coordinates = current_coordinates.copy()  # Update the longest coordinates
                else:
                    current_length = 0
                    current_coordinates = []  #Reset the temporary coordinates if a 0 is encountered
    
    return max_length, max_position, longest_coordinates

# Example usage:
x_dim, y_dim, z_dim = 7, 5, 3
# Generate the 3D matrix
matrix = generate_matrix(x_dim, y_dim, z_dim)

# Output the matrix
for i in range(x_dim):
    for j in range(y_dim):
        for k in range(z_dim):
            print(f"matrix[{i}][{j}][{k}] = {matrix[i][j][k]}")
        print()
    print()

#longest_length, start_position = longest_substring(matrix)
longest_length, start_position, coordinates = longest_substring(matrix)
print(f"Longest substring of 1s length: {longest_length}")
print(f"Starting position of longest substring: {start_position}")
print("Coordinates of longest substring:")
for coord in coordinates:
    print(coord)

#o/p:longest substring, its starting position, and all the coordinates that are part of this substring.