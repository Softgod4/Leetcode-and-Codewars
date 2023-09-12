import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix1 = []
        self.matrix2 = []

    def Create(self):
        try:
            matrix_rows = int(input('Введите количество строк [1/100]: '))
            matrix_cols = int(input('Введите количество столбцов [1/100]: '))
            if matrix_rows >= 1 and matrix_rows <= 100:
                if matrix_cols >= 1 and matrix_cols <= 100:
                    print(f'Матрица 1 будет {matrix_rows} на {matrix_cols}')
                    self.rows = matrix_rows
                    self.cols = matrix_cols
                    self.matrix1 = self.Create_matrix(matrix_rows, matrix_cols)

                    print(f'Матрица 2 будет {matrix_rows} на {matrix_cols}')
                    self.matrix2 = self.Create_matrix(matrix_rows, matrix_cols)

                    print('Матрицы успешно созданы!')

                    action_matrix = int(input('Введите действие с матрицей [1 - плюс | 2 - минус | 3 - умножить]: '))
                    match action_matrix:
                        case 1:
                            self.Plus()
                        case 2:
                            self.Minus()
                        case 3:
                            self.Multi()
                        case _:
                            print('Неверный выбор действия!')
                            return self.Create()

                else:
                    print('Введите числа от 1 до 100!')
                    return self.Create()
            else:
                print('Введите числа от 1 до 100!')
                return self.Create()
        except ValueError:
            print('Введите числа от 1 до 100!')
            return self.Create()

    def Create_matrix(self, rows, cols):
        matrix = np.random.randint(1, 10, size=(rows, cols))
        return matrix

    def Plus(self):
        plus = self.matrix1 + self.matrix2
        print(plus)

    def Minus(self):
        minus = self.matrix1 - self.matrix2
        print(minus)

    def Multi(self):
        dot = self.matrix1.dot(self.matrix2)
        print(dot)

if __name__ == "__main__":
    matrix_instance = Matrix(0, 0)
    matrix_instance.Create()
