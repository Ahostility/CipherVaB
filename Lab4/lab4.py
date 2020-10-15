def cipherViginer(our_text, abc, key):
    shifrotext = ""
    a = []
    k = 0
    n = 0
    index_str = 0
    index_pil = 0
    newkey = ""
    for i in range(len(our_text)):
        newkey += key[i % len(key)]
    for i in range(len(abc)):
        a.append([])
        for j in range(len(abc)):
            a[i].append(abc[(j + i) % len(abc)])
    while n != len(our_text):
        for ind in range(len(abc)):
            if a[ind][0] == our_text[k % len(newkey)]:
                index_str = ind
                for str in range(len(abc)):
                    if a[0][str] == newkey[k % len(newkey)]:
                        index_pil = str
                        shifrotext += a[index_str][index_pil]
        k += 1
        n += 1
    return shifrotext

def decriptionViginer(shifr,abc,key):
    old_text = ""
    a = []
    k = 0
    n = 0
    index_str = 0
    newkey = ""
    for i in range(len(shifr)):
        newkey += key[i % len(key)]
    for i in range(len(abc)):
        a.append([])
        for j in range(len(abc)):
            a[i].append(abc[(j + i) % len(abc)])
    while n != len(shifr):
        for ind in range(len(abc)):
            if a[0][ind] == newkey[k % len(newkey)]:
                for str in range(len(abc)):
                    if a[str][ind] == shifr[k % len(shifr)]:
                        index_str = str
                        old_text += a[index_str][0]
        k += 1
        n += 1
    return old_text


def winston_enc(origin):
    message = origin.upper()
    q0 = 0
    q1 = 0
    r0 = 0
    r1 = 0
    message_list = list(message.upper())
    excess_keys = []
    enc_message = []
    key1 = ['Ж', 'Щ', 'Н', 'Ю', 'Р', 'И', 'Т', 'Ь', 'Ц', 'Б', 'Я', 'М', 'Е', '.', 'С', 'В', 'Ы', 'П', 'Ч', ' ', ':',
            'Д', 'У', 'О', 'К', 'З', 'Э', 'Ф', 'Г', 'Ш', 'Х', 'А', ',', 'Л', 'Ъ']
    key2 = ['И', 'Ч', 'Г', 'Я', 'Т', ',', 'Ж', 'Ь', 'М', 'О', 'З', 'Ю', 'Р', 'В', 'Щ', 'Ц', ':', 'П', 'Е', 'Л', 'Ъ',
            'А', 'Н', '.', 'Х', 'Э', 'К', 'С', 'Ш', 'Д', 'Б', 'Ф', 'У', 'Ы', ' ']
    for i in range(len(message_list), 2):
        if message_list[i] == message_list[i + 1]:
            excess_keys.append(i)
    for i in excess_keys:
        message_list.insert(i, 'Ъ')
    if len(message_list) % 2 == 1:
        message_list.append("Ъ")
    for i in range(0, len(message_list), 2):
        q0 = key1.index(message_list[i]) // 5
        r0 = key1.index(message_list[i]) % 5
        q1 = key2.index(message_list[i + 1]) // 5
        r1 = key2.index(message_list[i + 1]) % 5
        if (q0 == q1):
            enc_message.append(key2[5 * q0 + r0])
            enc_message.append(key1[5 * q1 + r1])
        elif (r0 == r1):
            enc_message.append(key2[5 * q0 + r0])
            enc_message.append(key1[5 * q1 + r1])
        else:
            enc_message.append(key2[5 * q0 + r1])
            enc_message.append(key1[5 * q1 + r0])
    return ''.join(enc_message)
#
# print(Lab4.winston_enc(input()))