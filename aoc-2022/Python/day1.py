# # read input
# lines = open('aoc-2022/input/day1.txt').readlines()

# # part one
# sums = []
# sum = 0
# highest = 0
# for line in lines:
#     if line == '\n':
#         sums.append(sum)
#         highest = max(highest, sum)
#         sum = 0
#     else:
#         sum += int(line)
# highest = max(highest, sum)
# print(highest)

# # part two
# sums.append(sum)
# sorted = sorted(sums, reverse=True)
# print(sorted[0] + sorted[1] + sorted[2])

input = [[int(calorie) for calorie in elf.split('\n')] for elf in open('aoc-2022/input/day1.txt').read().split('\n\n')]
print(input)