import random
import random as rnd
from TStreet import TStreet as Street
import math


class TVehicle(object):
    x: int
    y: int
    street: Street
    direction: float
    normal_speed: int
    rrr: float

    def __init__(self):
        self.max_speed: int = rnd.randint(1, 60)
        self.noise_level: int = rnd.randint(1, 20)
        self.x = 0
        self.y = random.randint(1, 4) * 100
        self.speed = rnd.randint(1, self.max_speed)
        self.normal_speed = self.speed
        self.rrr = random.random()

        if self.rrr < 0.5:
            self.energy_source = 0
            self.pollution_level = 0
        else:
            self.energy_source = 1
            self.pollution_level = random.randint(1, 10)

    def type(self):
        return 0

    def can_obgon(self):
        return 1

    def get_energy_source(self):
        return self.energy_source

    def check_for_overtake(self, a_transport2):
        if self.street == a_transport2.street and self.energy_source == 0:
            x1: int = self.x + int(self.speed * math.cos(self.direction))
            y1: int = self.y + int(self.speed * math.sin(self.direction))
            x2: int = a_transport2.x + int(a_transport2.speed*math.cos(a_transport2.direction))
            y2: int = a_transport2.x + int(a_transport2.speed*math.sin(a_transport2.direction))

            if (self.x < a_transport2.x and x1 >= x2) or \
                    (self.x > a_transport2.x and x1 <= x2) or \
                (self.y < a_transport2.y and y1 >= y2) or \
                    (self.y > a_transport2.y and y1 <= y2):
                self.speed = a_transport2.speed
            else:
                self.speed = self.normal_speed
        else:
            self.speed = self.normal_speed

    def move(self):
        d_x: int = int(self.speed * math.cos(self.direction))
        d_y: int = int(self.speed * math.sin(self.direction))
        r: int

        if d_x < 0:
            r = ((1000 - self.x) - d_x) % 100
        else:
            r = (self.x + d_x) % 100

        if r != 0 and r < self.speed:
            self.change_direction(r)
        else:
            if d_y < 0:
                r = ((1000 - self.y) - d_y) % 100
            else:
                r = (self.y + d_y) % 100

            if r != 0 and r < self.speed:
                self.change_direction(r)
            else:
                self.x = self.x + d_x
                self.y = self.y + d_y

    def change_direction(self, a_delta):
        tmp: int
        self.x = int(self.x + int(self.speed - a_delta) * math.cos(self.direction))
        self.y = int(self.y + int(self.speed - a_delta) * math.sin(self.direction))
        tmp = random.randint(-1, 2)

        if tmp > 0:
            self.direction = self.direction + math.pi / 2 * 1
        else:
            self.direction = self.direction + math.pi / 2 * (-1)

        self.x = self.x + int(a_delta * math.cos(self.direction))
        self.y = self.y + int(a_delta * math.sin(self.direction))

    def is_transport_out_city(self):
        if self.x >= 500 or self.x <= 0:
            return 1
        else:
            if self.y >= 400 or self.y <= 0:
                return 1
            else:
                return 0

    def get_info(self):
        res: str = "X=" + str(self.x) + " Y=" + str(self.y)
        res = res + " Скорость=" + str(self.speed)
        if self.energy_source == 1:
            res = res + " Источник внутренний"
        else:
            res = res + " Источник внешний"

        res = res + " Шум= " + str(self.noise_level)
        res = res + " Загрязнение=" + str(self.pollution_level)

        return res

    def set_street(self, a_street: Street):
        self.street: Street = a_street

