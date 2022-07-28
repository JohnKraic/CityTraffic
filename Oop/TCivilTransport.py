from TVehicle import *
import random as rnd


class TCivilTransport(TVehicle):

    max_people_count: int
    people_count: int
    energy_source: int

    def __init__(self, max_people_count: int):
        super(TVehicle).__init__()
        self.max_people_count: int = int(max_people_count)
        self.energy_source = int(rnd.randint(10, 100))
        self.people_count: int = int(rnd.randint(1, self.max_people_count))

    def get_info(self):
        res = super(TCivilTransport).get_info()
        res = res + " пассажирский"
        return res

    def get_x(self) -> int:
        return int(self.x)

    def get_y(self) -> int:
        return int(self.y)

    def get_energy_source_type(self) -> int:
        return int(self.energy_source)

    def get_noise_level(self) -> int:
        return int(self.noise_level)

    def get_pollution_level(self) -> int:
        return int(self.pollution_level)

    def get_vehicle_type(self) -> int:
        return 1

    def get_vehicle_type_str(self) -> str:
        return "пассажирский"

    def get_good_volume(self) -> int:
        return self.people_count

    def get_speed(self) -> int:
        return self.speed

    def get_direction(self):
        return self.direction