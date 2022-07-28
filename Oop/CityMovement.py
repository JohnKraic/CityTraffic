import random
from Init import Init
from TVehicle import TVehicle
from TCivilTransport import TCivilTransport
from TLorryTransport import TLorryTransport


class CityMovement(Init):

    turn_count: int

    def get_vehicle_count(self, *abc):
        if abc == 1:
            self.gvc2(abc)

        else:
            self.gvc1()

    def gvc1(self):
        vehicle_count: int = 0
        vehicle_count = vehicle_count + len(Init.vehicle_list)
        return vehicle_count

    def gvc2(self, a_type):

        res = 0

        for v in range(len(list(Init.vehicle_list))):

            if Init.vehicle_list[v].type() == a_type:
                res = res + 1

        return res

    def get_ecology_vehicle_count(self):
        res: int = 0

        for v in range(len(list(Init.vehicle_list))):
            if Init.vehicle_list[v].energy_source != 0:
                res = Init.vehicle_list[v].get_energy_source()
                print("Экологический показатель: ", res)
        # return res

    def __init__(self):
        super().__init__()
        pass

    def get_turn_count(self):
        return self.turn_count

    def do_transport_move(self):

        for v in range(len(list(Init.vehicle_list))):

            for v_2 in range(len(list(Init.vehicle_list))):
                Init.vehicle_list[v].check_for_overtake(Init.vehicle_list[v_2])

            Init.vehicle_list[v].move()

            for s in range(len(list(Init.street_array))):
                if Init.street_array[s].is_transport_on_street:
                    Init.vehicle_list[v].set_street(Init.street_array[s])

        for s in range(len(list(Init.street_array))):
            Init.street_array[s].fill_noise_level_map(Init.vehicle_list)
            Init.street_array[s].fill_pollution_level_map(Init.vehicle_list)

        self.turn_count = self.turn_count + 1

    def check_transport_out(self):

        for i in range(len(Init.vehicle_list) - 1, 0, -1):
            if Init.vehicle_list[i].is_transport_out_city():
                Init.vehicle_list.pop(i)

    def do_transport_welcome(self):
        rnd = random.random()
        if rnd < 0.5:
            if random.randint(1, 3) == 1:
                Init.vehicle_list.append(TCivilTransport(random.randint(1, 40)))
                Init.vehicle_list.append(TLorryTransport(random.randint(1, 20)))

    def get_people_on_street(self, a_street):
        res = 0
        for i in range(len(Init.vehicle_list)):
            if a_street.is_transport_on_street(Init.vehicle_list[i]) and Init.vehicle_list[i].get_vehicle_type == 1:
                res = res + Init.vehicle_list[i].get_good_volume()

        return res

    def get_gruz_on_street(self, a_street):
        res = 0
        for vvv in range(len(Init.vehicle_list)):
            if a_street.is_transport_on_street(Init.vehicle_list[vvv]) and Init.vehicle_list[vvv].get_vehicle_type() == 2:
                res = res + Init.vehicle_list[vvv].get_good_volume()
        return res

    def get_street(self, a_index):
        return self.street_array[a_index]

    def get_noise_level_view(self, a_street):
        return a_street.get_noise_level_view()

    def get_pollution_level_view(self, a_street):
        return a_street.get_pollution_level_view()

    def draw_items(self):
        pass