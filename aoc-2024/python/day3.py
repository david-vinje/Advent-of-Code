import re

line = open('./input/day3.txt').readline()
mults = re.search(r"mul\([0-9],[0-9]\)", line)
n = mults.groups().count(0)
print(n)
for i in range(0, n):
  print(mults.group(i))
