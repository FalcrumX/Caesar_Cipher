print('Добро пожаловать в программу для шифровки/дешифровки текста!')
print('Код Цезаря')
print('Введите цифру 1, если вы хотите зашифровать текст на русском языке')
print('Введите цифру 2, если вы хотите зашифровать текст на английском языке')
print('Введите цифру 3, если вы хотите расшифровать текст на русском языке')
print('Введите цифру 4, если вы хотите расшифровать текст на английском языке')
print('Введите цифру 5, если вы хотите расшифровать текст на английском языке с неизвестным шагом шифровки : ')
question = int(input('Введите, цифру соответсвующего запроса: '))

num = 0


def get_russ_cipher(num, string):
     num = int(input('Введите шаг сдвига шифровки: '))
     for i in string:
        func = ord(i)+num #кодирование
        if func >= 1040 and func <= 1103:
            i = chr(func)
        elif ord(i) < 1040 or ord(i) > 1103:
            i = i
        elif func <= 1040:
            i = chr(func+32)
        elif func >= 1103:
            i = chr(func-32)
        print(i, end='')


def get_eng_cipher(num, string):
    num = int(input('Введите шаг сдвига шифровки: '))
    for i in string:
        func = ord(i)+num #кодирование
        if ord(i) >= 97 and ord(i) <= 122:
            if func >= 97 and func <= 122:
                i = chr(func)
            elif func >= 122:
                i = chr(func-26)
        elif ord(i) >= 65 and ord(i) <= 96:
            if func >= 65 and func <= 96:
                i = chr(func)
            elif func >= 96:
                i = chr(func-26)
        elif ord(i) < 65 or ord(i) > 122:
            i = i
        print(i, end='')


def get_rus_encoding(num, string):
    num = int(input('Введите шаг сдвига для дешифровки: '))
    for i in string:
        func = ord(i)-num #кодирование
        if i.isupper() == True:
            if func >= 1040 and func <= 1103:
                i = chr(func)
            elif ord(i) < 1040 or ord(i) > 1103:
                i = i
            elif func < 1040:
                i = chr(func+64)
        else:
            if func >= 1040 and func <= 1103:
                i = chr(func).lower()
            elif ord(i) < 1040 or ord(i) > 1103:
                i = i.lower()
            elif func <= 1040:
                i = chr(func+64).lower()
    
        print(i, end='')

def get_eng_encoding(num, string):
    num = int(input('Введите шаг сдвига для дешифровки: '))
    for i in string:
        func = ord(i)-num #кодирование
        if ord(i) >= 65 and ord(i) <= 96:
            if func >= 65 and func <= 96:
                i = chr(func)
            elif func < 65:
                i = chr(func+26)
        elif ord(i) >= 97 and ord(i) <= 122:
            if func >= 97 and func <= 122:
                i = chr(func)
            elif func < 97:
               i = chr(func+26)
        elif ord(i) < 65 or ord(i) > 122:
            i = i
        print(i, end='')

def get_encoding_non_step(string):
    for x in range(1, 26):
        code_string = ''
        for i in string:
            func = ord(i)-x #кодирование
            if ord(i) >= 65 and ord(i) <= 96:
                if func >= 65 and func <= 96:
                    i = chr(func)
                elif func < 65:
                    i = chr(func+26)
            elif ord(i) >= 97 and ord(i) <= 122:
                if func >= 97 and func <= 122:
                    i = chr(func)
                elif func < 97:
                    i = chr(func+26)
            elif ord(i) < 65 or ord(i) > 122:
                i = i
            code_string = code_string + i
        print(f'Вариант расшифровки №{x} - {code_string}')



if question == 1:
    string = input('Введите фразу для кодировки на русском языке: ')
    get_russ_cipher(num, string)
elif question == 2:
    string = input('Введите фразу для кодировки на английском языке: ')
    get_eng_cipher(num, string)
elif question == 3:
    string = input('Введите фразу для раскодировки на русском языке: ')
    get_rus_encoding(num, string)   
elif question == 4:
    string = input('Введите фразу для раскодировки на английском языке: ')
    get_eng_encoding(num, string)  
elif question == 5:
    string = input('Введите фразу для раскодировки на английском языке: ')
    get_encoding_non_step(string)
else:
    print('Ошибка!')

