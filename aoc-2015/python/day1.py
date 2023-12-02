# read input
line = open('aoc-2015/input/day1.txt').readline()

# part one
floor = sum([1 if x is '(' else -1 for x in line])
print(floor)

# part two
floor, count = 0, 0
for i in line:
    count += 1
    floor += 1 if i == '(' else -1
    if floor < 0:
        break
print(count)
