import socket
import pickle

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)


class Network:
    def __init__(self):
        """Initializes Connection to Server"""
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "71.162.242.106"
        self.server = server
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        """Connects to Server and Returns Server Message"""
        try:
            self.client.connect(self.addr)
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
