lines = [x.rstrip('\n') for x in open('./input/day3.txt').readlines()]

def part_one():
    count = [(0, 0)] * len(lines[0])
    for line in lines:
        for i, bit in enumerate(line):
            if bit == '0':
                count[i] = (count[i][0]+1, count[i][1])
            else:
                count[i] = (count[i][0], count[i][1]+1)
        gamma, epsilon = '', ''
        for bit in count:
            if bit[0] > bit[1]:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    print(gamma * epsilon)

part_one()