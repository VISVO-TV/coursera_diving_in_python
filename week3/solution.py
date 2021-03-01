"""Задание по программированию: Реализация простого класса для чтения из файла"""
import os

class FileReader:
    def __init__(self, road_file):
        self.road_file = road_file


    def read(self):
        try:
            with open(self.road_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print('')

    # в задании не требуют данного метода
    def get_path(self):
        print(os.path.abspath(self.road_file))
