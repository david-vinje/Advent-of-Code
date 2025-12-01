import os

path = os.path.dirname(os.path.abspath(__file__))

nums = [[int(y) for y in x.split()] for x in open(path + '/day1.txt')]
lists = [[], []]
for (a, b) in nums:
  lists[0].append(a)
  lists[1].append(b)
for list in lists:
  list.sort()
  
def part_one():
  difference = 0
  for i in range(len(nums)):
    a, b = lists[0][i], lists[1][i]
    difference += abs(a - b)
  print(difference)
  
def part_two():
  similarity = 0
  for a in lists[0]:
    count = 0
    for b in lists[1]:
      if a == b:
        count += 1
    similarity += count * a
  print(similarity)

part_one()
part_two()