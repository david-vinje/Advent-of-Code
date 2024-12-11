stones = open('./input/day11.txt').read().split()

def blink(stones: list):
  new_stones = []
  for stone in stones:
    if stone == '0':
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

# stones = list(range(1, 10))
# for i in range(1, 10):
#   stone = str(i * 2024)
#   m = int(len(stone) / 2)
#   left, right = stone[:m], stone[m:]
#   m = int(len(left) / 2)
#   a, b = left[:m], left[m:]
#   c, d = right[:m], right[m:]
#   print(i, ':', [a, b, c, d])

# for stone in ['20', '44', '68', '92', '16']:
#   m = int(len(stone) / 2)
#   left, right = stone[:m], stone[m:]
#   print([left, right])
  
for i in range(25):
  stones = blink(stones)
print(len(stones))