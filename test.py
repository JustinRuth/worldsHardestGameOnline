from dot import *

def coord_from_pos(x, y):
    x2 = (x*48)+64
    y2 = (y*48)+32
    return x2, y2

print(coord_from_pos(10, 5))
print(coord_from_pos(13, 8))

dot1  = PathDot((568, 296), (568, 296), (712, 440), 6, True, True)
dot2  = PathDot((616, 296), (568, 296), (712, 440), 6, True, True)
dot3  = PathDot((664, 296), (568, 296), (712, 440), 6, True, True)
dot4  = PathDot((712, 296), (568, 296), (712, 440), 6, True, True)
dot5  = PathDot((712, 344), (568, 296), (712, 440), 6, True, True)
dot6  = PathDot((712, 392), (568, 296), (712, 440), 6, True, True)
dot7  = PathDot((712, 440), (568, 296), (712, 440), 6, True, True)
dot8  = PathDot((664, 440), (568, 296), (712, 440), 6, True, True)
dot9  = PathDot((616, 440), (568, 296), (712, 440), 6, True, True)
dot10 = PathDot((568, 440), (568, 296), (712, 440), 6, True, True)
dot11 = PathDot((568, 392), (568, 296), (712, 440), 6, True, True)
dot12 = PathDot((568, 344), (568, 296), (712, 440), 6, True, True)
dots = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12]

print(dots)