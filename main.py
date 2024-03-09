from functions import *

print("========Welcome to Matrix Calculator========")
print("====Programed by Baraa, Rendy, and Ahmed====")
print()


def menu():
    print("Menu:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
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


        # call function add_matrices here

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

    elif chose_menu == 3:
        print("You chose to multiply matrices")
        number_of_rows_matrix_1 = int(input(f"Enter the number of rows for the first matrix : "))
        number_of_columns_matrix_1 = int(input(f"Enter the number of columns for the first matrix : "))
  
        number_of_rows_matrix_2 = int(input(f"Enter the number of rows for the second matrix : "))
        number_of_columns_matrix_2 = int(input(f"Enter the number of columns for the second matrix : "))


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
        
        if number_of_columns_matrix_1 == number_of_rows_matrix_2: # Check if the number of columns in the first matrix must be equal to the number of rows in the second matrix.
            # Call the multiplcation function
            result = multiply_matrices(matrix_1 , matrix_2)
            print('The multiplication result is: ')
            for row in result:
                print(row)
        else:
            print("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")


    else:
        print("You typed the wrong number")
        repeat = input("Do you want to repeat the program? (yes/no): ")
        if repeat == "yes":
            menu()
        else:
            print("Thank you for using this program")
            exit()


menu()


