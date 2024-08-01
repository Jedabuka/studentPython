import math


class Figure:
    sides_count = 0

    def __init__(self, __sides: int, __color: (int, int, int), filled: bool = False):
        pass

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

    def __init__(self, color_cir: (int, int, int), side_cir, __radius):
        self.color_cir = color_cir
        self.side_cir = side_cir
        self.__radius = __radius



    def get_radius(self):
        __radius = round(side_cir / (2 * 3.14), 2)
        return __radius


    def get_square_circle(self):
        square_cir = round(3.14 * __radius ** 2, 2)
        return square_cir


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color_tri: (int, int, int), side_1: int, side_2: int, side_3: int, __height):
        self.color_tri = color_tri
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.__height = __height

    def get_square_triangle(self):
        half_meter = (side_1 + side_2 + side_3) / 2
        square_tri = math.sqrt((half_meter * (half_meter - side_1) * (half_meter - side_2) * (half_meter - side_3)))
        square_tri = round(square_tri, 2)
        return square_tri

    def get_height(self):
        height_tri = 2 * square_tri / side_2
        return height_tri



class Cube(Figure):
    pass


print(Circle.mro())
print(Triangle.mro())
print(Cube.mro())