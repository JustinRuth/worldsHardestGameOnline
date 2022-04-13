import socket
from _thread import *
import pickle
from player2 import Player
import random
import pygame

# Gets the Users IP (For temp use only)
hostname = socket.gethostname()
server = socket.gethostbyname(hostname)

# server = "45.56.111.95"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the server to a port
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started on ", server)


def make_new_player(cp):
    """Makes a new player object at random position with a random color"""
    players.append(Player(260, 260, 32, 32, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), cp))


def get_player(id):
    """Gets the index of a player with a certain id from players"""
    try:
        for index, item in enumerate(players):
            if item.current_player == id:
                return index
    except error as e:
        print(e)


def threaded_client(conn, id):
    """Main loop that sends and receives data for the players"""
    player = get_player(id)
    conn.send(pickle.dumps([players[player], 1]))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            player = get_player(id)
            players[player] = data

            if not data:
                print("Disconnected")
                break
            elif data == 'disconnect':
                print("Disconnected")
                break
            else:
                reply = players

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    players.pop(get_player(id))
    conn.close()


players = []
current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    make_new_player(current_player)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
