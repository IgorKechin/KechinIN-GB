def base(name, s_name, year, city, email, tel):
    return f'{name} {s_name} родился в {year} году, проживает в городе {city}, {email}, {tel}'
print (base(name='Игорь', s_name='Кечин', year=1987, city='Москва', email='11111@inbox.ru', tel=8888888888))