nums = [int(x) for x in open('../input/day1.txt').readlines()]

def part_one():
    count = 0
    for i, num in enumerate(nums[:-1]):
        if num < nums[i+1]:
            count += 1
    print(count) 

def part_two():
    count = 0
    for i in range(2, len(nums)):
        prev = sum(nums[i-2:i+1])
        curr = sum(nums[i-1:i+2])
        if prev < curr:
            count += 1
    print(count) 

# part_one()
part_two()