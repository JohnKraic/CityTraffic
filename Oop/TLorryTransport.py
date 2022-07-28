from TVehicle import *
import random


class TLorryTransport(TVehicle):

    max_load_weight: int
    load_weight: int
    energy_source: int

    def __init__(self, max_load_weight: int):
        super(TVehicle).__init__()
        self.max_load_weight: int = int(max_load_weight)
        self.energy_source = int(rnd.randint(10, 100))
        self.load_weight: int = int(random.randint(1, self.max_load_weight))

    def get_info(self):
        res = super(TLorryTransport).get_info()
        res = res + " грузовой"
        return res

    def get_x(self) -> int:
        return int(self.x)

    def get_y(self) -> int:
        return int(self.y)

    def get_energy_source_type(self) -> int:
        return int(self.energy_source)

    def get_noise_level(self) -> int:
        return int(self.noise_level)

    def get_vehicle_type(self) -> int:
        return 2

    def get_vehicle_type_str(self) -> str:
        return "грузовой"

    def get_good_volume(self) -> int:
        return int(self.load_weight)

    def get_direction(self):
        return self.direction

    def get_speed(self) -> int:
        return int(self.speed)

    def get_pollution_level(self) -> int:
        return int(self.pollution_level)

