en_low = 'abcdefghijklmnopqrstuvwxyz'
en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

text = input('Введите ваш текст: ')
shift = int(input('Шаг сдвига: '))
crypt = ''
for char in text:
    crypt += chr((ord(char) + shift - 97) % 26 + 97)
print(crypt)