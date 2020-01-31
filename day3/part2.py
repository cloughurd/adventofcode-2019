f = open('input3.txt', 'r')
wires = [line.split(',') for line in f]

location_lists = []
for w in wires:
    x = 0
    y = 0
    wire_locations = []
    prev = 0
    for item in w:
        direction = item[0]
        num = int(item[1:])
        for i in range(num):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            else:
                x -= 1
            
            prev += 1
            for previous in wire_locations:
                if previous[0] == x and previous[1] == y:
                    if previous[2] < prev:
                        prev = previous[2]
            wire_locations.append((x, y, prev))
    location_lists.append(wire_locations)

w1_path = location_lists[0]
w2_path = location_lists[1]

best = float('inf')
for i in range(len(w1_path)):
    item = w1_path[i]
    for other in w2_path:
        if item[0] == other[0] and item[1] == other[1]:
            if item[2] + other[2] < best:
                best = item[2] + other[2]

print(best)