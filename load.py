import _pickle as pickle
import pygame, csv, os
from dot import *


def set_map(num):
    map = []
    # walls = [pygame.Rect(206, 222, 6, 294), pygame.Rect(211, 222, 139, 6), pygame.Rect(350, 222, 6, 246), pygame.Rect(355, 462, 43, 6), pygame.Rect(398, 270, 6, 198), pygame.Rect(403, 270, 427, 6), pygame.Rect(830, 222, 6, 54), pygame.Rect(835, 222, 235, 6), pygame.Rect(1070, 222, 6, 294), pygame.Rect(931, 510, 139, 6), pygame.Rect(926, 270, 6, 246), pygame.Rect(883, 270, 43, 6), pygame.Rect(878, 270, 6, 198), pygame.Rect(451, 462, 427, 6), pygame.Rect(446, 462, 6, 54), pygame.Rect(211, 510, 235, 6)]
    # walls = [pygame.Rect(206, 318, 6, 102), pygame.Rect(211, 318, 139, 6), pygame.Rect(350, 222, 6, 102), pygame.Rect(355, 222, 571, 6), pygame.Rect(926, 222, 6, 102), pygame.Rect(931, 318, 139, 6), pygame.Rect(1070, 318, 6, 102), pygame.Rect(931, 414, 139, 6), pygame.Rect(926, 414, 6, 102), pygame.Rect(355, 510, 571, 6), pygame.Rect(350, 414, 6, 102), pygame.Rect(211, 414, 139, 6)]
    walls = [pygame.Rect(542, 222, 6, 246), pygame.Rect(547, 222, 43, 6), pygame.Rect(590, 222, 6, 54), pygame.Rect(595, 270, 139, 6), pygame.Rect(734, 270, 6, 198), pygame.Rect(547, 462, 187, 6)]
    # home = (260, 260)
    # home = (250, 350)
    home = (624, 352)
    # dots = [LinearDot((424, 296), (856, 296), 6, True), LinearDot((856, 344), (424, 344), 6, True), LinearDot((424, 392), (856, 392), 6, True), LinearDot((856, 440), (424, 440), 6, True)]
    # dots = [LinearDot((376, 246), (376, 486), 4, False), LinearDot((424, 486), (424, 246), 4, False), LinearDot((472, 246), (472, 486), 4, False), LinearDot((520, 486), (520, 246), 4, False), LinearDot((568, 246), (568, 486), 4, False), LinearDot((616, 486), (616, 246), 4, False), LinearDot((664, 246), (664, 486), 4, False), LinearDot((712, 486), (712, 246), 4, False), LinearDot((760, 246), (760, 486), 4, False), LinearDot((808, 486), (808, 246), 4, False), LinearDot((856, 246), (856, 486), 4, False), LinearDot((904, 486), (904, 246), 4, False)]
    with open(os.path.join(f'level{num}.csv')) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    data = {'map': map, 'walls': walls, 'home': home}
    with open(f'level{num}.pkl', 'wb') as f:
        data = pickle.dump(data, f, -1)
    f.close()


def load_map(num):
    with open('level'+str(num)+'.pkl', 'rb') as f:
        data = pickle.load(f)
    f.close()
    return data

set_map(3)
