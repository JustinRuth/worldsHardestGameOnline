import _pickle as pickle
import pygame, csv, os
from dot import *
from coin import *

def set_map(num):
    map = []
    # walls = [pygame.Rect(206, 222, 6, 294), pygame.Rect(211, 222, 139, 6), pygame.Rect(350, 222, 6, 246), pygame.Rect(355, 462, 43, 6), pygame.Rect(398, 270, 6, 198), pygame.Rect(403, 270, 427, 6), pygame.Rect(830, 222, 6, 54), pygame.Rect(835, 222, 235, 6), pygame.Rect(1070, 222, 6, 294), pygame.Rect(931, 510, 139, 6), pygame.Rect(926, 270, 6, 246), pygame.Rect(883, 270, 43, 6), pygame.Rect(878, 270, 6, 198), pygame.Rect(451, 462, 427, 6), pygame.Rect(446, 462, 6, 54), pygame.Rect(211, 510, 235, 6)]
    # walls = [pygame.Rect(206, 318, 6, 102), pygame.Rect(211, 318, 139, 6), pygame.Rect(350, 222, 6, 102), pygame.Rect(355, 222, 571, 6), pygame.Rect(926, 222, 6, 102), pygame.Rect(931, 318, 139, 6), pygame.Rect(1070, 318, 6, 102), pygame.Rect(931, 414, 139, 6), pygame.Rect(926, 414, 6, 102), pygame.Rect(355, 510, 571, 6), pygame.Rect(350, 414, 6, 102), pygame.Rect(211, 414, 139, 6)]
    # walls = [pygame.Rect(542, 222, 6, 246), pygame.Rect(547, 222, 43, 6), pygame.Rect(590, 222, 6, 54), pygame.Rect(595, 270, 139, 6), pygame.Rect(734, 270, 6, 198), pygame.Rect(547, 462, 187, 6)]
    # walls = [pygame.Rect(302, 414, 6, 102), pygame.Rect(307, 414, 139, 6), pygame.Rect(446, 366, 6, 54), pygame.Rect(451, 366, 43, 6), pygame.Rect(494, 318, 6, 54), pygame.Rect(499, 318, 43, 6), pygame.Rect(542, 270, 6, 54), pygame.Rect(547, 270, 43, 6), pygame.Rect(590, 126, 6, 150), pygame.Rect(595, 126, 91, 6), pygame.Rect(686, 126, 6, 150), pygame.Rect(691, 270, 43, 6), pygame.Rect(734, 270, 6, 54), pygame.Rect(739, 318, 43, 6), pygame.Rect(782, 318, 6, 54), pygame.Rect(787, 366, 43, 6), pygame.Rect(830, 366, 6, 198), pygame.Rect(787, 558, 43, 6), pygame.Rect(782, 558, 6, 54), pygame.Rect(739, 606, 43, 6), pygame.Rect(734, 606, 6, 54), pygame.Rect(547, 654, 187, 6), pygame.Rect(542, 606, 6, 54), pygame.Rect(499, 606, 43, 6), pygame.Rect(494, 558, 6, 54), pygame.Rect(451, 558, 43, 6), pygame.Rect(446, 510, 6, 54), pygame.Rect(307, 510, 139, 6)]
    # walls = [pygame.Rect(206, 126, 6, 54), pygame.Rect(211, 126, 811, 6), pygame.Rect(1022, 126, 6, 54), pygame.Rect(979, 174, 43, 6), pygame.Rect(974, 174, 6, 438), pygame.Rect(307, 606, 667, 6), pygame.Rect(302, 270, 6, 342), pygame.Rect(211, 270, 91, 6), pygame.Rect(206, 222, 6, 54), pygame.Rect(211, 222, 667, 6), pygame.Rect(878, 222, 6, 294), pygame.Rect(403, 510, 475, 6), pygame.Rect(398, 318, 6, 198), pygame.Rect(403, 318, 379, 6), pygame.Rect(782, 318, 6, 102), pygame.Rect(499, 414, 283, 6), pygame.Rect(494, 366, 6, 54), pygame.Rect(451, 366, 43, 6), pygame.Rect(446, 366, 6, 102), pygame.Rect(451, 462, 379, 6), pygame.Rect(830, 270, 6, 198), pygame.Rect(355, 270, 475, 6), pygame.Rect(350, 270, 6, 294), pygame.Rect(355, 558, 571, 6), pygame.Rect(926, 174, 6, 390), pygame.Rect(211, 174, 715, 6)]
    # walls = [pygame.Rect(206, 126, 6, 102), pygame.Rect(211, 126, 859, 6), pygame.Rect(1070, 126, 6, 486), pygame.Rect(211, 606, 859, 6), pygame.Rect(206, 510, 6, 102), pygame.Rect(211, 510, 91, 6), pygame.Rect(302, 414, 6, 102), pygame.Rect(307, 414, 571, 6), pygame.Rect(878, 318, 6, 102), pygame.Rect(307, 318, 571, 6), pygame.Rect(302, 222, 6, 102), pygame.Rect(211, 222, 91, 6)]
    # walls = [pygame.Rect(206, 318, 6, 102), pygame.Rect(211, 318, 139, 6), pygame.Rect(350, 174, 6, 150), pygame.Rect(355, 174, 571, 6), pygame.Rect(926, 174, 6, 150), pygame.Rect(931, 318, 139, 6), pygame.Rect(1070, 318, 6, 102), pygame.Rect(931, 414, 139, 6), pygame.Rect(926, 414, 6, 150), pygame.Rect(355, 558, 571, 6), pygame.Rect(350, 414, 6, 150), pygame.Rect(211, 414, 139, 6)]
    walls = [pygame.Rect(398, 126, 6, 486), pygame.Rect(403, 126, 187, 6), pygame.Rect(590, 126, 6, 54), pygame.Rect(595, 174, 91, 6), pygame.Rect(686, 126, 6, 54), pygame.Rect(691, 126, 187, 6), pygame.Rect(878, 126, 6, 198), pygame.Rect(883, 318, 91, 6), pygame.Rect(974, 318, 6, 102), pygame.Rect(883, 414, 91, 6), pygame.Rect(878, 414, 6, 198), pygame.Rect(691, 606, 187, 6), pygame.Rect(686, 558, 6, 54), pygame.Rect(595, 558, 91, 6), pygame.Rect(590, 558, 6, 54), pygame.Rect(403, 606, 187, 6), pygame.Rect(494, 174, 6, 54), pygame.Rect(499, 174, 43, 6), pygame.Rect(542, 174, 6, 102), pygame.Rect(451, 270, 91, 6), pygame.Rect(446, 222, 6, 54), pygame.Rect(451, 222, 43, 6), pygame.Rect(446, 318, 6, 102), pygame.Rect(451, 318, 91, 6), pygame.Rect(542, 318, 6, 102), pygame.Rect(451, 414, 91, 6), pygame.Rect(446, 462, 6, 102), pygame.Rect(451, 462, 91, 6), pygame.Rect(542, 462, 6, 102), pygame.Rect(451, 558, 91, 6), pygame.Rect(734, 174, 6, 102), pygame.Rect(739, 174, 91, 6), pygame.Rect(830, 174, 6, 102), pygame.Rect(739, 270, 91, 6), pygame.Rect(734, 318, 6, 102), pygame.Rect(739, 318, 91, 6), pygame.Rect(830, 318, 6, 102), pygame.Rect(739, 414, 91, 6), pygame.Rect(734, 462, 6, 102), pygame.Rect(739, 462, 91, 6), pygame.Rect(830, 462, 6, 102), pygame.Rect(739, 558, 91, 6), pygame.Rect(590, 222, 6, 294), pygame.Rect(595, 222, 91, 6), pygame.Rect(686, 222, 6, 294), pygame.Rect(595, 510, 91, 6)]

    # home = (260, 260)
    # home = (250, 350)
    # home = (624, 352)
    # home = (624, 184)
    # home = (216, 136)
    # home = (240, 160)
    # home = (250, 350)
    home = (456, 184)

    # dots = [LinearDot((424, 296), (856, 296), 6, True), LinearDot((856, 344), (424, 344), 6, True), LinearDot((424, 392), (856, 392), 6, True), LinearDot((856, 440), (424, 440), 6, True)]
    # dots = [LinearDot((376, 246), (376, 486), 4, False), LinearDot((424, 486), (424, 246), 4, False), LinearDot((472, 246), (472, 486), 4, False), LinearDot((520, 486), (520, 246), 4, False), LinearDot((568, 246), (568, 486), 4, False), LinearDot((616, 486), (616, 246), 4, False), LinearDot((664, 246), (664, 486), 4, False), LinearDot((712, 486), (712, 246), 4, False), LinearDot((760, 246), (760, 486), 4, False), LinearDot((808, 486), (808, 246), 4, False), LinearDot((856, 246), (856, 486), 4, False), LinearDot((904, 486), (904, 246), 4, False)]
    # dots = [PathDot((568, 296), (568, 296), (712, 440), 3, True, True), PathDot((616, 296), (568, 296), (712, 440), 3, True, True), PathDot((664, 296), (568, 296), (712, 440), 3, True, True), PathDot((712, 296), (568, 296), (712, 440), 3, True, True), PathDot((712, 344), (568, 296), (712, 440), 3, True, True), PathDot((712, 392), (568, 296), (712, 440), 3, True, True), PathDot((712, 440), (568, 296), (712, 440), 3, True, True), PathDot((664, 440), (568, 296), (712, 440), 3, True, True), PathDot((616, 440), (568, 296), (712, 440), 3, True, True), PathDot((568, 440), (568, 296), (712, 440), 3, True, True)]
    # dots = [SpinDotParent((640, 464), 1.75, 5, 36, 0, True)]
    # dots = [SpinDotParent((640, 368), 1.2, 4, 96, -24, False)]
    # dots = [SpinDotParent((400, 224), 2.2, 2, 36, 0, True), SpinDotParent((592, 224), 2.2, 2, 36, 0, True), SpinDotParent((784, 224), 2.2, 2, 36, 0, True), SpinDotParent((976, 224), 2.2, 2, 36, 0, True), SpinDotParent((400, 512), 2.2, 2, 36, 0, True), SpinDotParent((592, 512), 2.2, 2, 36, 0, True), SpinDotParent((784, 512), 2.2, 2, 36, 0, True), SpinDotParent((976, 512), 2.2, 2, 36, 0, True)]
    # dots = [LinearDot((376, 200), (376, 536), 8, False), LinearDot((424, 536), (424, 200), 8, False), LinearDot((472, 200), (472, 536), 8, False), LinearDot((520, 536), (520, 200), 8, False), LinearDot((568, 200), (568, 536), 8, False), LinearDot((616, 536), (616, 200), 8, False), LinearDot((664, 200), (664, 536), 8, False), LinearDot((712, 536), (712, 200), 8, False), LinearDot((760, 200), (760, 536), 8, False), LinearDot((808, 536), (808, 200), 8, False), LinearDot((856, 200), (856, 536), 8, False), LinearDot((904, 536), (904, 200), 8, False)]
    dots = []

    # end = pygame.Rect(928, 224, 144, 288)
    # end = pygame.Rect(928, 320, 144, 96)
    # end = pygame.Rect(592, 320, 96, 96)
    # end = pygame.Rect(304, 416, 144, 96)
    # end = pygame.Rect(736, 320, 48, 96)
    # end = pygame.Rect(208, 512, 96, 96)
    # end = pygame.Rect(928, 320, 144, 96)
    end = pygame.Rect(880, 320, 96, 96)

    # coins = []
    # coins = [Coin(640, 368)]
    # coins = [Coin(568, 248)]
    # coins = [Coin(640, 320), Coin(784, 464), Coin(640, 608)]
    # coins = []
    # coins = [Coin(328, 440), Coin(520, 440), Coin(712, 440), Coin(904, 440)]
    # coins = [Coin(376, 200), Coin(904, 200), Coin(376, 536), Coin(904, 536)]
    coins = [Coin(856, 152), Coin(856, 584), Coin(424, 584)]

    # cp = []
    # cp = []
    # cp = []
    # cp = []
    # cp = [(pygame.Rect(976, 128, 48, 48), (984, 136), False), (pygame.Rect(208, 224, 48, 48), (216, 232), False)]
    # cp = [(pygame.Rect(880, 320, 192, 96), (960, 352), False)]
    # cp = []
    cp = []

    with open(os.path.join(f'level{num}.csv')) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    # map = load_map(num)['map']
    data = {'map': map, 'walls': walls, 'home': home, 'dots': dots, 'end': end, 'coins': coins, 'checkpoints': cp}
    # data = load_map(num)
    data['checkpoints'] = cp
    with open(f'level{num}.pkl', 'wb') as f:
        data = pickle.dump(data, f, -1)
    f.close()


def load_map(num):
    try:
        with open('level'+str(num)+'.pkl', 'rb') as f:
            data = pickle.load(f)
        f.close()
        return data
    except:
        return None

# set_map(8)
