def createABC3(key):
    abc = []
    for i in range(1040,1072):
        abc.append(chr(i))
    abc.remove("Ъ")
    abcWithKey = abc
    mid = []
    for i in range(len(key)):
        if key[i] not in mid:
            abcWithKey.pop(abcWithKey.index(key[i]))
            mid.append(key[i])
    for i in range(len(mid)):
        abcWithKey.insert(i, mid[i])
    abcMid = []
    for i in range(len(abcWithKey)):
        abcMid.append((abcWithKey[i % len(abcWithKey)]))
    return abcMid

def matrixNew(abc):
    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(abc[i * 5 + j])
    return matrix

def cipherPayfer(origin, matrix):    # Поиск на одинаковые символы
    # for i in matrix: print(i)
    for i in range(1, len(origin)):
        if origin[i] == origin[i - 1]:
            origin.insert(i, "Ё")
    # Если символов нечётное количество - прибавить 'X'
    if len(origin) % 2 != 0:
        origin.append("Ё")
    # Если в текста символ 'J' - заменить на 'I'
    for i in range(len(origin)):
        if origin[i] == "Ъ":
            origin[i] = "Ь"
    # Алгоритм Плейфера
    binary = []
    k = ""
    for i in origin:
        k += i
        if len(k) == 2:
            binary.append(k)
            k = ""
    # print(binary)
    # Шифрование
    encrypt = ""
    switch = 0
    # Перебор двойных символов
    for i in range(len(binary)):
        # k = 0 или k = 1 (Для разделения двойных символов)
        for k in range(2):
            # Перебор строк матрицы
            for x in range(len(matrix)):
                # Перебор символов в строке
                for y in range(len(matrix[x])):
                    # Если символ из матрицы равен символу из открытого сообщения
                    if matrix[x][y] == binary[i][k]:
                        # Если 0 и 1 символы открытого сообщения находятся на одной строке в матрице
                        if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                            # Если символ в матрице не равен началу матричной строки
                            if matrix[x][y] != matrix[x][-1]:
                                # То добавить к encrypt значение символа матрицы с отступом +1
                                encrypt += matrix[x][y + 1]
                            # Иначе если символы 0 и 1 находятся на разных строках матрицы
                            else:
                                # То добавить к encrypt значение символа матрицы с отступом -4
                                encrypt += matrix[x][y - 4]
                        # Иначе если символы 0 и 1 находятся на разных строках матрицы
                        else:
                            # Перебор строк матрицы
                            for a in range(len(matrix)):
                                # Перебор символов в строке
                                for b in range(len(matrix[a])):
                                    # Если символ из матрицы равен символу 0 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][0]:
                                        # Создать переменную x0, содержащую координату 0 символа
                                        x0 = a
                                    # Если символ из матрицы равен символу 1 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][1]:
                                        # Создать переменную x1, содержащую координату 1 символа
                                        x1 = a
                            # Если переменная 'switch' равна нулю
                            if switch == 0:
                                # Добавить к переменной decrypt координаты значения матрицы x1/y
                                encrypt += matrix[x1][y]
                                switch = 1
                            # Иначе
                            else:
                                # Добавить к переменной decrypt координаты значения матрицы x0/y
                                encrypt += matrix[x0][y]
                                switch = 0
    # Вывод зашифрованного сообщения на экран
    return encrypt

def decriptCipherPlayfer(shifrotext,matrix):
    # Деление зашифрованного текста по 2 символа
    binary = []
    k = ""
    for i in shifrotext:
        k += i
        if len(k) == 2:
            binary.append(k)
            k = ""
    # print(binary)

    # Расшифровка
    decrypt = []
    switch = 0
    # Перебор двойных символов
    for i in range(len(binary)):
        # k = 0 или k = 1 (Для разделения двойных символов)
        for k in range(2):
            # Перебор строк матрицы
            for x in range(len(matrix)):
                # Перебор символов в строке
                for y in range(len(matrix[x])):
                    # Если символ из матрицы равен символу из зашифрованного сообщения
                    if matrix[x][y] == binary[i][k]:
                        # Если 0 и 1 символы зашифрованного сообщения находятся на одной строке в матрице
                        if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                            # Если символ в матрице не равен началу матричной строки
                            if matrix[x][y] != matrix[x][0]:
                                # То добавить к decrypt значение символа матрицы с отступом -1
                                decrypt.append(matrix[x][y - 1])
                            # Иначе если символ в матрице равен началу матричной строки
                            else:
                                # То добавить к decrypt значение символа матрицы с отступом +4
                                decrypt.append(matrix[x][y + 4])
                        # Иначе если символы 0 и 1 находятся на разных строках матрицы
                        else:
                            # Перебор строк матрицы
                            for a in range(len(matrix)):
                                # Перебор символов в строке
                                for b in range(len(matrix[a])):
                                    # Если символ из матрицы равен символу 0 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][0]:
                                        # Создать переменную x0, содержащую координату 0 символа
                                        x0 = a
                                    # Если символ из матрицы равен символу 1 из зашифрованного сообщения
                                    if matrix[a][b] == binary[i][1]:
                                        # Создать переменную x1, содержащую координату 1 символа
                                        x1 = a
                            # Если переменная 'switch' равна нулю
                            if switch == 0:
                                # Добавить к переменной decrypt координаты значения матрицы x1/y
                                decrypt += matrix[x1][y]
                                switch = 1
                            else:
                                # Добавить к переменной decrypt координаты значения матрицы x0/y
                                decrypt += matrix[x0][y]
                                switch = 0
    # Удаление символов 'X'
    for i in range(len(decrypt) - 1):
        if decrypt[i] == "X":
            if decrypt[i] != decrypt[-1]:
                if decrypt[i - 1] == decrypt[i + 1]:
                    decrypt.remove(decrypt[i])
            else:
                decrypt.remove(decrypt[i])
    # Вывод расшифрованного сообщения на экран
    return "".join(decrypt)

our_text = list("тотктосмотритнаделособеихсторонобычноневидитниоднойизних".upper())
key = "жизнь".upper()
abc = createABC3(key)

# origin = [i for i in input().upper()]

print(cipherPayfer(our_text,matrixNew(abc)))
print(decriptCipherPlayfer(cipherPayfer(our_text,matrixNew(abc)),matrixNew(abc)))
