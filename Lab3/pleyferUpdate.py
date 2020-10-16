ALPHABET = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
def playfair_encode(key, message):
    table = []
    keyword = list(key.upper())
    message_list = list(message.upper())
    excess_keys = []
    q0 = 0
    q1 = 0
    r0 = 0
    r1 = 0
    enc_message = []
    for i in range(len(keyword)):
        if(keyword[i] == 'Ё'):
            keyword[i] = 'Е'
        if(keyword[i] in keyword[i+1::]):
            excess_keys.append(keyword.index(keyword[i],i+1))
    for i in range(len(excess_keys)):
        keyword.pop(excess_keys[i] -  i)
    table.extend(keyword)
    for i in ALPHABET:
        if(i not in table):
            table.append(i)
    excess_keys = []
    for i in range(len(message_list),2):
        if message_list[i] == message_list[i+1]:
            excess_keys.append(i)
    for i in excess_keys:
        message_list.insert(i,'Ъ')
    if len(message_list)%2 == 1:
        message_list.append("Ъ")
    for i in range(0,len(message_list),2):
        q0 = table.index(message_list[i])//8
        r0 = table.index(message_list[i])%8
        q1 = table.index(message_list[i+1])//8
        r1 = table.index(message_list[i+1])%8
        if (q0 == q1):
            enc_message.append(table[8*q0 + (r0 + 1)%8])
            enc_message.append(table[8*q1 + (r1 + 1)%8])
        elif (r0 == r1):
            enc_message.append(table[8*((q0+1)%4) + r0])
            enc_message.append(table[8*((q1+1)%4) + r1])
        else:
            enc_message.append(table[8*q0 + r1])
            enc_message.append(table[8*q1 + r0])
    return ''.join(enc_message)

print(playfair_encode('РАБОТА', 'ПРИЛЕТАЮЗАВТРА'))