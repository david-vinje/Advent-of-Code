lines = [
    [ 
     io.split() for io in line.split(' | ')
    ] for line in open(path + '/day8.txt').readlines()
]

def part_one():
    count = 0
    for (_, output) in lines:
        for segment in output:
            n = len(segment)
            if n < 5 or n > 6:
                count += 1
    print(count)
    
part_one()

def part_two():
    total = 0
    for line in lines:
        input, output = [
            [
                ''.join(sorted(list(segment))) for segment in io
            ] for io in line
        ]
        clock, letters = {}, {}
        fives, sixes = set(), set()
        missing = set(list('abcdefg'))
        for segment in input:
            n = len(segment)
            if n == 2:
                clock['1'] = segment
            elif n == 3:
                clock['7'] = segment
            elif n == 4:
                clock['4'] = segment
            elif n == 5:
                fives.add(segment)
            elif n == 6:
                sixes.add(segment)
            elif n == 7:
                clock['8'] = segment
        # a
        for letter in clock['7']:
            if letter not in clock['1']:
                letters['a'] = letter
                missing.remove(letter)
        # c
        for segment in sixes:
            for letter in clock['1']:
                if letter not in segment:
                    letters['c'] = letter
                    missing.remove(letter)
                    clock['6'] = segment
        sixes.remove(clock['6'])
        # f
        for letter in clock['1']:
            if letter != letters['c']:
                letters['f'] = letter
                missing.remove(letter)
        # d
        for segment in sixes:
            for letter in clock['4']:
                if letter in clock['6'] and letter not in segment:
                    letters['d'] = letter
                    missing.remove(letter)
                    clock['0'] = segment
        sixes.remove(clock['0'])
        clock['9'] = sixes.pop()
        # e
        for letter in clock['6']:
            if letter not in clock['9']:
                letters['e'] = letter
                missing.remove(letter)
        # b
        for letter in missing:
            if letter in clock['4']:
                letters['b'] = letter
        # g
        missing.remove(letters['b'])
        letters['g'] = missing.pop()
        # missing: 2, 3, 5
        for segment in fives:
            if letters['f'] not in segment:
                clock['2'] = segment
            elif letters['c'] not in segment:
                clock['5'] = segment
            else:
                clock['3'] = segment
        value = ''
        clock = {v: k for k, v in clock.items()}
        for segment in output:
            value += clock[segment]
        total += int(value)
    print(total)
part_two()
        
# # 2: 1
# # 3: 7
# # 4: 4
# # 5: 2, 3, 5
# # 6: 0, 6, 9
# # 7: 8