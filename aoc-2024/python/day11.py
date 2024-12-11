stones = open('./input/day11.txt').read().split()
# stones = [int(x) for x in open('./input/day11.txt').read().split()]

# 0 -> 1
# 2n -> split
# 2n-1 -> n*=2024

def blink(stones: list):
  new_stones = []
  for stone in stones:
    if int(stone) == 0:
      new_stones.append('1')
    elif len(stone) % 2 == 0:
      m = int(len(stone) / 2)
      left, right = int(stone[:m]), int(stone[m:])
      new_stones.append(str(left))
      new_stones.append(str(right))
    else:
      stone = int(stone) * 2024
      new_stones.append(str(stone))
  return new_stones

for i in range(75):
  stones = blink(stones)
res = ' '.join(stones) 
print(res) 