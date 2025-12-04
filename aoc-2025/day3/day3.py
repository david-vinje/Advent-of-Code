import os
from queue import PriorityQueue

path = os.path.dirname(os.path.abspath(__file__))

banks = [list(x.rstrip()) for x in open(path + '/day3.txt').readlines()]

def part_one():
  total = 0
  for bank in banks:
    combinations = PriorityQueue()
    for i, a in enumerate(bank):
      for b in bank[i+1:]:
        combinations.put(-int(a + b))
    joltage = -1 * combinations.get()
    total += joltage
  print(total)