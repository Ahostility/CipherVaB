file = open('out_put.txt', 'r')
start = file.readline().replace('\n', '')
trminal = file.readline().split(',')
notTerminal = file.readline().split(',')
rules = file.readline().split(',')
trminal[-1] = trminal[-1].replace('\n', '')
notTerminal[-1] = notTerminal[-1].replace('\n', '')
left = []
right = []
for i in rules: #делим правила на левые и правые части
    left.append(i.split('->')[0])
    right.append(i.split('->')[1])
N = []
for i in range(len(right)): # 1 шаг алгоритма
    no_term_string = True
    for j in right[i]:
        if j in notTerminal or right[i] in N:
            no_term_string = False
    if no_term_string: N.append(left[i])
new = []
while new != N: # оставшиеся шаги
    if new == []:
        new = N
    N = new
    for i in range(len(right)):
        for j in right[i]:
            if j in N:
                new.append(left[i])
                break
if (start not in N):
    print('Такой грамматики не существует')
else:
    print('Такая грамматика существует')
    
