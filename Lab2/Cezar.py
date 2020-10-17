def createABC2():
    ABC = []
    for i in range(1040,1072):
    # for i in range(65,92):
        ABC.append(chr(i))
    return ABC

def Cezar(our_text, abc, key):
    shifrotext = ""
    abc.insert(6,"Ё")
    for i in range(len(our_text)):
        shifrotext+=abc[(abc.index(our_text[i])+key)%len(abc)]
    return shifrotext

def decriptCezar(shifrotext,abc,keyInt):
    origin = ""
    abc.insert(6,"Ё")
    for i in range(len(shifrotext)):
        origin+=abc[(len(abc) + abc.index(shifrotext[i]) - keyInt)%len(abc)]
    return origin

def aphineCezar(our_text,abc,a,b):
    shifrotext = ""
    indexArr = []
    result = []
    abc.insert(6,"Ё")
    for i in range(len(our_text)):
        shifrotext+=abc[(a*abc.index(our_text[i])+b)%len(abc)]
        # print(shifrotext)
        indexArr.append(a*abc.index(our_text[i])+b)
    result.append(shifrotext)
    result.append(indexArr)
    return result

def decriptaphineCezar(shifrotext, indexAphine,abc,a,b):
    origin = ""
    abc.insert(6, "Ё")
    for i in range(len(shifrotext)):
        origin+=abc[((indexAphine[i] - b)//a) % len(abc)]
    return origin

def cezarWithKeyWord(origin,abc,key,indexK):
    shifrotext = ""
    abcWithKey = createABC2()
    abc = createABC2()
    abc.insert(6,"Ё")
    abcWithKey.insert(6,"Ё")
    mid = []
    for i in range(len(key)):
        if key[i] not in mid:
            abcWithKey.pop(abcWithKey.index(key[i]))
            mid.append(key[i])
    for i in range(len(mid)):
        abcWithKey.insert(i,mid[i])
    abcMid = []
    for i in range(len(abcWithKey)):
        abcMid.append(abcWithKey[(len(abcWithKey)-indexK+i)%len(abcWithKey)])
    print(abc)
    print(abcMid)
    for i in range(len(origin)):
        shifrotext+=abcMid[(abc.index(origin[i]))%len(abc)]
    return shifrotext

def decriptcezarWithKeyWord(shifrotext,abc,key,indexK):
    our_text = ""
    abcWithKey = createABC2()
    abc = createABC2()
    abc.insert(6, "Ё")
    abcWithKey.insert(6, "Ё")
    mid = []
    for i in range(len(key)):
        if key[i] not in mid:
            abcWithKey.pop(abcWithKey.index(key[i]))
            mid.append(key[i])
    for i in range(len(mid)):
        abcWithKey.insert(i, mid[i])
    abcMid = []
    for i in range(len(abcWithKey)):
        abcMid.append(abcWithKey[(len(abcWithKey) - indexK + i) % len(abcWithKey)])
    for i in range(len(shifrotext)):
        our_text += abc[(abcMid.index(shifrotext[i])) % len(abcMid)]
    return our_text

def trisemus(origin,abc,key):
    shifrotext = ""
    abcWithKey = createABC2()
    mid = []
    for i in range(len(key)):
        if key[i] not in mid:
            abcWithKey.pop(abcWithKey.index(key[i]))
            mid.append(key[i])
    for i in range(len(mid)):
        abcWithKey.insert(i, mid[i])
    abcMid = []

    for i in range(len(abcWithKey)):
        abcMid.append(abcWithKey[(i) % len(abcWithKey)])
    for i in range(len(origin)):
        shifrotext += abcMid[(8+abcMid.index(origin[i])) % len(abcMid)]
    return shifrotext

def decriptionTris(shifrotext,abc,key):
    our_text = ""
    abcWithKey = createABC2()
    mid = []
    for i in range(len(key)):
        if key[i] not in mid:
            abcWithKey.pop(abcWithKey.index(key[i]))
            mid.append(key[i])
    for i in range(len(mid)):
        abcWithKey.insert(i, mid[i])
    abcMid = []
    for i in range(len(abcWithKey)):
        abcMid.append(abcWithKey[(i) % len(abcWithKey)])
    print(abc)
    print(abcMid)
    for i in range(len(shifrotext)):
        our_text += abcMid[(len(abc) + abcMid.index(shifrotext[i])-8) % len(abcMid)]
    return our_text

#
abc = createABC2()
# origin = "мыдолжныпризнатьочевидноепонимаютлишьтектохочетпонять".upper()#originText
# origin = "УСПЕХ"#originText
# a = int(input())#aphine
# b = int(input())#aphine
# key = "музыка".upper()#input().upper()#keyWord
# keyInt = 17#int(input())#indexKeyShift
# #Cezar
# print(Cezar(origin,abc,keyInt))
# print(decriptCezar(Cezar(origin,abc,keyInt),abc,keyInt))
# #AphineCipher
# aphineCezarRes = aphineCezar(origin,abc,a,b)
# print(aphineCezarRes[0])
# print(decriptaphineCezar(aphineCezarRes[0],aphineCezarRes[1],abc,a,b))
# #cezarWithKeyWord
# print(cezarWithKeyWord(origin,abc,key,keyInt))
# print(decriptcezarWithKeyWord(cezarWithKeyWord(origin,abc,key,keyInt),abc,key,keyInt))
#trisemus
# print(trisemus(origin,abc,key))
# print(decriptionTris(trisemus(origin,abc,key),abc,key))
