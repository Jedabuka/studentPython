
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return sun.number_of_floors == meadow.number_of_floors

    def __lt__(self, other):
        return sun.number_of_floors < meadow.number_of_floors

    def __le__(self, other):
        return sun.number_of_floors <= meadow.number_of_floors

    def __gt__(self, other):
        return sun.number_of_floors > meadow.number_of_floors

    def __ge__(self, other):
        return sun.number_of_floors >= meadow.number_of_floors

    def __ne__(self, other):
        return sun.number_of_floors != meadow.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __iadd__(self, value):
        self.number_of_floors += value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __radd__(self, value):
        self.number_of_floors += value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

sun = House('ЖК Солнченый', 4)
meadow = House('ЖК Зеленые луга', 5)

print(sun.name, sun.number_of_floors)
print(meadow.name, meadow.number_of_floors)

sun.go_to(7)
meadow.go_to(3)

print(sun)
print(meadow)

print(len(sun))
print(len(meadow))

print(sun == meadow)
print(sun < meadow)
print(sun <= meadow)
print(sun > meadow)
print(sun >= meadow)
print(sun != meadow)
print(sun + 5)
sun += 6
print(sun)
meadow = 10 + meadow
print(meadow)
