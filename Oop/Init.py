from TLorryTransport import TLorryTransport
from TCivilTransport import TCivilTransport
from TStreet import TStreet
import numpy as np
import random


class Init(object):

    vehicle_list = list()
    street_array = np.empty(7, dtype=TStreet)

    def fill_transport_array(self):
        self.vehicle_list.append(TCivilTransport(random.randint(1, 40)))
        self.vehicle_list.append(TLorryTransport(random.randint(1, 20)))

    def fill_street_array(self):
        for i in range(3):
            self.street_array[i] = TStreet(_x1=(i+1) * 100, _y1=0)

        for i in range(3, 7):
            self.street_array[i] = TStreet(_x1=0, _y1=(i - 3) * 100)

    def __init__(self):
        self.fill_transport_array()
        self.fill_street_array()
