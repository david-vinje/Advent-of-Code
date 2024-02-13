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

def scrub(lst, is_oxygen):
    i = 0
    while len(lst) > 1:
        count = {'0': 0, '1': 0}
        for line in lst:
            bit = line[i]
            count[bit] += 1
        if is_oxygen:
            if count['0'] > count['1']:
                lst = [x for x in lst if x[i] == '0']
            else:
                lst = [x for x in lst if x[i] == '1']
        else:
            if count['1'] < count['0']:
                lst = [x for x in lst if x[i] == '1']
            else:
                lst = [x for x in lst if x[i] == '0']
        i += 1
    return lst[0]

def part_two():
    oxygen = scrub(lines, True)  
    carbondioxide = scrub(lines, False)
    carbondioxide, oxygen = int(carbondioxide, 2), int(oxygen, 2)
    print(carbondioxide * oxygen)

part_one()
part_two()