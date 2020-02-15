# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод init()), который должен принимать данные (список списков)
# для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
# в привычном виде.
#
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.



class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix_f = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix_f[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_f]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_f]))


my_matrix = Matrix([[8, 56, 8],[9, 2, 3],[8, 5, 9]],
                   [[77, 9, 3], [3, 5, 9],[86, 45, 5]])

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
# на реальных данных.Реализовать общий подсчет расхода ткани. Проверить на практике
# полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def result_a(self):
        return self.width / 6.5 + 0.5

    def result_b(self):
        return 2 * self.length + 0.3

    @property
    def get_cl(self):
        return str(f'Общее количество ткани - {(self.width / 6.5 + 0.5) + (2 * self.length + 0.3)}')

class Coat(Clothes):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.result_1 = round((self.width / 6.5 + 0.5))

    def __str__(self):
        return f'Количество ткани на пальто - {self.result_1}'

class Costume(Clothes):
    def __init__(self, width, length):
        super().__init__(width, length)
        self.result_2 = round(2 * self.length + 0.3)


    def __str__(self):
        return f'Количество ткани на костюм - {self.result_2}'



coat = Coat(30, 9)
costume = Costume(10, 5)
print(coat)
print(costume)
print(coat.get_cl)
print(costume.get_cl)
print(f'Костюм - {costume.result_a()}')
print(f'Костюм - {costume.result_b()}')
print(f'Пальто - {coat.result_a()}')
print(f'Пальто - {coat.result_b()}')