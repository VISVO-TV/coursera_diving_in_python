"""Задание по программированию: Клиент для отправки метрик"""
import socket
import time


class Client:
    def __init__(self, ip_adress, port, timeout=None):
        self.ip_adress = ip_adress
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((ip_adress, port), timeout)
        except socket.error as error:
            raise error('Can\'t create connection', error)


    def _read(self):
        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error as error:
                raise error("Error reading data from socket", error)
        return data.decode('utf-8')


    def _send(self, data):
        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise error("Error sending data to server", err)


    def put(self, key, value, timestamp=int(time.time())):
        self._send(f"put {key} {value} {timestamp}\n".encode())
        raw_data = self._read()

        if raw_data == 'ok\n\n':
            return
        raise error('Server returns an error')


    def get(self, key):
        self._send(f"get {key}\n".encode())
        raw_data = self._read()
        data = {}
        status, payload = raw_data.split("\n", 1)
        payload = payload.strip()
        if status != 'ok':
            raise error('Server returns an error')
        if payload == '':
            return data

        try:

            for row in payload.splitlines():
                key, value, timestamp = row.split()
                if key not in data:
                    data[key] = []
                bisect.insort(data[key], ((int(timestamp), float(value))))

        except Exception as error:
            raise error('Server returns invalid data', error)

        return data

    def close(self):

        try:
            self.connection.close()
        except socket.error as error:
            raise error("Error. Do not close the connection", error)
