immutable_var = 1, 'hello', 2.0, True
print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var) Мы не можем изменить сам кортеж, так как он отностится к
# неизменяемым типам данных, но мы можем изменить типы данных внутри кортежа, если они
# относятся к изменяемым типам данных.
mutable_list = (1, 2, [3, 4, 5])
mutable_list[2][0] = 9
print(mutable_list)
