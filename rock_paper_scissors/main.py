import random

def play():
    user = input('что ты выберешь? (к) для камня, (н) для ножниц, (б) для бумаги\n')
    user = user.lower()

    computer = random.choice(['к','н','б'])
    if user == computer:
        return 'Вы и компютер выбрали одно и тоже {}. Это ничья'.format(computer)
    
    # к > н, б > к, н > б
    if combat_win(user, computer):
        return 'Вы выбрали {} и компютер выбрал {}. Ты выиграл'.format(user, computer)

    return 'Вы выбрали {} и компютер выбрал {}. Ты проиграл'.format(user, computer)

def combat_win(player, oponent):
    if  (player == 'к' and oponent == 'н' ) or (player == 'б' and oponent == 'к' ) or (player == 'н' and oponent == 'б' ):
        return True
        
    return False

if __name__ == '__main__':
    print(play())
