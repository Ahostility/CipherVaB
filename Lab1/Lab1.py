def double_permutation_enc(key1, key2, message):
    if (len(key1) * len(key2) != len(message)):
        return
    else:
        permutation_table = []
        k = 0
        for i in range(len(key1)):
            for j in range(len(key2)):
                permutation_table.append([key1[i] * 10 + key2[j], message[k]])
                k += 1
        permutation_table.sort(key=lambda x: x[0])
        return ''.join([permutation_table[i][1] for i in range(len(message))])

def double_permutation_dec(key1, key2, enc_message):
    return ''.join(enc_message[4 * (i - 1) + (j - 1)] for i in key1 for j in key2)

def magic_square_enc(key, message):
    if len(key) != len(message):
        print("Не то")
        return None
    return "".join([message[i - 1] for i in key])

def magic_square_dec(key, enc_message):
    if len(key) != len(enc_message):
        print("Не то")
        return None
    return "".join([enc_message[key.index(i + 1)] for i in range(len(key))])


def permutation_enc(message, key):
    extend_key = []
    message_list = list(message)
    enc_message = ''
    for i in range(len(message)):
        extend_key.append(key[i // (len(message) // len(key))])
    for i in range(len(message) // len(key)):
        for j in range(len(key)):
            table_index = extend_key.index(j + 1)
            enc_message += message_list.pop(table_index)
            extend_key.pop(table_index)
    return enc_message


def permutation_dec(enc_message, key):
    extend_key = []
    enc_message_list = list(enc_message)
    message = ''
    for i in range(len(enc_message)):
        extend_key.append(1 + i // (len(enc_message) // len(key)))
    for i in range(len(enc_message) // len(key)):
        for j in key:
            table_index = extend_key.index(j)
            message += enc_message_list.pop(table_index)
            extend_key.pop(table_index)
    return message


# origin = 'ЛДАЛК___НЫАЧЕЛГДПУЫНЕ_ГЛ__ДС_О_ОЧННЛСЮДАОТ,И_БДУ_ЕИ_ДВЗЩООСЬЫСЖ,УОИБГК_СИИ_ИАГВВИ__АБВОЬБТЖОЕИЕО'
# key = [2,4,1,7,3,8,6,5]
# print(len(origin),len(key))
# print(permutation_dec(origin, key))


# print(magic_square_enc([8,3,4,1,5,9,6,7,2], "ВЕДОМОСТЬ"))
# print(magic_square_dec([8,3,4,1,5,9,6,7,2],magic_square_enc([8,3,4,1,5,9,6,7,2], "ВЕДОМОСТЬ")))