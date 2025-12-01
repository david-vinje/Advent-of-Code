import os

path = os.path.dirname(os.path.abspath(__file__))

all_dims = [
  [int(y) for y in x.split('x')]
  for x in open(path + '/day2.txt')
]

total = 0
for dims in all_dims:
  length, width, height = dims
  sides = length * width, length * height, width * height
  slack = min(min(sides[0], sides[1]), sides[2])
  total += 2 * sum(sides) + slack
print(total)

total = 0
for dims in all_dims:
  dims.sort()
  ribbon = dims[0] * dims[1] * dims[2]
  total += 2 * (dims[0] + dims[1]) + ribbon
print(total)

