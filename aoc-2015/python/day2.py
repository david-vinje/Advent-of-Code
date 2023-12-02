# read input
lines = [[int(x) for x in line.split('x')] for line in open('aoc-2015/input/day2.txt').readlines()]

# part one
sum = 0
for l, w, h in lines:
    s1 = l*w
    s2 = w*h
    s3 = l*h
    sum += 2*s1 + 2*s2 + 2*s3 + min(min(s1, s2), s3)
print(sum)

# part two
sum = 0
for line in lines:
    l, w, h  = line
    dims = sorted(line)
    sum += l*w*h + 2*dims[0] + 2*dims[1]
print(sum)