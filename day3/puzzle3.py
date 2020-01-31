import numpy as np

def extract(strline):
    pieces = strline.split(',')
    return pieces

f = open('input3.txt', 'r')
# f = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
f = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
    'U62,R66,U55,R34,D71,R55,D58,R83']
# f = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
#     'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

wires = [extract(line) for line in f]

dimv = 0
dimh = 0
for w in wires:
    vertical = 0
    horizontal = 0
    for item in w:
        direction = item[0]
        num = int(item[1:])
        if direction == 'R':
            horizontal += num
        elif direction == 'L':
            horizontal -= num
        elif direction == 'D':
            vertical -= num
        else:
            vertical += num
        if abs(vertical) > dimv:
            dimv = abs(vertical) + 1
        if abs(horizontal) > dimh:
            dimh = abs(horizontal) + 1

grid = np.zeros((2*dimh, 2*dimv))
# grid[dimh, dimv] = -1

intersections = []
val = 0
dec = 0
for w in wires:
    dec += 0.1
    val += 1
    locx = dimh
    locy = dimv
    for item in w:
        newx = locx
        newy = locy
        direction = item[0]
        num = int(item[1:])
        for i in range(num):
            val = int(grid[newx, newy])
            if direction == 'R':
                newx += 1
            elif direction == 'L':
                newx -= 1
            elif direction == 'D':
                newy -= 1
            else:
                newy += 1
            prev = grid[newx, newy]
            if prev > 0:
                if prev % 1 == dec and prev < val:
                    val = int(prev) - 1
                elif prev % 1 != dec:
                    intersections.append(int(prev) + val + 1)
                    # print(grid[newx, newy], val+1)
            grid[newx, newy] = val + 1 + dec
        locx = newx
        locy = newy

print(np.min(intersections))
# print(grid)
# occurrences = np.where(grid == 3)
# best = float('inf')
# for idx in range(len(occurrences[0])):
#     x = occurrences[0][idx]
#     y = occurrences[1][idx]
#     dist = abs(dimh - x) + abs(dimv - y)
#     if dist < best:
#         best = dist

# print(best)