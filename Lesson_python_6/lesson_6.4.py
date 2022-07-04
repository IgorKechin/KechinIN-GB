class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула {self.direction}!')

    def show_speed(self):
        print('Скорост автомобиля: ', self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print ('Превышение скорости!')
        else:
            print('Скорост автомобиля: ', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print ('Превышение скорости!')
        else:
            print('Скорост автомобиля: ', self.speed)


class PoliceCar(Car):
    pass


tc = TownCar(50, 'зеленый', 'Аврора', False)
tc.show_speed()
tc2 = TownCar(80, 'зеленый', 'Аврора', False)
tc2.show_speed()
sc = SportCar(100, 'красный', 'Феррари', False)
sc.go()
wc = WorkCar(50, 'оранжевый', 'Трудяга', False)
wc.show_speed()
pc = PoliceCar(90, 'синий', 'Трудяга', True)
print(pc.is_police)