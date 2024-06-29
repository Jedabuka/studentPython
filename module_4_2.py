def test_function():
    def inner_function():
        x = 'Я в области видимости функции test_function'
        print(x)  # - Не печатает. Мы не можем вызвать функцию inner_function не вызвав функцию test_function, так как
                  #   она находится в ней.

    inner_function()

inner_function()   # - Выдает ошибку, так как считывание идёт изнутри наружу.