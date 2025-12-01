import os

path = os.path.dirname(os.path.abspath(__file__))

# document = [
#   "1abc2",
#   "pqr3stu8vwx",
#   "a1b2c3d4e5f",
#   "treb7uchet",
# ]

# document = [
#   "two1nine",
#   "eightwothree",
#   "abcone2threexyz",
#   "xtwone3four",
#   "4nineeightseven2",
#   "zoneight234",
#   "7pqrstsixteen",
# ]

document = [
  x.rstrip() for x in
  open(path + '/day1.txt').readlines()
]

def find_digit(line: str):
  for char in line:
    if char.isnumeric():
      return char
  return None

def part_one():
  total = 0 
  for calibration in document:
    first = find_digit(calibration)
    calibration = reversed(calibration)
    second = find_digit(calibration)
    num = int(first + second)
    total += num
  print(total)
  
digits = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

def digitize(line: str, reversed=False):
  direction = -1 if reversed else 1
  res = ""
  line = list(line)
  found = False
  for char in line[::direction]:
    if reversed:
      res = char + res
    else:
      res += char
    if found:
      continue
    for digit in digits:
      if digit in res:
        res = res.replace(digit, digits[digit])
        found = True
  return ''.join(res)
    
def part_two():
  total = 0
  for calibration in document:
    digitized = digitize(calibration)
    first = find_digit(digitized)
    
    digitized = digitize(calibration, reversed=True)
    second = find_digit(reversed(digitized))
    
    num = int(first + second)
    total += num
  print(total)

# part_one()
part_two()