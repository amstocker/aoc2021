import functools

@functools.lru_cache
def simulate(x, n):
    if n <= x:
        return 1
    else:
        return simulate(7, n - x) + simulate(9, n - x)

def simulate_list(data, n):
    return sum([simulate(x, n) for x in data])


with open("day6_input.txt") as f:
    data = list(map(int, f.read().strip().split(',')))

# part 1
print(simulate_list(data, 80))

# part 2
print(simulate_list(data, 256))
