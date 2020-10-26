file = open('out_put.txt', 'r')
start_symbol = file.readline().replace('\n','')
term = file.readline().split(',')
non_term = file.readline().split(',')
rules = file.readline().split(',')
term[-1] = term[-1].replace('\n','')
non_term[-1] = non_term[-1].replace('\n','')
if '\n' in rules[-1]:
    rules[-1] = rules[-1].replace('\n', '')
left = []
right = []
context_rules_count = 0
reg_left = 0
reg_right = 0
start_rules = 0
for i in rules: #делим правила на левые и правые части
    left.append(i.split('->')[0])
    right.append(i.split('->')[1])
for i in left: #проверяем контекстную зависимость
    non_term_coun = 0
    for j in i: #считаем количество терминалов в каждой левой части правила, для того, чтобы убедиться в том, что это не грамматика 0
        if j in non_term:
            non_term_coun+=1
    if non_term_coun == 0:
        print('Неограниченая грамматика')
        exit(0)
    if (len(i)!= 1):
        context_rules_count+=1
#print(len(right))     
if context_rules_count!=0:
    print('Контекстно-зависимая грамматика')
else: #проверяем реуглярность грамматики
    for i in right:
        non_term_coun = 0
        non_term_visited = False
        left_term_count = 0
        right_term_count = 0
        for j in i: # считаем число терминалов слева и справа от нетреминала
            if(j in term and not non_term_visited):
                left_term_count+=1
            elif (j in term  and non_term_visited):
                right_term_count+=1
            else:
                non_term_visited=True
                non_term_coun+=1
        #print(left_term_count, ' ', right_term_count)
            
        if left_term_count == 0 and len(i)!=1 and non_term_coun == 1:
            reg_right+=1
        elif right_term_count == 0 and len(i)!=1 and non_term_coun == 1:
            reg_left+=1
        elif (left_term_count!=0 and right_term_count != 0) or non_term_coun > 1:
            print('Контекстно-независимая грамматика')
            exit(0)
    #print(reg_left, ' ', reg_right)
    if reg_right == 0 and reg_left != 0:
        print('Левосторонняя регулярная грамматика')
    else:#reg_left == 0 and reg_right !=0
        print('Правосторонняя регулярная грамматика')