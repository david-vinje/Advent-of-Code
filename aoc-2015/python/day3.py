# read input
input = open('aoc-2015/input/day3.txt').readline()

def move(pos, dir):
    r, c = pos
    if dir == '>':
        return (r, c+1)
    if dir == '<':
        return (r, c-1)
    if dir == '^':
        return (r-1, c)
    return (r+1, c)

# part one
santa_one = (0, 0)
houses = {santa_one}
for dir in input:
    santa_one = move(santa_one, dir)
    houses.add(santa_one)
print(len(houses))

# part two
santa_one = (0, 0)
santa_two = (0, 0)
houses = {santa_one}
for i in range(0, len(input), 2):
    santa_one = move(santa_one, input[i])
    santa_two = move(santa_two, input[i+1])
    houses.add(santa_one)   
    houses.add(santa_two)
print(len(houses))