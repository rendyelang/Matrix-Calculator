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
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)

    return result

def is_repeat_program():
    repeat = input("Do you want to repeat the program? (yes/no): ")
    if repeat == "yes":
        from main import menu
        menu()
    else:
        print("Thank you for using this program")
        exit()