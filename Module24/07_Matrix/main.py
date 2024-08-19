class Matrix:
    def __init__(self, rows, colums):
        self.rows = rows
        self.colums = colums
        self.data = []

    def __str__(self):
        for i_row in self.data:
            for j_colum in i_row:
                print(j_colum, end='\t')
            print()
        return ''

    def add(self, matrix):
        for i_row in range(self.rows):
            for j_colum in range(self.colums):
                print(self.data[i_row][j_colum] + matrix.data[i_row][j_colum], end='\t')
            print()
        return ''

    def subtract(self, matrix):
        for i_row in range(self.rows):
            for j_colum in range(self.colums):
                print(self.data[i_row][j_colum] - matrix.data[i_row][j_colum], end='\t')
            print()
        return ''

    def multiply(self, matrix):
        if self.colums == matrix.rows:
            for i_row in range(self.rows):
                for z_colum in range(matrix.colums):
                    res = 0
                    for j_colum in range(self.colums):
                        res += self.data[i_row][j_colum] * matrix.data[j_colum][z_colum]
                    print(res, end='\t')
                print()
        else:
            return 'Такие матрицы умножить нельзя\n'
        return ''

    def transpose(self):
        result = Matrix(self.colums, self.rows)
        for i_row in range(result.rows):
            result.data.append([])
            for j_colum in range(result.colums):
                # result.data[i_row].append([])
                # result.data[i_row][j_colum] = self.data[j_colum][i_row]
                result.data[i_row].append(self.data[j_colum][i_row])
        return result

m1 = Matrix(2, 3)
m1.data = [[1, 2, 3],
           [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9],
           [10, 11, 12]]

m3 = Matrix(3, 2)
m3.data = [[1, 2],
           [3, 4],
           [5, 6]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())