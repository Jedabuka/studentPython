def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            isinstance(number, (int, float))
            result += number
        except TypeError:
            incorrect_data = incorrect_data + 1

    return result, incorrect_data


def calculate_average(numbers):
    number_of_numbers = 0
    sum_num = 0
    try:
        for i in numbers:
            try:
                sum_num += i
                number_of_numbers += 1

            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')

        try:
            arithmetic_mean = sum_num / number_of_numbers
            return arithmetic_mean

        except ZeroDivisionError:
            return 0

    except TypeError:
        print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')