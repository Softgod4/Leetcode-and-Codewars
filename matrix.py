import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix1 = []
        self.matrix2 = []

    def create(self):
        try:
            matrix_rows = int(input('Введите количество строк [1/100]: '))
            matrix_cols = int(input('Введите количество столбцов [1/100]: '))
            if matrix_rows >= 1 and matrix_rows <= 100:
                if matrix_cols >= 1 and matrix_cols <= 100:
                    print(f'Матрица 1 будет {matrix_rows} на {matrix_cols}')
                    self.rows = matrix_rows
                    self.cols = matrix_cols
                    self.matrix1 = self.create_matrix(matrix_rows, matrix_cols)

                    print(f'Матрица 2 будет {matrix_rows} на {matrix_cols}')
                    self.matrix2 = self.create_matrix(matrix_rows, matrix_cols)

                    print('Матрицы успешно созданы!')

                    action_matrix = int(input('Введите действие с матрицей [1 - плюс | 2 - минус | 3 - умножить]: '))
                    if action_matrix == 1:
                        self.plus()
                    elif action_matrix == 2:
                        self.minus()
                    elif action_matrix == 3:
                        self.multi()
                    else:
                        print('Неверный выбор действия!')
                        return self.create()

                else:
                    print('Введите числа от 1 до 100!')
                    return self.create()
            else:
                print('Введите числа от 1 до 100!')
                return self.create()
        except ValueError:
            print('Введите числа от 1 до 100!')
            return self.create()

    def create_matrix(self, rows, cols):
        matrix = np.random.randint(1, 10, size=(rows, cols))
        return matrix

    def plus(self):
        plus = self.matrix1 + self.matrix2
        print(plus)

    def minus(self):
        minus = self.matrix1 + self.matrix2
        print(minus)

    def multi(self):
        dot = self.matrix1.dot(self.matrix2)
        print(dot)


if __name__ == "__main__":
    matrix_instance = Matrix(0, 0)
    matrix_instance.create()
