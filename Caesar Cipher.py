print('Добро пожаловать в программу шифрования текста по-Цезарьски!')
de_cipher = input('Если Вам необходимо ЗАшифровать текст, нажмите "+". Для ДЕшифровки нажмите "-": ')
language = input('На каком языке текст? Если на русском, введите "ru", если на английском - "en": ').lower()
key = input('Введите ключ шифра (шаг сдвига вправо): ')
text = input('Введите исходный текст: ')

russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
result = ''

if language == 'en':
    key = int(key) % 26
    for c in text:
        if 96 < ord(c.lower()) < 123:
            if de_cipher == '+':            
                order = ord(c.lower()) + key
                if order > 122:
                    order -= 26
            elif de_cipher == '-':
                order = ord(c.lower()) - key
                if order < 97:
                    order += 26                
            if c.isupper():
                c = chr(order).upper()
            else:
                c = chr(order)
        result += c
        
if language == 'ru':
    key = int(key) % 32
    for c in text:
        if c.lower() in russian_alphabet:
            if de_cipher == '+':
                order = russian_alphabet.find(c.lower()) + key
                if order > 31:
                    order -= 32
            elif de_cipher == '-':
                order = russian_alphabet.find(c.lower()) - key
                if order < 0:
                    order += 32                
            if c.isupper():
                c = russian_alphabet[order].upper()
            else:
                c = russian_alphabet[order]
        result += c        
        
print(result)