class ReadWriteMatrix:
    #function to read matrix
    def read_matrix(filename):
        matrix = []
        with open(filename, "r", encoding='utf-8-sig') as file:       #open filename for reading #bom error
            for line in file:
                row = list(map(int, line.strip().split(',')))  #strips whitespaces & splits the lines with comma #stores result in list row
                matrix.append(row)      #appends processed row to matrix list
        return matrix
    
    #function to write the matrix to csv file
    def write_matrix(matrix, filename):
        with open(filename, "w") as file:       #open filename for writing
            for row in matrix:
                file.write(','.join(map(str, row)) + ' \n')  #convert each element in the row to a string, joins element with comma 
                