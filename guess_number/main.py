import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Найди число от 1 до {x}: '))
        if guess < random_number:
            print('Не верный ответ. Бери выше!')
        elif guess > random_number:
            print('Не верный ответ. Бери меньше!')

    print(f'Вау, ты угадал число {random_number} правильно. Молодец!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Число {guess} больше (б), меньше (м), или правильно (п)?? ').lower()
        if feedback == 'б':
            high = guess - 1
        elif feedback == 'м':
            low = guess + 1

    print(f'Есть! Компютер угадал загаданный тобой {guess} правильно!')


guess(10)