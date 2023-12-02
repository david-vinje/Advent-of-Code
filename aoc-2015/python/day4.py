import hashlib

# read input
secret_key = 'bgvyzdsv'

def count_zeros(n, s):
    count = 0
    while s[count] == '0' and n > count:
        count += 1
    return count >= n

def solve(n):
    count = 0
    while True:
        hash = hashlib.md5(f'{secret_key}{count}'.encode()).hexdigest()
        if count_zeros(n, hash):
            print(count)
            break
        count += 1


# part one
solve(5)

# part two
solve(6)
