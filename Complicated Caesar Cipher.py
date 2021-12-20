# Шифрует/ дешифрует текст на русском и английском языках. Каждое слово (де)шифруется с ключом, равным длинне этого слова.

print('Добро пожаловать в программу шифрования текста по-Цезарьски!')
de_cipher = input('Если Вам необходимо ЗАшифровать текст, нажмите "+". Для ДЕшифровки нажмите "-": ')
language = input('На каком языке текст? Если на русском, введите "ru", если на английском - "en": ').lower()
text = input('Введите исходный текст: ').split()

russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
result = []

if language == 'en':
    for i in text:
        word = ''
        key = sum(c.isalpha() for c in i) % 26
        
        for c in i:        
            if c.isalpha(): 
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
            word += c
        result.append(word)
        
if language == 'ru':
    for i in text:
        word = ''
        key = sum(c.isalpha() for c in i) % 32
        for c in i:
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
            word += c   
        result.append(word)

result = ' '.join(result)
print('Результат', 'де' * (de_cipher == '-') + 'шифрования:', result)