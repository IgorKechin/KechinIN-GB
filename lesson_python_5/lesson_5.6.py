d={}
with open ('my_file_4', 'r', encoding='utf-8') as f:
    for line in f:
        name, lab = line.split(':')
        lab = lab.split()
        num = 0
        for l in lab:
            if '-' in l:
                continue
            n, v = l.split('(')
            num += int(n)
        d[name] = num
    print(d)
