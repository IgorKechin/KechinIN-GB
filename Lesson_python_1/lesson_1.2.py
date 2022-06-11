sec = int(input('Введите время в секундах: '))
hours = sec//3600
minutes = (sec - hours*3600)//60
seconds = sec - hours*3600 - minutes*60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')