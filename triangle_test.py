import math
import pytest


class Triangle:
    def is_exist(self):
        """
        a, b, c - вершины треугольника
        :param a:
        :param b:
        :param c:
        :return: возвращает True если треугольник с указанными координатами может существовать или False
        """
        result = True
        if (self.a[0] == self.b[0] and self.a[1] == self.b[1]) or (self.a[0] == self.c[0] and self.a[1] == self.c[1]) or (self.b[0] == self.c[0] and self.b[1] == self.c[1]):
            result = False
        if result :
            if self.a[0] == self.b[0] == self.c[0] or self.a[1] == self.b[1] == self.c[1]:
                result = False
        return result

    def __init__(self, a, b, c):
        # if self.is_exist():
        self.a = a
        self.b = b
        self.c = c
        # else:
        #     raise NameError('triangle could not exist')
    # aa = list()
    # bb = list()
    # cc = list()

    def side_length(self, point1, point2):
        """
        считает длину стороны треугольника по указанным точкам
        :param point1: координаты вершины треугольника
        :param point2:координаты вершины треугольника
        :return:
        """
        length = math.sqrt(math.pow((point2[0] - point1[0]), 2) + math.pow((point2[1] - point1[1]), 2))
        return length

    def perimeter(self):
        """
        считает периметр треугольника
        :return:
        """
        perimeter = self.side_length(self.a, self.b) + self.side_length(self.a, self.c) + self.side_length(self.b, self.c)
        return round(perimeter, 2)

    def area(self):
        """
        считает площадь треугольника
        :return:
        """
        # p = self.perimeter()
        # a = self.side_length(self.a, self.b)
        # b = self.side_length(self.b, self.c)
        # c = self.side_length(self.c, self.a)
        a = self.a
        b = self.b
        c = self.c
        # s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        s = 0.5 * abs((a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]))
        return s
    # def area(self):



def test_exist_1():
    tri = Triangle([1, 1], [1, 2], [2, 1])
    assert tri.is_exist()


def test_exist_2():
    tri = Triangle([1, 1], [1, 2], [1, 3])
    assert not(tri.is_exist())


def test_exist_3():
    tri = Triangle([1, 1], [2, 3], [2, 3])
    assert not(tri.is_exist())
# tri = Triangle([1, 1], [1, 2], [2, 1])
# print(tri.is_exist())
# print(tri.perimeter())
# print(tri.area())
