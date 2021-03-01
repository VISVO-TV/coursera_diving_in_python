"""Задание по программированию: Классы и наследование"""
import os
import csv
import re


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying


    def get_photo_file_ext(self):
        return print(os.path.splitext(self.photo_file_name)[1])


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = 'truck'
        if re.fullmatch('[\d]+\.[\d]*(| )x(| )[\d]+\.[\d]*(| )x(| )[\d]+\.[\d]*', body_whl):
            list = body_whl.split('x')
            self.body_whl = body_whl
            self.body_length = float(list[0])
            self.body_width = float(list[1])
            self.body_height = float(list[2])
        else:
            self.body_whl = None
            self.body_length = self.body_width = self.body_height = 0


    def get_body_volume(self):
        if self.body_whl:
            return self.body_length * self.body_height * self.body_width
        return '0'


class Car(CarBase):
    def __init__(self, brand,  photo_file_name, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class SpecMachine(CarBase):
    def __init__(self, brand,  photo_file_name, carrying, extra):
        super().__init__(photo_file_name, brand, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(filename):
    def handler(args):
        for n in args:
            if n == '':
                return False
            return True


    def handler_photo(photo):
        if os.path.splitext(photo)[1] in ('.jpeg', '.jpg', '.gif', '.png'):
            return True
        return False

    car_list = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0].lower() == 'car':
                    if handler([row[1], row[2], row[3], row[5]]) and handler_photo(row[3]):
                            name = Car(brand = row[1], passenger_seats_count = row[2], photo_file_name = row[3], carrying = row[5])
                            car_list.append(name)
                elif row[0].lower() == 'truck':
                    if handler([row[1], row[3], row[5]]) and handler_photo(row[3]):
                        name = Truck(brand = row[1], photo_file_name = row[3], body_whl = row[4], carrying = row[5])
                        car_list.append(name)
                elif row[0].lower() == 'spec_machine':
                    if handler([row[1], row[3], row[5], row[6]]) and handler_photo(row[3]):
                            name = SpecMachine(brand = row[1], photo_file_name = row[3], carrying = row[5], extra = row[6])
                            car_list.append(name)
                else:
                    continue
            except IndexError:
                continue
    return car_list
