import os


print('Текущая директория:', os.getcwd())

for i in os.walk('.'):
    print(i)

print(os.path.join('products.txt', 'module_7_1.py', 'module_7_2.py', 'module_7_2.txt', 'module_7_5.py', 'calc.py'))

print(os.path.getatime('products.txt'))

print(os.path.getsize('products.txt'))

print(os.path.dirname(os.path.abspath('products.txt')))
