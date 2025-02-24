import numpy as np

def get_matrix(name):
    while True:
        try:
            rows, cols = map(int, input("Enter the number of rows and columns for " + name + " matrix (e.g., 2 3 for 2x3): ").split())
            if rows <= 0 or cols <= 0:
                print("Matrix size must be positive integers.")
                continue
            
            print("Enter the elements of the " + name + " matrix row-wise (space-separated):")
            matrix = [list(map(float, input().split())) for _ in range(rows)]
            
            if any(len(row) != cols for row in matrix):
                print("Error: Expected " + str(cols) + " values in each row.")
                continue
            
            return np.array(matrix)
        
        except ValueError:
            print("Invalid input. Please enter numbers correctly.")

def display_matrix(matrix, name):
    print("\n" + name + " Matrix:")
    print(matrix)

def matrix_operations():
    while True:
        print("\nChoose a Matrix Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice in ['1', '2', '3']:
            A = get_matrix("First")
            B = get_matrix("Second")

            if A.shape != B.shape and choice != '3':
                print("Error: Matrices must be of the same size for addition and subtraction.")
                continue
            
            if choice == '1':
                result = A + B
                operation = "Addition"
            elif choice == '2':
                result = A - B
                operation = "Subtraction"
            else:
                if A.shape[1] != B.shape[0]:
                    print("Error: The number of columns in the first matrix must equal the number of rows in the second.")
                    continue
                result = np.dot(A, B)
                operation = "Multiplication"
            
            display_matrix(result, operation)

        elif choice == '4':
            A = get_matrix("Input")
            display_matrix(A.T, "Transpose")

        elif choice == '5':
            A = get_matrix("Square")
            if A.shape[0] != A.shape[1]:
                print("Error: Determinant can only be computed for square matrices.")
                continue
            print("\nDeterminant: " + str(round(np.linalg.det(A), 2)))

        elif choice == '6':
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Exiting the program.")
                break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    matrix_operations()