import _pickle as pickle
import pygame, csv, os


def set_map(num):
    map = []
    lines = [((144, 483), (144, 190)), ((147, 192), (285, 192)), ((288, 190), (288, 435)), ((291, 432), (333, 432)), ((336, 435), (336, 238)), ((339, 240), (765, 240)), ((768, 243), (768, 190)), ((771, 192), (1005, 192)), ((1008, 190), (1008, 483)), ((1005, 480), (867, 480)), ((864, 483), (864, 238)), ((861, 240), (819, 240)), ((816, 238), (816, 435)), ((813, 432), (387, 432)), ((384, 430), (384, 483)), ((381, 480), (147, 480))]
    walls = [pygame.Rect(206, 222, 6, 294), pygame.Rect(211, 222, 139, 6), pygame.Rect(350, 222, 6, 246), pygame.Rect(355, 462, 43, 6), pygame.Rect(398, 270, 6, 198), pygame.Rect(403, 270, 427, 6), pygame.Rect(830, 222, 6, 54), pygame.Rect(835, 222, 235, 6), pygame.Rect(1070, 222, 6, 294), pygame.Rect(931, 510, 139, 6), pygame.Rect(926, 270, 6, 246), pygame.Rect(883, 270, 43, 6), pygame.Rect(878, 270, 6, 198), pygame.Rect(451, 462, 427, 6), pygame.Rect(446, 462, 6, 54), pygame.Rect(211, 510, 235, 6)]
    with open(os.path.join('level1.csv')) as data:
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
