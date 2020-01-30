f = open('input1.txt', 'r')
# f = [12, 14, 1969, 100756]
total_fuel = 0
for line in f:
    fuel = 0
    num = int(line)
    while num > 0:
        num = num // 3
        num = num - 2
        if num > 0:
            fuel += num
    # print(fuel)
    total_fuel += fuel

print(total_fuel)