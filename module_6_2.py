class Vehicle:
    __COLOR_VARIANTS = ['bLack', 'Orange', 'YelloW', 'whIte', 'rEd']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        result_1 = self.get_model()
        print(result_1)
        result_2 = self.get_horsepower()
        print(result_2)
        result_3 = self.get_color()
        print(result_3)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        var = [x.lower() for x in Vehicle.__COLOR_VARIANTS]
        if new_color.lower() in var:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Evgeniy', 'Ford mustang', 300, 'orange')

vehicle1.print_info()

vehicle1.set_color('Blue')
vehicle1.set_color('YELLOW')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()