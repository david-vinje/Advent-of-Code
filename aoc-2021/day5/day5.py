# dim = 0

# def parse(coord):
#     global dim
#     coord = int(coord)
#     dim = max(dim, coord)
#     return coord

lines = [
    [
        [int(coord) for coord in coords.split(',')] 
        for coords in line.split(' -> ')
    ] for line in open('..//day5.txt').readlines()
]

def part_one():
    count = {}
    for line in lines:
        (x1, y1), (x2, y2) = line
        if x1 == x2:
            direction = 1 if y1 < y2 else -1
            for y in range(y1, y2+direction, direction):
                if (x1, y) not in count:
                    count[(x1, y)] = 0
                count[(x1, y)] += 1
        elif y1 == y2:
            direction = 1 if x1 < x2 else -1
            for x in range(x1, x2+direction, direction):
                if (x, y1) not in count:
                    count[(x, y1)] = 0
                count[(x, y1)] += 1
    count = {k: v for k, v in count.items() if v > 1}    
    print(len(count.keys()))

part_one()

def part_two():
    count = {}
    for line in lines:
        (x1, y1), (x2, y2) = line
        if x1 == x2:
            direction = 1 if y1 < y2 else -1
            for y in range(y1, y2+direction, direction):
                if (x1, y) not in count:
                    count[(x1, y)] = 0
                count[(x1, y)] += 1
        elif y1 == y2:
            direction = 1 if x1 < x2 else -1
            for x in range(x1, x2+direction, direction):
                if (x, y1) not in count:
                    count[(x, y1)] = 0
                count[(x, y1)] += 1
        else:
            x_direction = 1 if x1 < x2 else -1
            y_direction = 1 if y1 < y2 else -1
            distance = abs(x1 - x2) + 1
            for d in range(distance):
                x = x1 + d * x_direction
                y = y1 + d * y_direction
                if (x, y) not in count:
                    count[(x, y)] = 0
                count[(x, y)] += 1
    count = {k: v for k, v in count.items() if v > 1}    
    print(len(count.keys()))
    
part_two()