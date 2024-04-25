lines = [line.rstrip() for line in open('./input/day1.txt').readlines()]

def part_one():
    res = 0
    for line in lines:
        digits = [x for x in line if x.isdigit()]
        a, b = digits[0], digits[-1]
        res += int(a+b)
    print(res)

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3', 
    'four': '4',
    'five': '5', 
    'six': '6', 
    'seven': '7',
    'eight': '8', 
    'nine': '9'
}
digits = list('0123456789') + list(numbers.keys())

def find_digits(line: str):
    first_index, last_index = len(line), -1
    first_digit, last_digit = '', ''
    for digit in digits:
        i = line.find(digit)
        if i > -1:
            if i < first_index:
                first_index = i
                if digit in numbers.keys():
                    first_digit = numbers[digit]
                else:
                    first_digit = digit
        i = line.rfind(digit)
        if i > -1:
            if i > last_index:
                last_index = i
                if digit in numbers.keys():
                    last_digit = numbers[digit]
                else:
                    last_digit = digit
    return first_digit + last_digit

def part_two():
    res = sum([int(find_digits(line)) for line in lines])
    print(res)
    
# part_one()
part_two()