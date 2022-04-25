import socket
from _thread import *
import pickle
from player2 import Player
import random
import pygame
import sys

# Gets the Users IP (For temp use only)
# hostname = socket.gethostname()
# server = socket.gethostbyname(hostname)

server = "45.56.111.95"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the server to a port
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, Server Started on ", server)

game_id = 0
games = []


def make_new_player(cp):
    """Makes a new player object at random position with a random color"""
    return [260, 260, 1, cp, 0]
    # return Player(260, 260, 32, 32, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), cp)


def make_new_game(code=-1):
    global game_id
    if code == -1:
        code = random.randint(0,999999)
        # code = 123456
    players = []
    game = {'game_id': game_id, 'code': code, 'players': players}
    games.append(game)
    lmao = [game_id, code]
    game_id += 1
    return lmao


def get_game(code):
    global games
    for game in games:
        if game['code'] == code:
            return game['game_id']
    return make_new_game(code)[0]


def get_players(gid):
    global games
    try:
        for game in games:
            if game['game_id'] == gid:
                return game['players']
    except error as e:
        print(e)


def set_players(gid, players):
    global games
    try:
        for game in games:
            if game['game_id'] == gid:
                game['players'] = players
    except error as e:
        print(e)


def get_player(gid, id):
    """Gets the index of a player with a certain id from players"""
    try:
        players = get_players(gid)
        for index, item in enumerate(players):
            if item[3] == id:
                return index
    except error as e:
        print(e)


def set_player(gid, id, player):
    try:
        players = get_players(gid)
        players[get_player(gid, id)] = player
        set_players(gid, players)
    except error as e:
        print(e)


def add_new_player(gid, id):
    try:
        players = get_players(gid)
        players.append(make_new_player(id))
        set_players(gid, players)
    except error as e:
        print(e)


def remove_player(gid, id):
    try:
        players = get_players(gid)
        for index, item in enumerate(players):
            if item[3] == id:
                players.pop(index)
                if len(players) == 0:
                    remove_game(gid)
                else:
                    set_players(gid, players)
        print(games)
    except error as e:
        print(e)


def remove_game(gid):
    global games
    for index, game in enumerate(games):
        if game['game_id'] == gid:
            games.pop(index)


def threaded_client(conn, id):
    """Main loop that sends and receives data for the players"""
    data = pickle.loads(conn.recv(4092))
    if data == 'host':
        # print('host')
        game_data = make_new_game()
        gid = game_data[0]
        code = game_data[1]
    else:
        # print('join')
        code = data[1]
        gid = get_game(code)

    add_new_player(gid, id)
    player = get_players(gid)[get_player(gid, id)]
    conn.send(pickle.dumps([player, 1, code]))

    reply = ""
    while True:
        try:
            try:
                data = pickle.loads(conn.recv(4092))
            except:
                continue
            player = data

            if not data:
                print("Disconnected")
                break
            elif data == 'disconnect':
                break
            else:
                set_player(gid, id, player)
                reply = get_players(gid)

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    remove_player(gid, id)
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
