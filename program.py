def is_digital(number): # функция проверки на ввод числа
    num = number.strip()
    while True:
        if not num.isdigit() or int(num) == 0:
            print('Некорректные данные, введите число!')
            num = input('Введите число: ').strip()
        else:
            return int(num)

def is_answer(ans):
    answer = ans.strip().lower()
    while True:
        if answer in ['зашифровать', 'з', 'да', 'yes', 'y', 'crypt']:
            return crypt()
        elif answer in ['расшифровать', 'р', 'decrypt', 'd']:
            return decrypt()
        else:
            answer = input('Зашифровать или расшифровать тект? (з/р) ')

def is_again(ans): # функция проверки ответа
    if ans.strip().lower() in ['да', 'д', 'yes', 'y']:
        return True
    else:
        return False

def crypt():
    text = input('Введите ваш текст: ').strip()
    key = is_digital(input('Шаг сдвига: '))
    crypt = ''
    for char in text:
        if 97 <= ord(char) <= 122:
            crypt += chr((ord(char) + key - 97) % 26 + 97)
        elif 65 <= ord(char) <= 90:
            crypt += chr((ord(char) + key - 65) % 26 + 65)
        elif 1072 <= ord(char) <= 1103:
            crypt += chr((ord(char) + key - 1072) % 32 + 1072)
        elif 1040 <= ord(char) <= 1071:
            crypt += chr((ord(char) + key - 1040) % 32 + 1040)
        else:
            crypt += char
    print(crypt)

def decrypt():
    text = input('Введите ваш текст: ').strip()
    key = is_digital(input('Шаг сдвига: '))
    decrypt = ''
    for char in text:
        if 97 <= ord(char) <= 122:
            decrypt += chr((ord(char) - key - 97) % 26 + 97)
        elif 65 <= ord(char) <= 90:
            decrypt += chr((ord(char) - key - 65) % 26 + 65)
        elif 1072 <= ord(char) <= 1103:
            decrypt += chr((ord(char) - key - 1072) % 32 + 1072)
        elif 1040 <= ord(char) <= 1071:
            decrypt += chr((ord(char) - key - 1040) % 32 + 1040)
        else:
            decrypt += char
    print(decrypt)

again = True
while again:
    is_answer(input('Зашифровать или расшифровать тект?(з/р) '))
    again = is_again(input('Хотите повторно запустить программу?(д/н) '))
else:
    print('Спасибо, что воспользовались программой!')