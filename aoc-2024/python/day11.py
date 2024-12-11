# stones = [int(x) for x in open('./input/day11.txt').read().split()]

# 0 -> 1
# 2n -> split
# 2n-1 -> n*=2024

def blink(stones: dict):
  new_stones = {}
  for stone, count in stones.items():
    if int(stone) == 0:
      new_stones.setdefault(stone, 0)
      new_stones['1'] += count
    elif len(stone) % 2 == 0:
      m = int(len(stone) / 2)
      left, right = int(stone[:m]), int(stone[m:])
      new_stones.append(str(left))
      new_stones.append(str(right))
    else:
      stone = int(stone) * 2024
      new_stones.append(str(stone))
  return new_stones

def part_one(n):
  for i in range(n+1):
    stones = open('./input/day11.txt').read().split()
    for _ in range(i):
      # print(' '.join(stones))
      stones = blink(stones)
    print(i, len(stones))
# part_one(75)

def part_two():
  stones = {}
  for stone in open('./input/day11.txt').read().split():
    stones.setdefault(stone, 0)
    stones[stone] += 1
  print(stones)

part_two()