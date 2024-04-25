colors = ['red', 'blue', 'green']

class Set():
    def __init__(self, set: str):
        for color in colors:
            self.__setattr__(color, 0)
        for color in set.split(', '):
            value, color = color.split()
            self.__setattr__(color, int(value))

games = [
    [Set(set) for set in line.split(': ')[1].rstrip().split('; ')]
    for line in open('./input/day2.txt')
]

def part_one(restrictions=[('red', 12), ('green', 13), ('blue', 14)]):
    total = 0
    for i, game in enumerate(games):
        valid = True
        for set in game:
            for (color, restriction) in restrictions:
                value = set.__getattribute__(color)
                if value > restriction:
                    valid = False
                    break
        if valid:
            total += i+1
    print(total)
    
def part_two():
    total = 0
    for game in games:
        min = {color: 0 for color in colors}
        for set in game:
            for color in colors:
                value = set.__getattribute__(color)
                min[color] = max(value, min[color])
        power = 1
        for color in colors:
            power *= min[color]
        total += power
    print(total)
    
part_one()
part_two()