with open ('my_file','r',encoding='utf-8') as f:
    c = f.read().splitlines()
    print('Количество строк в файле: ', len(c))
    for i, w in enumerate(c):
        print('Номер строки и количество слов: ', i, len(w.split()))