import random
number = random.randint(1, 100)
attempts = 0
border = int(input('Укажите правую границу:'))
m = 'д'
print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    if num in range(1, border + 1):
        return True
    else:
        return False
while m == 'д':        
    n = int(input('Введите число'))
    while is_valid(n) != True:
        print('А может быть все-таки введем целое число от 1 до 100?')
        n = int(input())
    while n != number:
        if n < number:
            attempts += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            n = int(input())
        elif n > number:
            attempts += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            n = int(input())
    print('Вы угадали, поздравляем!')
    print('Количесвто попыток:', attempts)
    print('Ссыграть заново?')
    m = input('Да = д, Нет = н')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        