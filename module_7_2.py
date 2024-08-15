def custom_write(file_name, strings):
    strings_positions = {}
    lines = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        current_tell = file.tell()
        lines += 1
        strings_positions.update({(lines, current_tell): string})
        file.write(f'{string}\n')

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('module_7_2.txt', info)
for elem in result.items():
    print(elem)




