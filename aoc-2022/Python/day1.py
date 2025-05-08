elfs = [
    sum([int(calorie) for calorie in elf.split("\n")])
    for elf in open("aoc-2022/input/day1.txt").read().split("\n\n")
]

part_one = max(elfs)
part_two = sum(sorted(elfs, reverse=True)[:3])

print(part_one)
print(part_two)
