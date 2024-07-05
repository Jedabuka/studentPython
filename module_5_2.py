
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

sun = House('ЖК Солнченый', 4)
meadow = House('ЖК Зеленые луга', 5)

print(sun.name, sun.number_of_floors)
print(meadow.name, meadow.number_of_floors)

sun.go_to(7)
meadow.go_to(5)

print(sun)
print(meadow)

print(len(sun))
print(len(meadow))


