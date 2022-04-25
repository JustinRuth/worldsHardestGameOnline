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
    # walls = [pygame.Rect(398, 126, 6, 486), pygame.Rect(403, 126, 187, 6), pygame.Rect(590, 126, 6, 54), pygame.Rect(595, 174, 91, 6), pygame.Rect(686, 126, 6, 54), pygame.Rect(691, 126, 187, 6), pygame.Rect(878, 126, 6, 198), pygame.Rect(883, 318, 91, 6), pygame.Rect(974, 318, 6, 102), pygame.Rect(883, 414, 91, 6), pygame.Rect(878, 414, 6, 198), pygame.Rect(691, 606, 187, 6), pygame.Rect(686, 558, 6, 54), pygame.Rect(595, 558, 91, 6), pygame.Rect(590, 558, 6, 54), pygame.Rect(403, 606, 187, 6), pygame.Rect(494, 174, 6, 54), pygame.Rect(499, 174, 43, 6), pygame.Rect(542, 174, 6, 102), pygame.Rect(451, 270, 91, 6), pygame.Rect(446, 222, 6, 54), pygame.Rect(451, 222, 43, 6), pygame.Rect(446, 318, 6, 102), pygame.Rect(451, 318, 91, 6), pygame.Rect(542, 318, 6, 102), pygame.Rect(451, 414, 91, 6), pygame.Rect(446, 462, 6, 102), pygame.Rect(451, 462, 91, 6), pygame.Rect(542, 462, 6, 102), pygame.Rect(451, 558, 91, 6), pygame.Rect(734, 174, 6, 102), pygame.Rect(739, 174, 91, 6), pygame.Rect(830, 174, 6, 102), pygame.Rect(739, 270, 91, 6), pygame.Rect(734, 318, 6, 102), pygame.Rect(739, 318, 91, 6), pygame.Rect(830, 318, 6, 102), pygame.Rect(739, 414, 91, 6), pygame.Rect(734, 462, 6, 102), pygame.Rect(739, 462, 91, 6), pygame.Rect(830, 462, 6, 102), pygame.Rect(739, 558, 91, 6), pygame.Rect(590, 222, 6, 294), pygame.Rect(595, 222, 91, 6), pygame.Rect(686, 222, 6, 294), pygame.Rect(595, 510, 91, 6)]
    # walls = [pygame.Rect(206, 126, 6, 486), pygame.Rect(211, 126, 91, 6), pygame.Rect(302, 126, 6, 102), pygame.Rect(307, 222, 91, 6), pygame.Rect(398, 126, 6, 102), pygame.Rect(403, 126, 283, 6), pygame.Rect(686, 126, 6, 294), pygame.Rect(691, 414, 91, 6), pygame.Rect(782, 126, 6, 294), pygame.Rect(787, 126, 283, 6), pygame.Rect(1070, 126, 6, 294), pygame.Rect(979, 414, 91, 6), pygame.Rect(974, 222, 6, 198), pygame.Rect(883, 222, 91, 6), pygame.Rect(878, 222, 6, 294), pygame.Rect(883, 510, 187, 6), pygame.Rect(1070, 510, 6, 102), pygame.Rect(787, 606, 283, 6), pygame.Rect(782, 510, 6, 102), pygame.Rect(499, 510, 283, 6), pygame.Rect(494, 510, 6, 102), pygame.Rect(211, 606, 283, 6), pygame.Rect(302, 318, 6, 198), pygame.Rect(307, 318, 187, 6), pygame.Rect(494, 222, 6, 102), pygame.Rect(499, 222, 91, 6), pygame.Rect(590, 222, 6, 198), pygame.Rect(403, 414, 187, 6), pygame.Rect(398, 414, 6, 102), pygame.Rect(307, 510, 91, 6)]
    walls = [pygame.Rect(494, 126, 6, 294), pygame.Rect(499, 126, 139, 6), pygame.Rect(638, 126, 6, 102), pygame.Rect(547, 222, 91, 6), pygame.Rect(542, 222, 6, 54), pygame.Rect(547, 270, 43, 6), pygame.Rect(590, 270, 6, 198), pygame.Rect(499, 462, 91, 6), pygame.Rect(494, 462, 6, 54), pygame.Rect(499, 510, 235, 6), pygame.Rect(734, 462, 6, 54), pygame.Rect(643, 462, 91, 6), pygame.Rect(638, 270, 6, 198), pygame.Rect(643, 270, 43, 6), pygame.Rect(686, 126, 6, 150), pygame.Rect(691, 126, 139, 6), pygame.Rect(830, 126, 6, 102), pygame.Rect(739, 222, 91, 6), pygame.Rect(734, 222, 6, 198), pygame.Rect(739, 414, 91, 6), pygame.Rect(830, 414, 6, 150), pygame.Rect(739, 558, 91, 6), pygame.Rect(734, 558, 6, 54), pygame.Rect(499, 606, 235, 6), pygame.Rect(494, 558, 6, 54), pygame.Rect(403, 558, 91, 6), pygame.Rect(398, 414, 6, 150), pygame.Rect(403, 414, 91, 6)]

    # home = (260, 260)
    # home = (250, 350)
    # home = (624, 352)
    # home = (624, 184)
    # home = (216, 136)
    # home = (240, 160)
    # home = (250, 350)
    # home = (456, 184)
    # home = (240, 160)
    home = (552, 160)

    # dots = [LinearDot((424, 296), (856, 296), 6, True), LinearDot((856, 344), (424, 344), 6, True), LinearDot((424, 392), (856, 392), 6, True), LinearDot((856, 440), (424, 440), 6, True)]
    # dots = [LinearDot((376, 246), (376, 486), 4, False), LinearDot((424, 486), (424, 246), 4, False), LinearDot((472, 246), (472, 486), 4, False), LinearDot((520, 486), (520, 246), 4, False), LinearDot((568, 246), (568, 486), 4, False), LinearDot((616, 486), (616, 246), 4, False), LinearDot((664, 246), (664, 486), 4, False), LinearDot((712, 486), (712, 246), 4, False), LinearDot((760, 246), (760, 486), 4, False), LinearDot((808, 486), (808, 246), 4, False), LinearDot((856, 246), (856, 486), 4, False), LinearDot((904, 486), (904, 246), 4, False)]
    # dots = [PathDot((568, 296), (568, 296), (712, 440), 3, True, True), PathDot((616, 296), (568, 296), (712, 440), 3, True, True), PathDot((664, 296), (568, 296), (712, 440), 3, True, True), PathDot((712, 296), (568, 296), (712, 440), 3, True, True), PathDot((712, 344), (568, 296), (712, 440), 3, True, True), PathDot((712, 392), (568, 296), (712, 440), 3, True, True), PathDot((712, 440), (568, 296), (712, 440), 3, True, True), PathDot((664, 440), (568, 296), (712, 440), 3, True, True), PathDot((616, 440), (568, 296), (712, 440), 3, True, True), PathDot((568, 440), (568, 296), (712, 440), 3, True, True)]
    # dots = [SpinDotParent((640, 464), 1.75, 5, 36, 0, True)]
    # dots = [SpinDotParent((640, 368), 1.2, 4, 96, -24, False)]
    # dots = [SpinDotParent((400, 224), 2.2, 2, 36, 0, True), SpinDotParent((592, 224), 2.2, 2, 36, 0, True), SpinDotParent((784, 224), 2.2, 2, 36, 0, True), SpinDotParent((976, 224), 2.2, 2, 36, 0, True), SpinDotParent((400, 512), 2.2, 2, 36, 0, True), SpinDotParent((592, 512), 2.2, 2, 36, 0, True), SpinDotParent((784, 512), 2.2, 2, 36, 0, True), SpinDotParent((976, 512), 2.2, 2, 36, 0, True)]
    # dots = [LinearDot((376, 200), (376, 536), 8, False), LinearDot((424, 536), (424, 200), 8, False), LinearDot((472, 200), (472, 536), 8, False), LinearDot((520, 536), (520, 200), 8, False), LinearDot((568, 200), (568, 536), 8, False), LinearDot((616, 536), (616, 200), 8, False), LinearDot((664, 200), (664, 536), 8, False), LinearDot((712, 536), (712, 200), 8, False), LinearDot((760, 200), (760, 536), 8, False), LinearDot((808, 536), (808, 200), 8, False), LinearDot((856, 200), (856, 536), 8, False), LinearDot((904, 536), (904, 200), 8, False)]
    # dots = [PathDot((424, 152), (424, 152), (568, 296), 3.25, True, True), PathDot((424, 296), (424, 296), (568, 440), 3.25, True, True), PathDot((424, 440), (424, 440), (568, 584), 3.25, True, True), PathDot((856, 152), (712, 152), (856, 296), 3.25, False, True), PathDot((856, 296), (712, 296), (856, 440), 3.25, False, True), PathDot((856, 440), (712, 440), (856, 584), 3.25, False, True), PathDot((568, 200), (568, 200), (712, 536), 3.25, True, True)]
    # dots = [Dot(232, 464), Dot(280, 368), Dot(352, 248), Dot(352, 536), Dot(424, 176), Dot(544, 200), Dot(424, 464), Dot(496, 440), Dot(616, 272), Dot(568, 488), Dot(808, 560), Dot(808, 368), Dot(856, 272), Dot(1000, 272), Dot(928, 200), PathDot((232, 248), (232, 248), (280, 296), 6, True, True), PathDot((808, 152), (808, 152), (856, 200), 6, True, True), PathDot((808, 440), (808, 440), (856, 488), 6, True, True), PathDot((280, 584), (232, 536), (280, 584), 6, True, True), PathDot((472, 584), (424, 536), (472, 584), 6, True, True), PathDot((472, 296), (424, 248), (472, 296), 6, True, True), PathDot((664, 200), (616, 152), (664, 200), 6, True, True), PathDot((1048, 200), (1000, 152), (1048, 200), 6, True, True)]
    dots = [LinearDot((520, 296), (576, 296), 2, True), LinearDot((576, 344), (520, 344), 2, True), LinearDot((520, 392), (576, 392), 2, True), LinearDot((576, 440), (520, 440), 2, True), LinearDot((472, 440), (416, 440), 2, True), LinearDot((416, 488), (472, 488), 2, True), LinearDot((472, 536), (416, 536), 2, True), LinearDot((520, 592), (520, 536), 2, False), LinearDot((568, 536), (568, 592), 2, False), LinearDot((616, 592), (616, 536), 2, False), LinearDot((664, 536), (664, 592), 2, False), LinearDot((712, 592), (712, 536), 2, False), LinearDot((760, 440), (816, 440), 2, True), LinearDot((816, 488), (760, 488), 2, True), LinearDot((760, 536), (816, 536), 2, True), LinearDot((712, 296), (656, 296), 2, True), LinearDot((656, 344), (712, 344), 2, True), LinearDot((712, 392), (656, 392), 2, True), LinearDot((656, 440), (712, 440), 2, True)]

    # end = pygame.Rect(928, 224, 144, 288)
    # end = pygame.Rect(928, 320, 144, 96)
    # end = pygame.Rect(592, 320, 96, 96)
    # end = pygame.Rect(304, 416, 144, 96)
    # end = pygame.Rect(736, 320, 48, 96)
    # end = pygame.Rect(208, 512, 96, 96)
    # end = pygame.Rect(928, 320, 144, 96)
    # end = pygame.Rect(880, 320, 96, 96)
    # end = pygame.Rect(976, 320, 96, 96)
    end = pygame.Rect(668, 128, 144, 96)

    # coins = []
    # coins = [Coin(640, 368)]
    # coins = [Coin(568, 248)]
    # coins = [Coin(640, 320), Coin(784, 464), Coin(640, 608)]
    # coins = []
    # coins = [Coin(328, 440), Coin(520, 440), Coin(712, 440), Coin(904, 440)]
    # coins = [Coin(376, 200), Coin(904, 200), Coin(376, 536), Coin(904, 536)]
    # coins = [Coin(856, 152), Coin(856, 584), Coin(424, 584)]
    # coins = [Coin(1024, 560)]
    coins = []

    # cp = []
    # cp = []
    # cp = []
    # cp = []
    # cp = [(pygame.Rect(976, 128, 48, 48), (984, 136), False), (pygame.Rect(208, 224, 48, 48), (216, 232), False)]
    # cp = [(pygame.Rect(880, 320, 192, 96), (960, 352), False)]
    # cp = []
    # cp = []
    # cp = [(pygame.Rect(592, 416, 96, 96), (624, 448), False)]
    cp = []

    with open(os.path.join(f'levels/level{num}.csv')) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    # map = load_map(num)['map']
    data = {'map': map, 'walls': walls, 'home': home, 'dots': dots, 'end': end, 'coins': coins, 'checkpoints': cp}
    # data = load_map(num)
    # data['checkpoints'] = cp
    with open(f'levels/level{num}.pkl', 'wb') as f:
        data = pickle.dump(data, f, -1)
    f.close()


def load_map(num):
    try:
        with open('levels/level'+str(num)+'.pkl', 'rb') as f:
            data = pickle.load(f)
        f.close()
        return data
    except:
        return None

# set_map(10)