def matrix_operation():
    def create_matrix(rows, cols):
        matrix = []
        print("Введіть елементи матриці розділені пробілами та рядки через Enter:")
        for _ in range(rows):
            while True:
                row = input().split()
                if len(row) != cols:
                    print("Неправильна кількість елементів у рядку. Спробуйте ще раз.")
                else:
                    matrix.append(list(map(float, row)))
                    break
        return matrix

    def determinant(matrix):
        n = len(matrix)
        if n != len(matrix[0]):
            print("Матриця повинна бути квадратною для обчислення визначника.")
            return None

        det = 0
        if n == 1:
            det = matrix[0][0]
        elif n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            for j in range(n):
                sign = (-1) ** j
                minor = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
                det += sign * matrix[0][j] * determinant(minor)
        return det

    def multiply_by_scalar(matrix, scalar):
        result_matrix = [[element * scalar for element in row] for row in matrix]
        return result_matrix

    def inverse_matrix(matrix):
        n = len(matrix)
        if n != len(matrix[0]):
            print("Матриця повинна бути квадратною для знаходження оберненої.")
            return None

        identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        augmented_matrix = [row + identity_matrix[i] for i, row in enumerate(matrix)]

        for i in range(n):
            for j in range(i, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[i], augmented_matrix[j] = augmented_matrix[j], augmented_matrix[i]
                    break
            else:
                print("Матриця не має оберненої.")
                return None

            pivot = augmented_matrix[i][i]
            for j in range(i, 2 * n):
                augmented_matrix[i][j] /= pivot
            for j in range(n):
                if j != i:
                    factor = augmented_matrix[j][i]
                    for k in range(2 * n):
                        augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

        inverse = [row[n:] for row in augmented_matrix]
        return inverse

    while True:
        rows = int(input("Введіть кількість рядків матриці: "))
        cols = int(input("Введіть кількість стовпчиків матриці: "))
        matrix = create_matrix(rows, cols)
        if matrix is not None:
            break

    while True:
        operation = input("Виберіть операцію (determinant/multiply/inverse): ")
        if operation in ["determinant", "multiply", "inverse"]:
            break
        else:
            print("Неправильна операція. Спробуйте ще раз.")

    if operation == "determinant":
        det = determinant(matrix)
        if det is not None:
            print(f"Визначник матриці: {det}")
    elif operation == "multiply":
        scalar = float(input("Введіть число, на яке потрібно помножити матрицю: "))
        result_matrix = multiply_by_scalar(matrix, scalar)
        print("Результат множення матриці на число:")
        for row in result_matrix:
            print(" ".join(map(str, row)))
    elif operation == "inverse":
        inv_matrix = inverse_matrix(matrix)
        if inv_matrix is not None:
            print("Обернена матриця:")
            for row in inv_matrix:
                print(" ".join(map(str, row)))


