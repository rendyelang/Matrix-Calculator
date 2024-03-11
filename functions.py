def add_matrices(matrix1, matrix2):
    result = []
    # By Rendy
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def multiply_matrices(matrix1 , matrix2):
    result = []
    # By Baraa
    result = []
    number_of_columns_matrix2 =  len(matrix2[0])
    number_of_rows_matrix1 =  len(matrix1)

    # Step 1: Extract columns from matrix 2
    matrix2_columns = []
    for column_number in range(0 , number_of_columns_matrix2):
        result_row = []
        column_from_matrix_2 = []
        for row in matrix2:
            column_from_matrix_2.append(row[column_number])
        matrix2_columns.append(column_from_matrix_2)
    
    # Step 2: calulate the dot_product by multiplying each row in matrix 1 by each column in matrix 2
    for row in matrix1: # Remember, len(row) == len(column_from_matrix_2)
        result_row = []
        for column in matrix2_columns:
            dot_product = []
            for value in range(0, len(column)):  
                dot_product.append(column[value] * row[value])
            dot_product = sum(dot_product)
            result_row.append(dot_product)
        result.append(result_row)


    return result

def subtract_matrices(matrix1 , matrix2):
    # By Ahmed
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result

def transpose_matrix(matrix):
    # By Rendy
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)

    return result

def determinant_matrix(matrix):
    # By Baraa
    result = []



    return result

def inverse_matrix(matrix):
    # By Ahmed
    result = []



    return result

def is_repeat_program():
    repeat = input("Do you want to repeat the program? (yes/no): ")
    if repeat == "yes":
        from main import menu
        menu()
    else:
        print("Thank you for using this program")
        exit()