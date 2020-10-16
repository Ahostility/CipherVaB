def permutation_enc(message, key):
    extend_key = []
    message_list = list(message)
    enc_message = ''
    for i in range(len(message)):
        extend_key.append(key[i//(len(message)//len(key))])
    for i in range(len(message)//len(key)):
        for j in range(len(key)):
            table_index = extend_key.index(j+1)
            enc_message += message_list.pop(table_index)
            extend_key.pop(table_index)
    return enc_message
    
def permutation_dec(enc_message, key):
    extend_key = []
    enc_message_list = list(enc_message)
    message = ''
    for i in range(len(enc_message)):
        extend_key.append(1 + i//(len(enc_message)//len(key)))
    for i in range(len(enc_message)//len(key)):
        for j in key:
            table_index = extend_key.index(j)
            message += enc_message_list.pop(table_index)
            extend_key.pop(table_index)
    return message
    
 
print(permutation_dec('ЛДАЛК___НЫАЧЕЛГДПУЫНЕ_ГЛ__ДС_О_ОЧННЛСЮДАОТ,И_БДУ_ЕИ_ДВЗЩООСЬЫСЖ,УОИБГК_СИИ_ИАГВВИ__АБВОЬБТЖОЕИЕО', [2,4,1,7,3,8,6,5]))
 