from cars import *


car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying,
car.passenger_seats_count, sep='\n')

truck = Truck('Nissan', 'nissan.jpeg', '1.5', body_whl='1.3 x 2.23 x 3.11')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.carrying,
truck.body_length, truck.body_width, truck.body_height, sep='\n')

spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,
spec_machine.photo_file_name, spec_machine.extra, sep='\n')

spec_machine.get_photo_file_ext()
cars = get_car_list('coursera.csv')
print(cars)
