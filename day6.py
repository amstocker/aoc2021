import functools

with open("day6_input.txt") as f:
    data = list(map(int, f.read().strip().split(',')))

@functools.lru_cache
def simulate(x, n):
    if n <= x:  return 1
    else:       return simulate(7, n - x) + simulate(9, n - x)

# part 1
print(sum(simulate(x, 80) for x in data))

# part 2
print(sum(simulate(x, 256) for x in data))
