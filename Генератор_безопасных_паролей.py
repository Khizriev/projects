import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
quantity = int(input('Количество паролей для генерации?'))
for i in range(quantity):
    def generate_password(lengthh, charss):
        return random.sample(charss, lengthh)
    length = int(input('Длина одного пароля?'))
    numbers = input('Включать ли цифры?')
    capital_letters = input('Включать ли прописные буквы?')
    lower_case = input('Включать ли строчные буквы?')
    symbols = input('Включать ли символы?')
    ambiguous_characters = input('Исключать ли неоднозначные символы? il1Lo0O')
    if numbers == 'д':
        chars += digits
    if capital_letters == 'д':
        chars += uppercase_letters
    if lower_case == 'д':
        chars += lowercase_letters
    if symbols == 'д':
        chars += punctuation
    if ambiguous_characters == 'д':
        chars = [char for char in chars if char not in 'il1Lo0O']
    print(*generate_password(length, chars), sep = '')            
            
            