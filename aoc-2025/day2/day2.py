import os

path = os.path.dirname(os.path.abspath(__file__))

data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

data = open(path + "/day2.txt").read()

id_ranges = [
  [int(y) for y in x.split("-")]
  for x in data.split(",")
]

def part_one():
  total = 0
  for id_range in id_ranges:
    start, end = id_range 
    for id in range(start, end+1):
      id = str(id)
      n = len(id)
      if n % 2 == 0:
        m = int(n/2)
        start, end = id[:m], id[m:]
        if start == end:
          total += int(id)
  print(total)
  
def all_equal(chunks):
  for a in chunks:
    for b in chunks:
      if a != b:
        return False
  return True
  

total = 0
for id_range in id_ranges:
  start, end = id_range 
  for id in range(start, end+1):
    id = str(id)
    for n in range(1, len(id)):
      chunks = [id[i:i + n] for i in range(0, len(id), n)]
      if all_equal(chunks):
        total += int(id)
        break
print(total)