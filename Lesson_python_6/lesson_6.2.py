

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        m = self._length * self._width * 25 * 5 / 1000
        print(m)


road = Road(5000, 20)
road.massa()