def transform(stone):
  if stone == '0':
    return ['1']
  if len(stone) % 2 == 0:
    m = int(len(stone) / 2)
    left = str(int(stone[:m]))
    right = str(int(stone[m:]))
    return [left, right]  
  return [str(int(stone) * 2024)]

def blink(stones: list):
  new_stones = []
  for stone in stones:
    new_stones += transform(stone)
  return new_stones

def part_one(n):
    stones = open('./input/day11.txt').read().split()
    for _ in range(n):
      stones = blink(stones)
    print(len(stones))

def part_two(n):
  stones = {}
  for stone in open('./input/day11.txt').read().split():
    stones.setdefault(stone, 0)
    stones[stone] += 1
  for _ in range(n):
    # print(stones)
    new_stones = stones.copy()
    for stone, count in stones.items():
      new_stones[stone] -= count
      for new_stone in transform(stone):
        new_stones.setdefault(new_stone, 0)
        new_stones[new_stone] += count
    stones = new_stones
  # print(stones)
  print(sum(stones.values()))
  
part_one(25)
part_two(75)