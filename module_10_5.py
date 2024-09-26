from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    for file in filenames:
        with open(file, 'r') as f:
            for line in f:
                f.readline()
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# read_info(filenames)
# end = datetime.now()
# print(f'{end - start} - линейный вызов')



if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} - многопроцессный вызов')

        
