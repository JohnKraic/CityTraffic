import time

from CityMovement import CityMovement
from Init import Init
from TCivilTransport import TCivilTransport
from TLorryTransport import TLorryTransport
from TStreet import TStreet
from TVehicle import TVehicle


movement = CityMovement()

init = Init()

init.fill_transport_array()

# for i in range(len(movement.street_array)):
#     print(movement.street_array[i].name)  # Вывод названия улицы
#     print(movement.street_array[i].x1)

movement.do_transport_welcome()
# movement.check_transport_out()
# movement.fill_transport_array()
# movement.get_ecology_vehicle_count()
for i in range(7):
    time.sleep(1)
    print("Название улицы: ", movement.street_array[i].name)
    # print("Легковой транспорт на улице: ", movement.vehicle_list[i])
    # for j in range(len(movement.vehicle_list)):
    #     if j % 2 == 0:
    #         print("Легковой транспорт: ", movement.vehicle_list[j])
    #     if j % 2 != 0:
    #         print("Грузовой транспорт: ", movement.vehicle_list[j])
    # print(movement.get_ecology_vehicle_count())
    print(movement.get_pollution_level_view(a_street=movement.street_array[i]))
    print(movement.street_array[i].pollution_map)




# На каждом шаге по времени  пользователь может вывести следующую информацию:
# 	Состояние любого транспортного средства;
# 	уровень шума в каждой точке проезжей части;
# 	уровень загрязнения в каждой точке проезжей части;
# 	количество пассажиров на любой улице;
# 	вес перевозимого груза на любой улице;
# 	количество пассажирских транспортных средств;
# 	количество грузовых транспортных средств;
# 	количество  транспортных средств, не загрязняющих окружающую среду.
