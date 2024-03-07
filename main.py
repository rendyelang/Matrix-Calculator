number_of_rows = int(input(f"Enter the number of rows for the matrices : "))
number_of_columns = int(input(f"Enter the number of columns for the matrices : "))


matrix_1 = []
for row in range(number_of_rows):
    row_values = []
    for column in range(number_of_columns):
        value = int(input(f"Enter a value for the first matrix posation {row + 1},{column + 1}: " )) # We add one because the count in python starts from zero
        row_values.append(value)
    matrix_1.append(row_values)
    # At the end matrix_1 will look something like this [[5,4] , [6,8] , [9,4]]

matrix_2 = []
for row in range(number_of_rows):
    row_values = []
    for column in range(number_of_columns):
        value = int(input(f"Enter a value for the second matrix posation {row + 1},{column + 1}: " )) # We add one because the count in python starts from zero
        row_values.append(value)
    matrix_2.append(row_values)
    # At the end matrix_1 will look something like this [[5,4] , [6,8] , [9,4]]


def add_matrices(matrix1 , matrix2):
    result = []
    # By Rendy


    return result

def multiply_matrices(matrix1 , matrix2):
    result = []
    # By Baraa


    return result

def subtract_matrices(matrix1 , matrix2):
    result = []
    # By Ahmed


    return result

