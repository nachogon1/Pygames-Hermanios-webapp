import socket

from src.constants import SERVER_IP


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER_IP
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            print("socket", socket.gethostname())
            self.client.connect(self.addr)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(str(data)))
            return eval(self.client.recv(8000).decode())
        except socket.error as e:
            print(e)