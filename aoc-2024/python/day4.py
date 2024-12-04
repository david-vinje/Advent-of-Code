
letters = [list(line) for line in open('./input/day4.txt')]
n = len(letters)
word = 'XMAS', 0
count = 0

def check_left(i, j):
  global count
  if j >= 3 \
    and letters[i][j-1] == 'M' \
    and letters[i][j-2] == 'A' \
    and letters[i][j-3] == 'S':
      count += 1
  
def check_right(i, j):
  global count
  if j < n-3 \
    and letters[i][j+1] == 'M' \
    and letters[i][j+2] == 'A' \
    and letters[i][j+3] == 'S':
      count += 1
    
def check_down(i, j):
  global count
  if i < n-3 \
    and letters[i+1][j] == 'M' \
    and letters[i+2][j] == 'A' \
    and letters[i+3][j] == 'S':
      count += 1
  
def check_up(i, j):
  global count
  if i >= 3 \
    and letters[i-1][j] == 'M' \
    and letters[i-2][j] == 'A' \
    and letters[i-3][j] == 'S':
      # print(i, j)
      count += 1
  
def check_up_left(i, j):
  global count
  if i >= 3 and j >= 3 \
    and letters[i-1][j-1] == 'M' \
    and letters[i-2][j-2] == 'A' \
    and letters[i-3][j-3] == 'S':
      count += 1
  
def check_up_right(i, j):
  global count
  if i >= 3 and j < n-3 \
    and letters[i-1][j+1] == 'M' \
    and letters[i-2][j+2] == 'A' \
    and letters[i-3][j+3] == 'S':
      count += 1
  
def check_down_left(i, j):
  global count
  if i < n-3 and j >= 3 \
    and letters[i+1][j-1] == 'M' \
    and letters[i+2][j-2] == 'A' \
    and letters[i+3][j-3] == 'S':
      count += 1
  
def check_down_right(i, j):
  global count
  if i < n-3 and j < n-3 \
    and letters[i+1][j+1] == 'M' \
    and letters[i+2][j+2] == 'A' \
    and letters[i+3][j+3] == 'S':
      count += 1

for i, row in enumerate(letters):
  for j, letter in enumerate(row):
    if letter != 'X':
      continue
    check_left(i, j)
    check_right(i, j)
    check_up(i, j)
    check_down(i, j)
    check_down_right(i, j)
    check_down_left(i, j)
    check_up_right(i, j)
    check_up_left(i, j)
  
print(count)
    
count = 0
for i, row in enumerate(letters):
  for j, letter in enumerate(row):
    if 0 < i < n-1 and 0 < j < n-1 and letters[i][j] == 'A':
      left = letters[i-1][j-1] + letters[i+1][j+1]
      left = left == 'MS' or left == 'SM'
      right = letters[i-1][j+1] + letters[i+1][j-1]
      right = right == 'MS' or right == 'SM'
      if left and right:
        count += 1
        
print(count)