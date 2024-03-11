from functions import *

print("========Welcome to Matrix Calculator========")
print("====Programed by Baraa, Rendy, and Ahmed====")
print()


def menu():
    print("Menu:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Transpose Matrix")
    print("5. Determinant Matrix")
    print("6. Inverse Matrix")
    print()

    chose_menu = int(input("Choose a menu: "))
    print()
    if chose_menu == 1:
        print("You chose to add matrices")
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

        print()
        print("Matrix 1 :")
        print_function(matrix_1)

        print("Matrix 2 :")
        print_function(matrix_2)


        # call function add_matrices here
        print("the result of matrix addition is : ")
        result = add_matrices(matrix_1 , matrix_2)
        print_function(result)

        is_repeat_program()


    elif chose_menu == 2:
        print("You chose to subtract matrices")
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

        # call function subtract_matrices here
        print()
        print("Matrix 1 :")
        print_function(matrix_1)
        print()

        print("Matrix 2 :")
        print_function(matrix_2)
        print()

        print("the result of matrix subtraction is : ")
        result = subtract_matrices(matrix_1 , matrix_2)
        print_function(result)
        is_repeat_program()
        

    elif chose_menu == 3:
        print("You chose to multiply matrices")
        number_of_rows_matrix_1 = int(input(f"Enter the number of rows for the first matrix : "))
        number_of_columns_matrix_1 = int(input(f"Enter the number of columns for the first matrix : "))
  
        number_of_rows_matrix_2 = int(input(f"Enter the number of rows for the second matrix : "))
        number_of_columns_matrix_2 = int(input(f"Enter the number of columns for the second matrix : "))

        
        if number_of_columns_matrix_1 == number_of_rows_matrix_2: # Check if the number of columns in the first matrix must be equal to the number of rows in the second matrix.
            # Call the multiplcation function
            matrix_1 = []
            for row in range(number_of_rows_matrix_1):
                row_values = []
                for column in range(number_of_columns_matrix_1):
                    value = int(input(f"Enter a value for the first matrix posation {row + 1},{column + 1}: " )) # We add one because the count in python starts from zero
                    row_values.append(value)
                matrix_1.append(row_values)
                # At the end matrix_1 will look something like this [[5,4] , [6,8] , [9,4]]

            matrix_2 = []
            for row in range(number_of_rows_matrix_2):
                row_values = []
                for column in range(number_of_columns_matrix_2):
                    value = int(input(f"Enter a value for the second matrix posation {row + 1},{column + 1}: " )) # We add one because the count in python starts from zero
                    row_values.append(value)
                matrix_2.append(row_values)
            # At the end matrix_1 will look something like this [[5,4] , [6,8]]
                
            print()
            print("Matrix 1 :")
            print_function(matrix_1)
            print()

            print("Matrix 2 :")
            print_function(matrix_2)
            print()
            
            print("The multiplication result is: ")
            result = multiply_matrices(matrix_1 , matrix_2)
            print('The multiplication result is: ')
            print_function(result)
            is_repeat_program()
        else:
            print("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
            is_repeat_program()

    elif chose_menu == 4:
        print("You chose to transpose a matrix")
        number_of_rows = int(input(f"Enter the number of rows for the matrices : "))
        number_of_columns = int(input(f"Enter the number of columns for the matrices : "))
        matrix = []
        for row in range(number_of_rows):
            row_values = []
            for column in range(number_of_columns):
                value = int(input(f"Enter a value for the matrix posation {row + 1},{column + 1}: " ))
                row_values.append(value)
            matrix.append(row_values)
        print()
        print("The matrix you entered is :")
        print_function(matrix)
        print()
        # call function transpose_matrix here
        print("The transpose of the matrix is : ")
        result = transpose_matrix(matrix)
        print_function(result)
        is_repeat_program()

    elif chose_menu == 5:
        print("You chose to determinant a matrix")

    elif chose_menu == 6:
        print("You chose to inverse a matrix")

    else:
        print("You typed the wrong number")
        is_repeat_program()


def print_function(matrix):
    for row in matrix:
        print(row)
    print()


def is_repeat_program():
    repeat = input("Do you want to repeat the program? (yes/no): ")
    if repeat == "yes":
        menu()
    else:
        print("Thank you for using this program")
        exit()

menu()