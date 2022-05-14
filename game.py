import random


class ENGINE:
    def __init__(self, min_num, max_num):
        self._bot_num = random.randint(min_num, max_num)
        self._count = 0

    def logic(self, version):
        self._count += 1
        if version > self._bot_num:
            return 'LESS'
        if version < self._bot_num:
            return 'MORE'
        return 'WIN'

    def get_count(self):
        return self._count

    def get_num(self):
        return self._bot_num


def info():
    print(f'''\n--- INFO ---
Число: {engine.get_num()}
Спроб: {engine.get_count()}
------------''')


def check(value):
    if value == 'LESS' or value == 'MORE':
        print(value)
    elif value == 'WIN':
        print('! You win !')
        return True
    return False


def input_num():
    value = None
    while 1:
        try:
            value = int(input('> '))
        except ValueError:
            print('Incorrect input!')
            continue
        break
    return value


if __name__ == '__main__':
    numbers = (1, 1000000)
    engine = ENGINE(numbers[0], numbers[1])
    print(f'! The bot_num guessed the number {numbers[0]}-{numbers[1]} !')
    while not check(engine.logic(input_num())):
        pass
    info()
