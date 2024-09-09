def is_prime(func):
    def wrapper(*args):
        prime = func(*args)
        if prime > 1 and (prime % 2 != 0 or prime == 2) and (prime % 3 != 0 or prime == 3):
            print('Простое')
        else:
            print('Составное')
        return prime
    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)