import socket
import pickle

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)


class Network:
    def __init__(self):
        """Initializes Connection to Server"""
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "45.56.111.95"
        # self.server = server
        self.port = 55555
        self.addr = (self.server, self.port)
        self.p = None

    def getP(self, type):
        self.p = self.connect(type)
        return self.p

    def connect(self, type):
        """Connects to Server and Returns Server Message"""
        try:
            self.client.connect(self.addr)
            self.client.send(pickle.dumps(type))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

    def send(self, data):
        """Sends and Receives data from Server"""
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

    def disconnect(self):
        try:
            self.client.send(pickle.dumps('disconnect'))
        except socket.error as e:
            print(e)

