crabs = [
    int(x) for x in open('.//day7.txt').readline().split(',')
]
crabs.sort()

n = len(crabs)

def part_one():
    m = crabs[round(n/2)]
    fuel = 0
    for crab in crabs:
        fuel += abs(crab-m)
    print(fuel)
    
def part_two():
    m = round(sum(crabs)/n)
    fuel = 0
    for crab in crabs:
        dist = abs(crab - m)
        fuel += dist*(dist+1) / 2
    print(int(fuel))

part_one()
part_two()