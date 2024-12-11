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
  stones = [int(x) for x in open('./input/day11.txt').read().split()]
  for i in range(n+1):
    stones = open('./input/day11.txt').read().split()
    for _ in range(i):
      # print(' '.join(stones))
      stones = blink(stones)
    print(i, len(stones))
part_one(25)

# def part_two(n):
#   stones = {}
#   for stone in open('./input/day11.txt').read().split():
#     stones.setdefault(stone, 0)
#     stones[stone] += 1
#   print(stones)
#   for stone, count in stones.items():
#     new_stones = stones.copy()
#     if stone == '0':
#       new_stones.setdefault('1', 0)
#       new_stones['1'] += count
#       new_stones[0] = 0
#     elif len(stone) % 2 == 0:
#       m = int(len(stone) / 2)
#       left = str(int(stone[:m]))
#       right = str(int(stone[m:]))
#       new_stones.setdefault(left, 0)
#       new_stones.setdefault(right, 0)
#     else:
#       stone = int(stone) * 2024
#       new_stones.append(str(stone))
# part_two(25)