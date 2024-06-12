def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2, 'shorts')
# # print_params(3, 'T-shirt', False, 7) - выдаёт ошибку так как кол-во заданных параметров не совпадает с переданными.
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'juice', True]
values_dict = {'a': 1, 'b': "juice",'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'mango']
print_params(*values_list_2,42)