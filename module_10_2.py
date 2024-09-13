from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.warriors = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warriors > 0:
            self.warriors -= self.power
            sleep(1)
            if self.warriors <= 0:
                self.days += 1
                self.warriors = 0
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.warriors} воинов.')
            elif self.warriors > 0:
                self.days += 1
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.warriors} воинов.')

        return print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight("Sir Lancelot", 13)
second_knight = Knight("Sir Galahad", 26)

threads = [first_knight, second_knight]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


