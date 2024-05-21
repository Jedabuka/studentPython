def key():
    if number == 3:
        return '12'
    if number == 4:
        return '13'
    if number == 5:
        return '1423'
    if number == 6:
        return '121524'
    if number == 7:
        return '162534'
    if number == 8:
        return '13172635'
    if number == 9:
        return '1218273645'
    if number == 10:
        return '141923283746'
    if number == 11:
        return '11029384756'
    if number == 12:
        return '12131511124210394857'
    if number == 13:
        return '112211310495867'
    if number == 14:
        return '1611325212343114105968'
    if number == 15:
        return '1214114232133124115106978'
    if number == 16:
        return '1317115262143531341251161079'
    if number == 17:
        return '11621531441351261171089'
    if number == 18:
        return '12151811724272163631545414513612711810'
    if number == 19:
        return '118217316415514613712811910'
    if number == 20:
        return '13141911923282183731746416515614713812911'

import random

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(1, 6):
    number = random.choice(numbers)
    print((number), '-', key())








