lines = [(a, int(b)) for (a, b) in [x.split() for x in open('..//day2.txt').readlines()]]

def part_one():
    depth, position = 0, 0
    for direction, amount in lines:
        if direction == 'forward':
            position += amount
        elif direction == 'down':
            depth += amount
        else:
            depth -= amount
    print(depth * position)

def part_two():
    aim, depth, position = 0, 0, 0
    for direction, amount in lines:
        if direction == 'forward':
            position += amount
            depth += aim * amount
        elif direction == 'down':
            aim += amount
        else:
            aim -= amount
    print(depth * position)

part_one()
part_two()