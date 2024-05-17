car_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]

for i in car_list:
    print('Я езжу на автомобиле марки', i)
    
    cars_count = 0

    for i in range(len(car_list[1:])):
        cars_count += 10

print(cars_count)


