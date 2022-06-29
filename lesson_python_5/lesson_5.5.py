with open ('my_file_3','r', encoding='utf-8') as f:
    c = f.readline()
    c = c.split()
    s = 0
    for n in c:
        s += int(n)
    print(s)