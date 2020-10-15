def double_permutation_enc(key1,key2, message):
    if(len(key1)*len(key2) != len(message)):
        print('саси быдло')
        return
    else:
        permutation_table = []
        k = 0
        for i in range(len(key1)):
            for j in range(len(key2)):
                permutation_table.append([key1[i]*10 + key2[j], message[k]])
                k += 1 
        permutation_table.sort(key = lambda x: x[0])
        return ''.join([permutation_table[i][1] for i in range(len(message))])

def double_permutation_dec(key1, key2, enc_message):
    return ''.join(enc_message[4*(i-1)+(j-1)] for i in key1 for j in key2)

    

def magic_square_enc(key, message):
    if len(key) != len(message):
        print("Не то")
        return None
    return "".join([message[i-1] for i in key])

def magic_square_dec(key, enc_message):
    if len(key) != len(enc_message):
        print("Не то")
        return None
    return "".join([enc_message[key.index(i+1)] for i in range(16)])
    

#print(magic_square_enc([16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1], "ПРИЛЕТАЮВОСЬМОГО"))
#print(magic_square_dec([16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1], magic_square_enc([16,3,2,13,5,10,11,8,9,6,7,12,4,15,14,1], "ПРИЛЕТАЮВОСЬМОГО")))
print(double_permutation_dec([3,1,4,2], [4,1,3,2], 'ТЮАЕООГМРЛИПЕЬДС'))# 