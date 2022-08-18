import random
def hangman ():
    wrong = 0
    stages = ['',
              '_________________                 ',
              '|                                 ',
              '|               |                 ',
              '|               0                 ',
              '|             / | \               ',
              '|              / \                ',
              '|                                 ',
              ]
    slova = ['кот', 'собака', 'попугай', 'мышь', 'слон', 'корова', 'коза']
    rand = random.randint(1,7)
    word = slova[rand]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = input('Введите букву: ')
        if msg in rletters:
            cind = rletters.index(msg)
            board[cind] = msg
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ' + ' '.join(board))
            win = True
            break
    if not win:
        print('Вы проиграли! Было загадано слово: {}.' .format(rletters))
hangman()
