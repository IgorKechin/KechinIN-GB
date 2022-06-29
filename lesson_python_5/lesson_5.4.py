with open ('my_file_1', 'r', encoding='utf-8') as f:
    c = f.readlines()
    print(c)
    with open ('my_file_2', 'w', encoding='utf-8') as m:
        for w in c:
            w = w.split()
            if w[0] == 'One':
                w[0] = 'Один'
            elif w[0] == 'Two':
                w[0] = 'Два'
            elif w[0] == 'Three':
                w[0] = 'Три'
            elif w[0] == 'Four':
                w[0] = 'Четыре'
            w = ' '.join(s for s in w) + '\n'
            m.write(w)
