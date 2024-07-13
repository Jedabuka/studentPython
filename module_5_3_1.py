
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

sun = House('ЖК Солнченый', 4)
meadow = House('ЖК Зеленые луга', 5)
rainbow = House('ЖК Радуга', 7)
paradise = House('ЖК Фруктовый рай', 3)

print(House.houses_history)

del meadow
del rainbow

print(House.houses_history)
