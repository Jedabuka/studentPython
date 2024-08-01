import math


class Figure:
    sides_count = 0
    list_sides = []

    def __init__(self, __color: (int, int, int), *__sides: int, filled: bool = False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        for i in __sides:
            Figure.list_sides.append(i)

    def get_color(self):   # список RGB цветов
        return

        # служебный, принимает параметры r, g, b, который проверяет корректность
        # переданных значений перед установкой нового цвета. Корректным цвет: все
        # значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        pass

        # изменяет атрибут __color на соответствующие значения, предварительно проверив их
        # на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        pass

        # принимает неограниченное кол-во сторон, возвращает True если все стороны целые
        # положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.
    def __is_valid_sides(self):
        pass

    def get_sides(self):  # должен возвращать значение я атрибута __sides.
        pass

    def __len__(self):  # должен возвращать периметр фигуры.
        pass

        # должен принимать новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: (int, int, int), *__sides: int, filled: bool = False):
        super().__init__(__color, __sides)
        self.__color = __color
        self.__sides = __sides
        self.__radius = Circle.get_radius(self)
        self.filled = filled

    def get_radius(self):
        self.__radius = round(self.__sides / (2 * 3.14), 2)
        return self.__radius

    def get_square_circle(self):
        square_cir = round(3.14 * self.__radius ** 2, 2)
        return self.square_cir


# class Triangle(Figure):
#     sides_count = 3
#
#     def __init__(self, __color: (int, int, int), *__sides: int, __height, filled: bool = False):
#         super().__init__(__color, __sides)
#         self.__color = __color
#         self.__sides = __sides
#         self.filled = filled
#         self.__height = __height
#
#     def get_square_triangle(self):
#         half_meter = (side_1 + side_2 + side_3) / 2
#         square_tri = math.sqrt((half_meter * (half_meter - side_1) * (half_meter - side_2) * (half_meter - side_3)))
#         square_tri = round(square_tri, 2)
#         return square_tri
#
#     def get_height(self):
#         height_tri = 2 * square_tri / side_2
#         return height_tri



class Cube(Figure):
    pass

circle1 = Circle((200, 200, 100), 10)