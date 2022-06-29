with open ('my_file_0', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст, для выхода Enter: ')
        if not line:
            break
        print(line, file=f)

