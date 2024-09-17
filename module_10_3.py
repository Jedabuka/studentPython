from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(1, 101):
            number = randint(50, 500)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                self.balance += number
                print(f'Пополнение: {number}. Баланс: {self.balance}')

            elif self.lock.locked() and self.balance < 500:
                self.lock.release()
                self.balance += number
                print(f'Пополнение: {number}. Баланс: {self.balance}')

            sleep(0.001)

    def take(self):
        for i in range(1, 101):
            number = randint(50, 500)
            print(f'Запрос на {number}')

            if self.balance >= number:
                self.balance -= number
                print(f'Снятие: {number}. Баланс: {self.balance}')

            elif self.balance < number:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

        sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
