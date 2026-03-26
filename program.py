en_low = 'abcdefghijklmnopqrstuvwxyz'
en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def crypt():
    text = input('Введите ваш текст: ')
    key = int(input('Шаг сдвига: '))
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

def encrypt():
    text = input('Введите ваш текст: ')
    key = int(input('Шаг сдвига: '))
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

q = input('Зашифровать или расшифровать тект? (з/р)')
if q == 'Зашифровать':
    crypt()
else:
    encrypt()