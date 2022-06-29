with open ('zp', 'r', encoding='utf-8') as f:
    c = f.read().splitlines()
    s=0
    for i in c:
        i = i.split()
        if int(i[1]) < 20000:
            print(i[0])
        s+=int(i[1])
    print('Итого зп по всем сотрудникам', s)
