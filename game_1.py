import random


def info():
    print('Гра: "Вгадай число!"')
    input('''--- Правила ---
Бот загадує число від 1 до 9, 
а ви повині його відгадати.
---------------
Натисніть Enter для продовження!''')
    print()


def player():
    while True:
        numbers = [f'{i}' for i in range(1, 10)]
        number = str(input('YOU :: '))
        if number not in numbers:
            print('! Потрібно вести число від 1 до 9 !\n')
        else:
            return int(number)


def bot():
    print('BOT :: Загадав число')
    return random.randrange(1, 10)


def nears(lst, arrow=None):
    if len(lst) == 1:
        mess = '[.]'
    else:
        mess = '['
        for i in range(len(lst)):
            if lst[i] == arrow:
                mess += '^  '
            else:
                mess += '.  '
        mess += '.]'
    return mess


def statistic(list_bot, list_player):
    # --- Вичисляєм найближче числодо до загаданого ботом ---
    if len(list_player) == 1:
        nearest = nears(list_player)
    else:
        lst = []
        for i in range(len(list_bot)-1):
            if list_bot[i] > list_player[i]:
                lst.append(list_bot[i] - list_player[i])
            elif list_player[i] > list_bot[i]:
                lst.append(list_player[i] - list_bot[i])
            elif list_player[i] == list_bot[i]:
                lst.append(0)
        near = lst[lst.index(min(lst))]
        nearest = nears(lst, near)
    # -------------------------------------------------------

    print(f'''\n|=== Statistic ===|
Спроб :: {len(list_player)}
{list_bot} :: Бот
{list_player} :: Ти
{nearest} :: Найблища
|=================|\n''')


def logic(list_bot, list_player):
    if list_player[-1] == list_bot[-1]:
        print('! Ти виграв !')
        statistic(list_bot, list_player)
        return False
    else:
        print('! Неправильне число !\n')
        return True


def main():
    ext = True
    list_bot = []
    list_player = []

    info()
    while ext:
        number_bot = bot()
        list_bot.append(number_bot)
        number_player = player()
        list_player.append(number_player)
        ext = logic([1], list_player)


if __name__ == '__main__':
    ex = True
    while ex:
        main()
        while True:
            print('Зіграти ще раз? Y/N')
            again = str(input('> ')).lower()
            if again == 'y' or again == 'yes':
                print()
                break
            elif again == 'n' or again == 'no':
                ex = False
                break
            else:
                print('Так чи ні! Y/N')
