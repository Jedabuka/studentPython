from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            file.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.now()
print(f'{end - start} - линейный вызов')


# if __name__ == '__main__':
#     start = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     end = datetime.now()
#     print(f'{end - start} - многопроцессный вызов')

        
