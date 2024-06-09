def generate_key(num):
    key = ''
    for i in range(1, num):
        for j in range(i + 1, num + 1):
            if num % (i + j) == 0:
                key += str(i) + str(j)
    return key

for num in range(3, 21):
    key = generate_key(num)
    print(f"{num} - {key}")