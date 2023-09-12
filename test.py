import numpy as np

class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def create(self):
        try:
            matrix_rows = int(input('Введите количество строк [1/100]: '))
            matrix_cols = int(input('Введите количество столбцов [1/100]: '))
            if matrix_rows >= 1 and matrix_rows <= 100:
                if matrix_cols >= 1 and matrix_cols <= 100:
                    print(f'Матрица будет {matrix_rows} на {matrix_cols}')
                    action_matrix = int(input('Введите действие с матрицей [1 - плюс | 2 - минус | 3 - умножить]:'))
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

    def plus(self):
        ...
    def minus(self):
        ...
    def multi(self):
        ...

if __name__ == "__main__":
    matrix_instance = matrix(0, 0)
    print(matrix_instance.create()) 

    