# def get_multiplied_digits(number):
#     str_number = str(number)
#
#     if len(str_number) == 1:
#         return str_number
#     else:
#         first = int(str_number[0])
#         rest_of_digits = int(str_number[1:])
#         print(rest_of_digits)
#         return first * get_multiplied_digits(rest_of_digits)
#
# result = get_multiplied_digits(50609)
# print(result)

def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        first = int(str(number)[0])
        rest_of_digits = number % 10 ** (len(str(number)) - 1)
        print(rest_of_digits)
        return first * get_multiplied_digits(rest_of_digits)

result = get_multiplied_digits(50609)
print(result)

# rest_of_digits = number % 10 ** (len(str_number) - 1)
# rest_of_digits = int(str_number[1:])