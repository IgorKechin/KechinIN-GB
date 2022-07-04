from time import sleep


class TrafficLight:

    def running(self):
        while True:
            self.__color = 'Красный'
            print(f'{self.__color} светофор!')
            sleep(7)
            self.__color = 'Желтый'
            print(f'{self.__color} светофор!')
            sleep(2)
            self.__color = 'Зеленый'
            print(f'{self.__color} светофор!')
            sleep(7)


traffic_light = TrafficLight()
traffic_light.running()