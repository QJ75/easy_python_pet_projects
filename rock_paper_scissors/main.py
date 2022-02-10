import random
import math

def play():
    user = input('что ты выберешь? (к) для камня, (н) для ножниц, (б) для бумаги\n')
    user = user.lower()

    computer = random.choice(['к','н','б'])

    if user == computer:
        return (0, user, computer)
    
    # к > н, б > к, н > б
    if combat_win(user, computer):
        return (1, user, computer)
        
    return (-1, user, computer)

def combat_win(player, oponent):
    if  (player == 'к' and oponent == 'н' ) or (player == 'б' and oponent == 'к' ) or (player == 'н' and oponent == 'б' ):
        return True
        
    return False

def best_player(n):
    #игра против компютера пока не достигнута победа в n раз
    player_wins = 0
    computer_wins = 0
    wins_necesery = math.ceil(n/2)
    print(wins_necesery)
    while player_wins < wins_necesery and computer_wins < wins_necesery:
        
        result, user, computer = play()
        
        if result == 0:
            print('Вы и компютер выбрали одно и тоже {}. Это ничья\n'.format(user))
        elif result == 1:
            player_wins +=1
            print('Вы выбрали {} и компютер выбрал {}. Ты выиграл\n'.format(user, computer))
        else:
            computer_wins += 1
            print('Вы выбрали {} и компютер выбрал {}. Ты проиграл\n'.format(user, computer))
        print('\n')
    if player_wins > computer_wins:
        print('Ты одержал победу за {} раз. Молодец!!!\n'.format(n))
    else:
        print('Ты проиграл компьютеру за {} раз. Попробуй еще раз!\n'.format(n))

if __name__ == '__main__':
    best_player(3) #2
