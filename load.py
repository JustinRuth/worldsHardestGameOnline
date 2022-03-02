import _pickle as pickle
import pygame, csv, os


def set_map(num):
    map = []
    lines = []
    walls = []
    with open(os.path.join('level2.csv')) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    data = {'map': map, 'lines': lines, 'walls': walls}
    with open('level'+str(num)+'.pkl', 'wb') as f:
        data = pickle.dump(data, f, -1)
    f.close()


def load_map(num):
    with open('level'+str(num)+'.pkl', 'rb') as f:
        data = pickle.load(f)
    f.close()
    return data
