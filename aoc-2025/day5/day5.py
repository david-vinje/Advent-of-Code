import os

path = os.path.dirname(os.path.abspath(__file__))

ranges, ingredients = [x.split("\n") for x in open(path + '/day5.txt').read().split("\n\n")]
ranges = [[int(y) for y in x.split("-")] for x in ranges]
ingredients = [int(x) for x in ingredients]

def part_one():
  count = 0
  for ingredient in ingredients:
    for start, end in ranges:
      if ingredient >= start and ingredient <= end:
        count += 1
        break

  print(count)

count = 0
for start, end =