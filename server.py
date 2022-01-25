import socket
from _thread import *
import pickle
from player import Player
import random

server = "192.168.1.10"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")

players = []


def make_new_player(cp):
    players.append(Player(random.randint(0, 100)*4, random.randint(0, 100)*4, 50, 50, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), cp))


def get_player(id):
    try:
        for index, item in enumerate(players):
            if item.current_player == id:
                return index
    except error as e:
        print(e)


def threaded_client(conn, id):
    player = get_player(id)
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            player = get_player(id)
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players

                #print("Received: ", data)
                #print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    players.pop(get_player(id))
    conn.close()

current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    make_new_player(current_player)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1