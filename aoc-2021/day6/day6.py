def solve(n):
    lanterns = [int(x) for x in open('.//day6.txt').readline().split(',')]
    counter = {}
    for i in range(9): 
        counter.setdefault(i, 0)
    for lantern in lanterns:
        counter[lantern] += 1
    for _ in range(n):
        zeroes = counter[0]
        for count in range(8):
            counter[count] = counter[count+1]
        counter[8] = zeroes
        counter[6] += zeroes
    print(sum(counter.values()))

solve(80)
solve(256)
