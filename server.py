import socket
from _thread import *
import pickle
from player2 import Player
import random
import pygame

# Gets the Users IP (For temp use only)
hostname = socket.gethostname()
server = socket.gethostbyname(hostname)

# server = "66.71.20.137"
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
    players.append(Player(225, 225, 50, 50, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), cp))


def set_walls():
    wall1 = (pygame.Rect(0, 0, 50, 1000), (0, 0, 0))
    wall2 = (pygame.Rect(450, 0, 50, 1000), (0, 0, 0))
    wall3 = (pygame.Rect(0, 0, 1000, 50), (0, 0, 0))
    wall4 = (pygame.Rect(0, 450, 1000, 50), (0, 0, 0))
    wall5 = (pygame.Rect(100, 350, 1000, 50), (0, 0, 0))
    wall6 = (pygame.Rect(0, 100, 400, 50), (0, 0, 0))
    return [wall1, wall2, wall3, wall4, wall5, wall6]


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
                reply = [players, walls]

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    players.pop(get_player(id))
    conn.close()


players = []
walls = set_walls()
current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    make_new_player(current_player)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
