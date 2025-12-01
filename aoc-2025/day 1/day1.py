import os
path = os.path.dirname(os.path.abspath(__file__))

rotations = [
  "L68",
  "L30",
  "R48",
  "L5",
  "R60",
  "L55",
  "L1",
  "L99",
  "R14",
  "L82",
  "R1000"
]

# rotations = ["R49", "R101"]
# rotations = ["L49", "L101"]

rotations = open(path + '/day1.txt').readlines()

def part_one():
  dial = 50
  count = 0
  for rotation in rotations:
    direction = -1 if rotation[0] == "L" else 1
    amplitude = int(rotation[1:])
    dial = (dial + direction * amplitude) % 100
    if dial == 0:
      count += 1
  print(count)
     
def part_two():
  dial = 50
  count = 0
  for rotation in rotations:
    direction = -1 if rotation[0] == "L" else 1
    amplitude = int(rotation[1:])
    for _ in range(amplitude):
      dial = (dial + direction) % 100
      if dial == 0:
        count += 1
  print(count)
  
part_one()
part_two()
