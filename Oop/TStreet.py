import math


class TStreet(object):

    name: str
    noise_map = list()
    pollution_map = list()
    type: int
    x1: int
    x2: int
    y1: int
    y2: int

    def __init__(self, _x1: int, _y1: int):

        self.x1 = _x1
        self.y1 = _y1

        if _x1 == 0:
            self.type = 2
            self.x2 = 500
            self.y2 = self.y1
            self.name = "Проспект №"+str(self.y1)
        else:
            self.type = 1
            self.x2 = self.x1
            self.y1 = 400
            self.name = "Улица №"+str(self.x1)

    def fill_noise_level_map(self, a_list):
        noise_level: float = 0
        l: int
        n: int

        if self.type == 2:
            l = self.x1
            n = self.x2
        else:
            l = self.y1
            n = self.y2

        while l < n:
            for vvv in range(len(a_list)):
                if self.is_transport_on_street(a_list[vvv]):
                    if self.type == 2:
                        noise_level = noise_level + a_list[vvv].get_noise_level() / max(1, abs(l - a_list[vvv].get_x()))
                    else:
                        noise_level = noise_level + a_list[vvv].get_noise_level() / max(1, abs(l - a_list[vvv].get_y()))
            if noise_level < 1:
                self.noise_map[l] = 0
            else:
                self.noise_map[l] = int(noise_level)
            noise_level = 0
            l += 1

    def get_noise_level_view(self):
        result: str = ""
        for i in range(len(self.noise_map)):
            if self.noise_map[i] == 0:
                result = result + "."
            else:
                result = result + "[" + str(self.noise_map[i]) + "]"
        return result

    def fill_pollution_level_map(self, a_list):
        pl: float = 0
        l: int = 0
        n: int = 0

        if self.type == 2:
            l = self.x1
            n = self.x2
        else:
            l = self.y1
            n = self.y2

        while l < n:
            for vvv in range(len(a_list)):
                if a_list[vvv].get_pollution_level() > 0 and self.is_transport_on_street(a_list[vvv]):
                    if self.type == 2:
                        pass

    def get_pollution_level_view(self):
        result: str = ""
        for i in range(len(self.pollution_map)):
            if self.pollution_map[i] == 0:
                result = result + "."
            else:
                result = result + "[" + str(self.pollution_map[i]) + "]"
        return result

    def get_pollution_level(self):
        result: str = ""
        for i in range(len(self.pollution_map)):
            if self.pollution_map[i] == 0:
                result = result + "."
            else:
                result = result + "[" + str(self.pollution_map[i]) + "]"
        return result

    def is_transport_on_street(self, a_transport):
        if a_transport.get_x() == self.x1 or a_transport.get_y == self.y1:
            return 1
        else:
            return 0

    def get_name(self):
        return self.name

    def noise_level(self, n_lvl):
        return 0

    def pollution_level(self, p_lvl):
        return 0

    def get_vehicle_count_on_street(self, vehicle_count):
        return 0
