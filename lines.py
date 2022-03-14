# points = [(3, 4), (6, 4), (6, 9), (7, 9), (7, 5), (16, 5), (16, 4), (21, 4), (21, 10), (18, 10), (18, 5), (17, 5), (17, 9), (8, 9), (8, 10), (3, 10)]
# points = [(3, 6), (6, 6), (6, 4), (18, 4), (18, 6), (21, 6), (21, 8), (18, 8), (18, 10), (6, 10), (6, 8), (3, 8)]
points = [(10, 4), (11, 4), (11, 5), (14, 5), (14, 9), (10, 9)]
prev_point = points[-1]
lines = []
for point in points:
    start_x = prev_point[0]*48
    start_y = prev_point[1]*48
    end_x = point[0]*48
    end_y = point[1]*48
    if end_x == start_x:
        if end_y > start_y:
            start_y -= 2
            end_y += 3
        else:
            start_y += 3
            end_y -= 2
    else:
        if start_x > end_x:
            start_x -= 3
            end_x += 3
        else:
            start_x += 3
            end_x -= 3
    lines.append(((start_x, start_y), (end_x, end_y)))
    prev_point = point

print(lines)

