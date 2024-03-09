def add_matrices(matrix1, matrix2):
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

def check_multiplication_validity(matrix_1 , matrix_2):
    # The rule is: the number of columns in the first matrix must be equal to the number of rows in the second matrix.
    number_of_columns_first_matrix = len(matrix_1[0]) # E.g. if matrix_1 = [[1,2] , [3,4] , [5,6]], matrix_1[0] will be [1,2] so len(matrix_1) will be 2, which is the number of columns.
    number_of_rows_second_matrix = len(matrix_2) # E.g. if matrix_2 = [[1,2] , [3,4] , [5,6]], len(matrix_2) will be 3, which is the number of rows.
    
    if number_of_columns_first_matrix == number_of_rows_second_matrix:
        is_valid = True
    else:
        is_valid = False
    
    return is_valid
