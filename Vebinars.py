# def printMax(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
#
# printMax(3, 4) # прямая передача значений
#
# x = 5
# y = 7
# -------------------------------------------------------------------------------

# def weight_change(weight, product_price, cash_paid):
#     """
#     Рассчитывает сдачу за покупку товара на развес.
#
#     :param total_cost: общая стоимость товара
#     :param product_price: цена за килограмм
#     :param weight: вес товара в килограммах
#     :param cash_paid: сумма денег, заплаченная покупателем
#     :return: сумма сдачи
#     """
#     total_cost = product_price * weight
#     change = cash_paid - total_cost
#     return change
#
# # Пример использования для другого товара
# weight = 2.3
# product_pr
# # Пример использования для другого товара
# weight = 2.3
# product_price = 50
# cash_paid = 300
#
# print(f"Сдача за товар весом {weight} кг по цене {product_price} руб/кг: {weight_change(weight, product_price, cash_paid)} рублей")

# ---------------------------------------------------------------------------------------------

# def single_root_words(root_word, *other_words):
#     same_words = []  # Список для хранения слов, удовлетворяющих условию
#     root_word = root_word.lower()  # Приведение корневого слова к нижнему регистру
#
#     for word in other_words:
#         word = word.lower()  # Приведение текущего слова к нижнему регистру
#         if root_word in word or word in root_word:  # Проверка условия
#             same_words.append(word)  # Добавление слова в список
#
#     return same_words

# # Примеры использования функции
# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
#
# print(result1)  # Вывод: ['richiest', 'orichalcum', 'richies']
# print(result2)  # Вывод: ['Able', 'Disable']

# ---------------------------------------------------------------------------------------------

# def my_function(name, last_name, occupation, age):
#     print(f'Сотрудник #1 - {name} {last_name} {occupation} {age}')
#
# info1, info2, info3, info4 = 'Алиса', 'Селезнева', 'скрам-мастер', 30
# my_function(info1, info2, info3, info4)
# my_function(info2, info3, info1, info4)
# my_function(info4, info1, info2, info3)
#
# my_function('Svytoslav', 'Ivanovich', 'IT-tech', '28')

# -------------------------------------------------------------------------------------------------------
#
# def calculate_structure_sum(data_structure):
#     total_sum = 0
#
#     if isinstance(data_structure, (int, float)):
#         return data_structure
#     elif isinstance(data_structure, str):
#         return len(data_structure)
#     elif isinstance(data_structure, (list, tuple, set)):
#         for item in data_structure:
#             total_sum += calculate_structure_sum(item)
#     elif isinstance(data_structure, dict):
#         for value in data_structure.values():
#             total_sum += calculate_structure_sum(value)
#
#     return total_sum
#
# # Пример использования функции
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# result = calculate_structure_sum(data_structure)
# print(result)  # Выведет 99
#
# -----------------------------------------------------------------------
#
# def calculate_structure_sum(data_structure):
#     total_sum = 0
#     if isinstance(data_structure, (int, float)):
#         return data_structure
#     elif isinstance(data_structure, str):
#         return len(data_structure)
#     elif isinstance(data_structure, (list, tuple, set)):
#         for item in data_structure:
#             total_sum += calculate_structure_sum(item)
#     elif isinstance(data_structure, dict):
#         for key, value in data_structure.items():
#             total_sum += calculate_structure_sum(key)
#             total_sum += calculate_structure_sum(value)
#     elif isinstance(data_structure, tuple):
#         for item in data_structure:
#             total_sum += calculate_structure_sum(item)
#     return total_sum
#
#
# # Пример использования функции
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# result = calculate_structure_sum(data_structure)
# print(result)  # Выведет 99

# ---------------------------------------------------------------