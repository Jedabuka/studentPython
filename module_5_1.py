class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

        def go_to(new_floor):
            for i in range(1, new_floor + 1):
                print(i)
                if new_floor > number_of_floors:
                    print(f'Такого этажа не существует')


sun = House('ЖК Солнченый', 4)
meadow = House('ЖК Зеленые луга', 5)

print(sun.name, sun.number_of_floors)
print(meadow.name, meadow.number_of_floors)

sun.go_to(4)
meadow.go_to(6)