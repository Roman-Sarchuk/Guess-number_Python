import game_2 as game
from time import sleep


class BOT:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.num = [n for n in range(min_num, max_num + 1)]
        self.ram = None
        self.answer = None
        self.index = None

    def _info(self, array):
        if array is True:
            print(f'{self.num} :: {self.index} = ', end='')
        else:
            print(f'{self.index} = ', end='')

    def _check_answer(self):
        if self.answer == 'LESS':
            self.num = self.num[0:self.index]
        elif self.answer == 'MORE':
            self.num = self.num[self.index:len(self.num)]
        elif self.answer == 'WIN':
            print('--- !WIN! ---')
            return False
        return True

    def _del_repeat(self):
        if self.ram in self.num:
            del self.num[self.index]

    def run(self, array=True):
        run = True
        print('--- Start ---')
        version = len(self.num)//2
        while run:
            self.index = 0 if version == 0 else version - 1
            self._info(array)
            self.ram = self.num[self.index]
            print(self.ram)
            self.answer = engine.logic(self.ram)
            print(self.ram, '->', self.answer)
            self._del_repeat()
            run = self._check_answer()
            version //= 2
            sleep(FPS)

    def info(self):
        print(f'''\n--- INFO ---
Число: {engine.get_num()}
Спроб: {engine.get_count()}
------------''')


if __name__ == '__main__':
    FPS = 0
    numbers = (1, 100000)
    engine = game.ENGINE(numbers[0], numbers[1])
    bot = BOT(numbers[0], numbers[1])
    print(f'NUM: {engine.get_num()}')
    bot.run(False)
    bot.info()
