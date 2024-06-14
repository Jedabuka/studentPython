def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        first = int(str(number)[0])
        rest_of_digits = number % 10 ** (len(str(number)) - 1)
        return first * get_multiplied_digits(rest_of_digits)

result = get_multiplied_digits(50609)
print(result)