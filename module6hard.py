import math


class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        if self.__is_valid_sides(*__sides):
            if isinstance(self, Cube):
                self.__sides = list(__sides) * self.sides_count
            else:
                self.__sides = list(__sides)
        else:
            self.__sides = [1] * self.sides_count

        self.__color = list(__color) if self.__is_valid_color(*__color) else [0, 0, 0]
        self.filled = False

    def get_color(self):   # список RGB цветов
        return self.__color

        # служебный, принимает параметры r, g, b, который проверяет корректность
        # переданных значений перед установкой нового цвета. Корректным цвет: все
        # значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

        # изменяет атрибут __color на соответствующие значения, предварительно проверив их
        # на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

        # принимает неограниченное кол-во сторон, возвращает True если все стороны целые
        # положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.
    def __is_valid_sides(self, *__sides):
        if all(isinstance(side, int) and side > 0 for side in __sides):
            if len(__sides) == self.sides_count:
                return True
            elif isinstance(self, Cube) and len(__sides) == 1:
                return True
        else:
            return False

    def get_sides(self):  # должен возвращать значение я атрибута __sides.
        return self.__sides

    def __len__(self):  # должен возвращать периметр фигуры.
        return sum(self.__sides)

        # должен принимать новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides) * self.sides_count
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__radius = self.__get_radius()

    def __get_radius(self):
        return self.get_sides()[0] / (2 * 3.14)

    def get_radius(self):
        return self.__radius

    def get_square_circle(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__height = self.__get_height()

    def get_square_triangle(self):
        half_metr = sum(self.get_sides()) / 2
        return math.sqrt((half_metr * (half_metr - self.get_sides()[0]) * (half_metr - self.get_sides()[1]) *
                          (half_metr - self.get_sides()[2])))

    def __get_height(self):
        return 2 * self.get_square_triangle() / self.get_sides()[1]

    def get_height(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)

    def get_volume(self):
        return math.pow(self.get_sides()[0], 3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print('\nКруг:')
circle1 = Circle((200, 200, 100), 10)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square_circle())
print('радиус:', circle1.get_radius())
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 3)
print('цвета:', circle1.get_color())
circle1.set_color(-1, 200, 3)
print('цвета:', circle1.get_color())
circle1.set_color(1, 2, 300.0)
print('цвета:', circle1.get_color())
circle1.set_sides(15)
print('стороны:', circle1.get_sides())
print('прощадь:', circle1.get_square_circle()) # не меняет площадь
print('радиус:', circle1.get_radius()) # не меняет радиус
circle1.set_sides(10, 9)
print('стороны:', circle1.get_sides())

print('\nТреугольник:')
tri = Triangle((200, 200, 100), 10)
print('стороны:', tri.get_sides())
print('прощадь:', tri.get_square_triangle()) # + получение высоты треугольника
print('цвета:', tri.get_color())

tri = Triangle((200, 200, 100), 10, 7, 9)
print('стороны:', tri.get_sides())
tri.set_sides(1)
print('стороны:', tri.get_sides())
tri.set_sides(1, 2, 3)
print('стороны:', tri.get_sides())
tri.set_sides(1, 2, -3)
print('стороны:', tri.get_sides())

print('\nКуб:')
cub = Cube((200, 200, 100), 10, 12)
print('стороны:', cub.get_sides())
print('объём:', cub.get_volume())
print('цвета:', cub.get_color())

cub = Cube((200, 200, 100), 10)
print('стороны:', cub.get_sides())
cub.set_sides(50)
print('стороны:', cub.get_sides())
cub.set_sides(-100)
print('стороны:', cub.get_sides())
cub.set_sides(1, 2, 3)
print('стороны:', cub.get_sides())
cub.set_sides(1, 2, -3)
print('стороны:', cub.get_sides())
