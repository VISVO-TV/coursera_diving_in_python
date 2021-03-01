"""Задание по программированию: Файл с магическими методами"""

import os
import csv
import tempfile

class ReadAnyFile:
    # в задании данной функции не предполагается, и можно ограничиться методом
    # read() в классе File
    # но тренировка 'фабричного' паттерна - мое решение. Мне с ним жить.
    def read(self):
        raise NameError

class ReadCSV(ReadAnyFile):
    def read(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            a = []
            for row in reader:
                a.append(row)
            return a


class ReadTXT(ReadAnyFile):
    def read(self, path):
        with open(path, 'r') as f:
            return f.read()


class File:
    def __init__(self, path):
        self.path = path
        self.counter = 0
        self._reader = ReadAnyFile()
        a = path[0 : path.rfind('/')]
        if not os.path.exists(a) and path.rfind('/') != -1:
            # функционал по созданию древа директорий не предполагался в задании
            os.makedirs(a)
        open(self.path, 'a').close()


    def read(self):
        if os.path.splitext(self.path)[1] in ('.txt', '', None):
            self._reader = ReadTXT()
            return self._reader.read(self.path)
        elif os.path.splitext(self.path)[1] in ('.csv'):
            self._reader = ReadCSV()
            return self._reader.read(self.path)
        else:
            print("Sorry, this format file not supported")

    def write(self, str):
        with open(self.path, 'w') as f:
            return f.write(str)


    def __str__(self):
        return os.path.join(os.getcwd(), self.path)


    def __add__(self, obj):
        try:
            data = self.read() + '\n' + obj.read()
        except TypeError:
            print('Files format are different')
            data = ''
        fd, path = tempfile.mkstemp(suffix=os.path.splitext(self.path)[1], dir=tempfile.gettempdir())
        a = File(path)
        a.write(data)
        return a


    def __iter__(self):
        return self

    def __next__(self):
        list = self.read().split('\n')
        if len(list) <= self.counter:
            raise StopIteration
        result = list[self.counter]
        self.counter += 1
        return result
